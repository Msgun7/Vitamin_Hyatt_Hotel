from django.urls import reverse
# from rest_framework.test import APITestCase
# from django.test.client import MULTIPART_CONTENT, encode_multipart, BOUNDARY
# from PIL import Image
# from users.models import User
# import tempfile


# def get_temporary_image(temp_file):
#     size = (200, 200)
#     color = (255, 0, 0, 0)
#     image = Image.new("RGBA", size, color)
#     image.save(temp_file, 'png')
#     return temp_file


# class RoomsCreateTest(APITestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.data = {'username': 'Jgun', 'password': '1234'}
#         cls.users = User.objects.create_user('Jgun', '1234')
#         cls.article_data = {'spot': 'spot name', 'image': 'rooms_image'}


# def test_create_rooms_with_image(self):
#         temp_file = tempfile.NamedTemporaryFile()
#         temp_file.name = 'image.png'
#         image_file = get_temporary_image(temp_file)
#         image_file.seek(0)
#         self.article_data['image'] = image_file
#         response = self.client.post(
#             path=reverse('room_view'),
#             HTTP_AUTHORIZATION=f"Bearer {self.access_token}",
#             data = encode_multipart(data=self.article_data, boundary=BOUNDARY),
#             content_type=MULTIPART_CONTENT
#         )
#         self.assertEquals(response.status_code, 200)