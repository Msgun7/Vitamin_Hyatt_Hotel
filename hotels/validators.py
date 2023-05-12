import re
import phonenumbers
# phonenumber pip install phonenumbers 필요 전화번호 유효성 검사에 있어 해외번호 또한 사용가능하게 하기 위해서 설치
from rest_framework.serializers import ValidationError


# 객실 등록에 있어 지점과 객실이름에 특수문자를 등록하지 못하게 유효성 검사를 하는 것
def contains_special_character(name):
    name_regex = re.compile(r"^[a-zA-Z가-힣0-9\s]+$")
    if not name_regex.findall(name):
        raise ValidationError('이름에 특수문자를 사용할 수 없습니다!')
    return name



# 전화번호의 유효성 Django의 모듈 phonenumbers를 받아와 전화번호의 형식을 판단합니다.

def validate_phone_number(phone_number):
    pattern_no_hyphen = re.compile(r"^(010|012|0133|015|"
                                   r"02|031|033|041|042|043|044|051|052|053|054|055|061|062|063|064)"
                                   r"[^0][0-9]{3,4}[0-9]{4}$")
    if not pattern_no_hyphen.match(phone_number):
        raise ValidationError('올바른 전화 번호를 입력해 주세요!')
    return phone_number
    # try:
    #     parsed_number = phonenumbers.parse(phone_number)
    #     if not phonenumbers.is_valid_number(parsed_number):
    #         raise ValidationError('사용할 수 없는 전화번호입니다. - 과 함께 입력해주세요.')
    # except phonenumbers.phonenumberutil.NumberParseException:
    #     raise ValidationError('사용할 수 없는 전화번호입니다.')



