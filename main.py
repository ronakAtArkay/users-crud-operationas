from typing import List
import crud, schemas, models
from database import sessionLocal, engine
from fastapi import FastAPI, Depends, HTTPException 
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind = engine)

app = FastAPI()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users")
def new_user(user:schemas.userBase ,db : Session = Depends(get_db)):
    users = crud.create_user(db = db, user = user)
    if users is None:
        raise HTTPException(status_code= 400, detail= "User already exist")
    return users

@app.get("/users/", response_model= List[schemas.ShowUser])
def get_users(skip : int = 0, limit : int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip, limit)
    if users is None:
        raise HTTPException(status_code= 404, detail= "User not found")
    return users


@app.get("/users/{mobileno}", response_model=schemas.ShowUser)
def get_user_number(mobileno : str , db: Session = Depends(get_db)):
    users = crud.get_user(db, mobileno)
    if users is None:
        raise HTTPException(status_code= 404, detail= "User not found")
    return users

@app.get("/users/{user_email}/", response_model=schemas.ShowUser)
def get_user_email(user_email : str, db: Session = Depends(get_db)):
    users = crud.get_user_email(db, user_email)
    if users is None:
        raise HTTPException(status_code= 404, detail= "User not found")
    return users

@app.put("/users/{user_id}", response_model=schemas.ShowUser)
def update_user(user_detail: schemas.userBase, user_id : str, db:Session = Depends(get_db)):
    users = crud.update_user(db, user_id, user_detail)
    return users

@app.delete("/users/{user_id}")
def delete_user(user_id : str, db: Session = Depends(get_db)):
    users = crud.delete_user(db, user_id)
    if users:
        return "User are deleted successfully"

