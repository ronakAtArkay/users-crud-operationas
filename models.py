from database import Base
from sqlalchemy import Column, String, DateTime, Boolean
from datetime import datetime



class UserModel(Base):
    __tablename__ = "users"

    id = Column(String(200), primary_key = True)
    first_name = Column(String(200))
    last_name = Column(String(200))
    email = Column(String(200))
    password = Column(String(200))
    mobile_number = Column(String(200))
    image = Column(String(255))
    created_at = Column(DateTime, default = datetime.now)
    updated_at = Column(DateTime, default = datetime.now)
    is_deleted = Column(Boolean, default = False)
