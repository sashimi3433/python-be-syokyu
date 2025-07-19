from sqlalchemy.orm import Session
from app.const import TodoItemStatusCode
from .. import models, schemas

def get_todo_item(db: Session, todo_item_id: int):
    return db.query(models.ItemModel).filter(models.ItemModel.id == todo_item_id).first()

def create_todo_item(db: Session, todo_list_id: int, todo_item: schemas.NewTodoItem):
    db_item = models.ItemModel(
        todo_list_id=todo_list_id,
        title=todo_item.title,
        description=todo_item.description,
        due_at=todo_item.due_at,
        status_code=TodoItemStatusCode.NOT_COMPLETED
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_todo_item(db: Session, db_item: models.ItemModel, todo_item: schemas.UpdateTodoItem):
    db_item.title = todo_item.title
    db_item.description = todo_item.description
    db_item.due_at = todo_item.due_at
    if todo_item.complete is not None:
        db_item.status_code = (
            TodoItemStatusCode.COMPLETED
            if todo_item.complete else TodoItemStatusCode.NOT_COMPLETED
        )
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_todo_item(db: Session, db_item: models.ItemModel):
    db.delete(db_item)
    db.commit()
    return db_item