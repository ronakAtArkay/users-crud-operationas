from pydantic import BaseModel, Field
from datetime import datetime

class userBase(BaseModel):
    first_name : str
    last_name : str
    email : str
    password : str
    mobile_number : str = Field(min_length=10, max_length=10)
    image : str

    class Config:
        orm_mode = True

class ShowUser(BaseModel):
    first_name : str
    last_name : str
    email : str
    password : str
    mobile_number : str = Field(min_length=10, max_length=10)
    image : str
    created_at : datetime
    updated_at : datetime
    is_deleted : datetime

    class Config:
        orm_mode = True