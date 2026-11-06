"""
    Pydantic 모델 : 요청 / 응답 데이터의 모양과 검증 규칙을 정의
"""
from pydantic import BaseModel, Field, ConfigDict

class ItemCreate(BaseModel):
    """
    - name  : 1 ~ 50자 문자열
    - price : 0 보다 큰 정수 gt
    """
    name: str = Field(min_length=1, max_length=50)
    price: int = Field(gt=0)


class UserCreate(BaseModel):
    """
    - username : 1 ~ 50자 문자열
    - password : 1 ~ 20자 문자열
    """
    username: str = Field(min_length=1, max_length=50)
    password: str = Field(min_length=1, max_length=20)


# {"id": xx, "username": "xxx"}
class UserOut(BaseModel):
    id: int
    username: str

# ------------------------------------------------------------------
# {"title": "xxxxx"}
class TodoCreate(BaseModel):
    """
    - title : str (1 자 이상)
    """
    title: str = Field(min_length=1)


class TodoOut(BaseModel):
    """
    DB에서 조회한 후, ORM --> 응답
    """
    # from_attributes=True : ORM 객체의 속성을 읽어서 변환하도록 허용
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    done: bool