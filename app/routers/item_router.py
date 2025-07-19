from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..dependencies import get_db

router = APIRouter(
    prefix="/lists/{todo_list_id}/items",
    tags=["TODO項目"],
)

@router.post("/", response_model=schemas.ResponseTodoItem)
def create_item(todo_list_id: int, todo_item: schemas.NewTodoItem, db: Session = Depends(get_db)):
    return crud.item_crud.create_todo_item(db=db, todo_list_id=todo_list_id, todo_item=todo_item)

@router.get("/{todo_item_id}", response_model=schemas.ResponseTodoItem)
def read_item(todo_list_id: int, todo_item_id: int, db: Session = Depends(get_db)):
    db_item = crud.item_crud.get_todo_item(db=db, todo_item_id=todo_item_id)
    if db_item is None or db_item.todo_list_id != todo_list_id:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.put("/{todo_item_id}", response_model=schemas.ResponseTodoItem)
def update_item(todo_list_id: int, todo_item_id: int, todo_item: schemas.UpdateTodoItem, db: Session = Depends(get_db)):
    db_item = crud.item_crud.get_todo_item(db=db, todo_item_id=todo_item_id)
    if db_item is None or db_item.todo_list_id != todo_list_id:
        raise HTTPException(status_code=404, detail="Item not found")
    return crud.item_crud.update_todo_item(db=db, db_item=db_item, todo_item=todo_item)

@router.delete("/{todo_item_id}", response_model=schemas.ResponseTodoItem)
def delete_item(todo_list_id: int, todo_item_id: int, db: Session = Depends(get_db)):
    db_item = crud.item_crud.get_todo_item(db=db, todo_item_id=todo_item_id)
    if db_item is None or db_item.todo_list_id != todo_list_id:
        raise HTTPException(status_code=404, detail="Item not found")
    return crud.item_crud.delete_todo_item(db=db, db_item=db_item)