from django.urls import reverse
from rest_framework.test import APITestCase
from users.models import User
from .models import Rooms, Book, Spots
from faker import Faker
from .serializers import DetailSerializer, RoomsSerializer, SpotSerializer

class RoomViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(email='miyeong@naver.com', password='1234')
        cls.data = {'email': 'miyeong@naver.com', 'password': '1234'}
        cls.room_data = {'spot': 1, 'name': 'hi', 'price':10000, 'max_members':3,
                         'status':'empty', 'description':'hihi'}
        cls.spot = Spots.objects.create(name='대구점', call_number='123679', location='gdsgs')
        cls.faker = Faker()
        cls.rooms = []
        for i in range(10):
            cls.rooms.append(Rooms.objects.create(
                spot=cls.spot,
                name=cls.faker.sentence(),
                price=10000,
                status='empty',
                max_members=3,
                description=cls.faker.sentence()
            ))

    def setUp(self):
        self.access_token = self.client.post(reverse('login'), self.data).data['access']

    # 방 등록
    def test_create_room(self):
        response = self.client.post(
            path=reverse('rooms_view'),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
            data=self.room_data
        )
        self.assertEquals(response.status_code, 201)

    # 방 목록
    def test_get_room(self):
        response = self.client.get(
            path=reverse('rooms_view'),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
        )
        self.assertEquals(response.status_code, 200)

    # 방 상세 정보
    def test_get_detail_room(self):
        for room in self.rooms:
            url = room.get_absolute_url()
            response = self.client.get(path=url, HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
            serializer = RoomsSerializer(room).data
            for k, v in serializer.items():
                self.assertEquals(response.data[k], v)

    # 방 정보 수정
    def test_patch_room(self):
        for room in self.rooms:
            url = room.get_absolute_url()
            response = self.client.patch(path=url,
                                         HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
                                         data={'name': self.faker.sentence()})
            self.assertEquals(response.status_code, 200)

    # 방 삭제
    def test_delete_room(self):
        for room in self.rooms:
            url = room.get_absolute_url()
            response = self.client.delete(path=url, HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
            self.assertEquals(response.status_code, 204)

class SpotViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(email='miyeong@naver.com', password='1234')
        cls.data = {'email': 'miyeong@naver.com', 'password': '1234'}
        cls.spot_data = {'name':'대구점', 'call_number':'12390723', 'location':'ahlwfsdf'}
        cls.faker = Faker()
        cls.spots = []
        for i in range(10):
            cls.spots.append(Spots.objects.create(
                name=cls.faker.sentence(),
                call_number=cls.faker.random_int(min=10000000, max=99999999),
                location=cls.faker.sentence()
            ))

    def setUp(self):
        self.access_token = self.client.post(reverse('login'), self.data).data['access']

    # 지점 생성
    def test_creat_spot(self):
        response = self.client.post(
            path=reverse('spot_view'),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
            data=self.spot_data
        )
        self.assertEquals(response.status_code, 201)

    # 지점 목록
    def test_get_spot(self):
        response = self.client.get(
            path=reverse('spot_view'),
            HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
        )
        self.assertEquals(response.status_code, 200)

    # 지점 수정
    def test_patch_spot(self):
        for spot in self.spots:
            url = spot.get_absolute_url()
            response = self.client.patch(path=url,
                                         HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
                                         data={'name': self.faker.sentence()})
            self.assertEquals(response.status_code, 200)

    # 지점 삭제
    def test_delete_room(self):
        for spot in self.spots:
            url = spot.get_absolute_url()
            response = self.client.delete(path=url, HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
            self.assertEquals(response.status_code, 204)

