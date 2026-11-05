from fastapi import APIRouter

# 공통 주소: /todos --> 라우팅 설정(등록)
# * prefix ---> Spring @RequestMapping
router = APIRouter(prefix="/todos")

# [GET] /todos/health
# - response : "ok"
# - 함수명 : health_check
@router.get("/health")
def health_check():
    return "ok"