from fastapi import APIRouter

router = APIRouter(
    prefix="/lists",
    tags=["TODOリスト"],
)

@router.get("/{todo_list_id}")
def get_todo_list(todo_list_id: int):
    return {"todo_list_id": todo_list_id}

@router.post("/")
def post_todo_list():
    return {"message": "TODOリストを作成しました"}

@router.put("/{todo_list_id}")
def put_todo_list(todo_list_id: int):
    return {"todo_list_id": todo_list_id}

@router.delete("/{todo_list_id}")
def delete_todo_list(todo_list_id: int):
    return {"todo_list_id": todo_list_id}