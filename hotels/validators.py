import re
from django.core.exceptions import ValidationError
from rest_framework.serializers import ValidationError


# 객실 등록에 있어 지점과 객실이름에 특수문자를 등록하지 못하게 유효성 검사를 하는 것
def contains_special_character(name):
    name_regex = re.compile(r"^[a-zA-Z가-힣0-9\s]+$")
    if not name_regex.findall(name):
        raise ValidationError('이름에 특수문자와 초성을 사용할 수 없습니다!')
    return name


# 전화번호의 유효성 Django의 모듈 phonenumbers를
def validate_phone_number(phone_number):
    pattern_no_hyphen = re.compile(r"^(010|012|0133|015|"
                                   r"02|031|033|041|042|043|044|051|052|053|054|055|061|062|063|064)"
                                   r"[^0][0-9]{3,4}[0-9]{4}$")
    if not pattern_no_hyphen.match(phone_number):
        raise ValidationError('올바른 전화 번호를 입력해 주세요!')
    return phone_number



