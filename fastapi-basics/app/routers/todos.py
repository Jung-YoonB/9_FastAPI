from fastapi import APIRouter, Depends

from app.schemas import TodoCreate, TodoOut
from app.database import get_db, Session
from app.models import Todo

# 공통 주소: /todos --> 라우팅 설정(등록)
# * prefix ---> Spring @RequestMapping
router = APIRouter(prefix="/todos")

# [GET] /todos/health
# - response : "ok"
# - 함수명 : health_check
@router.get("/health")
def health_check():
    return "ok"

"""
    [GET]    /todos        할 일 목록 조회 (Read)
    [GET]    /todos/{id}   할 일 상세 조회 (Read)
    [POST]   /todos        할 일 등록(생성)(Create)
    [PATCH]  /todos/{id}   할 일 부분 수정 (Update)
    [DELETE] /todos/{id}   할 일 삭제 (Delete)
"""

@router.get("", response_model=list[TodoOut])
def list_todos(db: Session = Depends(get_db)):

    query = db.query(Todo)

    return query.all()

@router.get("/{id}")
def todo_read(id: int):
    return id

@router.post("")
# - request body : {title: "xxxxx"}
def create_todo(body: TodoCreate,
                db: Session = Depends(get_db)):

    todo = Todo(title=body.title)

    db.add(todo)        # 저장 할 객체 등록 (DB 처리 전)
    db.commit()         # DB에 적용

    db.refresh(todo)    # DB에 적용 된 객체를 다시 읽어옴
    
    return todo

@router.patch("/{id}")
def update_todo(id: int):
    return id

@router.delete("/{id}")
def delte_todo(id: int):
    return id