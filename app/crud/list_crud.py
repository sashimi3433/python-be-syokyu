from sqlalchemy.orm import Session
from .. import models, schemas

def get_todo_list(db: Session, todo_list_id: int):
    return db.query(models.ListModel).filter(models.ListModel.id == todo_list_id).first()

def create_todo_list(db: Session, todo_list: schemas.NewTodoList):
    db_item = models.ListModel(title=todo_list.title, description=todo_list.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_todo_list(db: Session, db_list: models.ListModel, todo_list: schemas.UpdateTodoList):
    db_list.title = todo_list.title
    db_list.description = todo_list.description
    db.commit()
    db.refresh(db_list)
    return db_list

def delete_todo_list(db: Session, db_list: models.ListModel):
    db.delete(db_list)
    db.commit()
    return db_list