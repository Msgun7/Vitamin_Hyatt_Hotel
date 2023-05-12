import re
from rest_framework.serializers import ValidationError

def check_username(username):
    username_regex = re.compile(r"[^ A-Za-z0-9가-힣+]")
    if username_regex.findall(username):
        raise ValidationError('이름에 특수문자와 초성을 사용할 수 없습니다!')
    return username

def check_password(password):
    password_regex = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&^])[A-Za-z\d$@$!%*#?&^]{8,}$"
    if not re.match(password_regex, password):
        raise ValidationError('8자 이상의 영문 대/소문자, 숫자, 특수문자 조합이어야 합니다!')           
    return password

# def check_phone(phone):
#     phone_regex = r"^01[0-9]-\d{3,4}-\d{4}$"
#     if not re.match(phone_regex, phone):
#         raise ValidationError('전화번호를 01*-****-**** 형식으로 입력해주세요!')
#     return phone
