# Vitamin_Hyatt_Hotel_Front

---

![](/css/assets/logo.png)

## 소개 



가상의 호텔 Vitamin Hyatt Hotel을 관리하고 이용하기위한 목적을 가진 페이지입니다.

관리자용 기능과 일반 유저용 기능으로 나누어져 있습니다.


---
## 기능구현 
### 공통
1. 회원가입 → users/signup → 필수 요소 : 이름, 이메일, 전화번호
2. 로그인 → users/login
    
---    
### 관리자용 (김미영/연제건)
1. 방 등록 - 위치,서비스 제공 목록, 방 이미지, 설명 → manager/rooms/
2. 방 조회 - boolean → manager/rooms/
3. 방 삭제 - 예약한 사람이 있으면 X → manager/rooms/
4. 방 수정 → manager/rooms/
5. 예약자 명단 조회(이름, 전화번호, 방, 날짜) → manager/book/
<details>
<summary>추가 기능 ( 제작 후반 검토 )</summary>

    룸서비스 예약 조회 

</details>



### 일반회원용 (양예린/장소은/김은수)
1. 숙소 조회 - 지역별/유형별 → users/
1. 숙소 예약&예약 취소 (옵션 선택 : 인원 수 추가, 날짜, 조식 포함, 지점) - 다른 사람이 동시간 같은방을 먼저 예약 했다면 예약할 수 없게 ..   → users/
1. 숙소 북마크  → users/bookmark → 보류!
1. 리뷰,별점 생성 (+공유?) 포인트 적립?  → users/<int:room_id>
1. 방 상세페이지(리뷰포함) → users/<int:room_id>
    리뷰 (별점/평점 카테고리 선택해서 조회할 수 있기 / 페이지네이션)
1. 마이페이지 → 프로필, 예약 조회, 내 리뷰 조회, 탈퇴, 회원정보수정 → users/profile

<details>
<summary>추가 기능 ( 제작 후반 검토 )</summary>

    1. 비회원 예약조회     
    1. 지점별 매니저가 각각 자기 지점만 관리할 수 있도록
    1. 회원가입 이메일 인증
    1. 예약 확정시 문자나 이메일 전송

</details>

---
## 팀

**팀명** : 비타민 B3

**팀 소개** : 상큼한 팀

## 우리 팀 규칙

1. 포기하지 않기
1. 컴다운(**제일 중요!!!**)
1. 프로젝트 기능별 나누기
1. 깃 브랜치 전략 & S.A 작성(와이어프레임(kakao oven), ERD, api 명세) -월요일
1. 각자 기능 제작( 월요일 시작 ~ 목요일 완성목표 (금요일 마지노선) )
1. 기능 Pull merge - 저녁 8시 지정
1. 프론트 제작 (금요일 시작) https://github.com/hanmariyang/off_the_outfit_frontend <<기철 매니저님 프론트엔드 정리
1. Git ReadME 작성

---

### 역할 분담
- 김은수 → 지점별 조회,  예약, 취소, 방등록,  지점 등록 js 매니저에게만 보이게하기
- 연제건 → 방 등록, 조회, 삭제, 객실 상태페이지 구현, 발표 준비
- 김미영 → 방 수정, 예약자 명단 조회,지점 등록, 핸드폰번호 예약가능 달력, 관리자계정 조건, 배포
- 장소은 → 리뷰(별점 포함)CRUD, 방 상세페이지, 마이페이지(예약조회, 리뷰조회), 포인트,  마이페이지, 자바스크립트 POST, GET, 후기작성
- 양예린 → 로그인(JWT토큰사용!), 회원가입, 로그아웃(js), 프로필조회, 탈퇴, 회원정보 수정, 회원가입오류 고치기, 로그인 화면 한정시키기, 마이페이지 불러오기
          

## 언어 모음
    
- HTML
- JavaScript
- CSS
- Python **3.8.6**
- Django 4.2
- DRF 3.14.0



## <일별 계획표>

- 5/8 : s.a작성, erd구성, 와이어프레임 설정, Model작성, repo 생성, merge
- 5/9 : 기능구현
- 5/9 : 진행상태 공유
- 5/10 : merge, 이미지 첨부, 유저기능, 호텔 테스트코드 작성,
- 5/11 : url을 맞추고, view작성 -> 기능완성
- 5/12 : css 와 기능 잇기
- 5/13 : 프론트 엔드와 백엔드 연결하기 & 배포하기 = 2시 모이기
- 5/14 : 계획이 미뤄졌던 항목들 수행 & 배포하기

## 와이어프레임

컨셉 : 호텔 브랜드 예약 사이트
이유 : 백오피스와 유저가 사용하는 플렛폼을 동시에 구현하기에 적절할 것 같아서 입니다!

[와이어프레임 링크](https://ovenapp.io/view/BBWK0bIBH6Gvn2wfO3Lx2L9VwS7NketT/M5h9Q)

## ERD 

-예약 > 예약여부 삭제 
-숙소관리의 지점은  > 하나 추가
-예약 리뷰는 원 투 원
-지점의 위치는 위도 경도를 입력해야함

[ERD 링크](https://www.erdcloud.com/d/XAFNn332mDJ2C2jdr)

## API

### 관리자용 

|관리자 기능|Method|url|request|response|
|------|---|---|---|---|
|방 등록|POST|manager/rooms|manager/rooms|'roomname','description','spot','price','max_members'|{’msg’:’등록완료’, HTTP_201_CREATED}validated_data|
|방 전체 조회|GET|manager/rooms|  |’room_name’, ‘spot’, ‘price’|
|방 삭제|DELETE|manager/rooms/<int:room_id>|room_id|{’msg’:’삭제완료’, HTTP_204_NO_CONTENT}|
|방 수정|PUT|manager/rooms/<int:room_id>|id,room_name,description,spot,price,max_members|{’msg’:’수정완료’, HTTP_200_OK}|
|예약자 명단 조회|GET|manager/customers/<int:room_id>|room_id|{’user’, ’room’, ‘created_at’,’members’}|


### 일반 회원용

|기능|Method|url|request|response|
|------|---|---|---|---|
|숙소 조회|GET|users/|manager/rooms|ID|name, img, comment, hobby, info(1~4)|
|숙소 예약|POST|users/|ID, name, img, intro, hobby, info(1~4)|{msg : ”숙소 예약완료”}|
|예약 취소|PUT|users/|ID, name, img, intro, hobby, info(1~4)|{msg : “예약 취소완료”}|
|숙소 상세조회 및 리뷰 전체 조회|GET|reviews/room/<int:booked_id>/|ID|roomname, description,spot,price,max_members|
|로그인|POST|users/login|email, password|{msg : “로그인 완료”, 200 OK}|
|회원가입|POST|users/signup|email, password, phone-number|{msg : “회원가입 완료”, 201 OK}|
|리뷰 생성|POST|reviews/room/<int:booked_id>|title, content, star|{msg : “리뷰 생성완료”, 201 OK}|
|리뷰 상세 조회|GET|reivews/<int:room_id>|ID||
|리뷰 수정|PUT|reivews/<int:room_id>|ID, title, content, star||
|리뷰 삭제|DELETE|reivews/<int:room_id>|ID||
|검색|GET|users/search/<int:search_id>|title, region|roomname,description,spot,price,mex_members|
|마이페이지 조회|GET|users/search/<int:search_id>|title, region|roomname,description,spot,price,mex_members|
|회원 탈퇴|DELETE|users/search/<int:search_id>|title, region|roomname,description,spot,price,mex_members|
|회원정보 수정|PATCH|users/search/<int:search_id>|title, region|roomname,description,spot,price,mex_members|

---

## 실행



기본적으로 url을 통해 접속하면 되지만 

로컬 환경에서 실행하시고 싶으실 때 
다운로드 받으신 폴더로 이동하셔서 
>! 기본적으로 파이썬 3.8 이상 버전을 설치해주셔야 합니다. 

https://www.python.org/downloads/

```
$ pip install -r requirements.txt
$ python manage.py runserver
```

---
## Contributors


<a href ='https://github.com/MSgun7'><img src="https://github.com/MSgun7.png" alt="프로필 이미지" width="100" height="100" style="margin-right: 10px;"></a>
<a href ='https://github.com/kmy9810'><img src="https://github.com/kmy9810.png" alt="프로필 이미지" width="100" height="100" style="margin-right: 10px;"></a>
<a href ='https://github.com/yell2023'><img src="https://github.com/yell2023.png" alt="프로필 이미지" width="100" height="100" style="margin-right: 10px;"></a>
<a href ='https://github.com/misily'><img src="https://github.com/misily.png" alt="프로필 이미지" width="100" height="100" style="margin-right: 10px;"></a>
<a href ='https://github.com/Soeun-Jan'><img src="https://github.com/Soeun-Jang.png" alt="프로필 이미지" width="100" height="100" style="margin-right: 10px;"></a>
