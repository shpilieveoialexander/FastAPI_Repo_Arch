from sqlalchemy import Column, String

from db.models import BaseModel


class User(BaseModel):
    __tablename__ = "user"
    username = Column(String(128), nullable=False)
    hash_password = Column(String(128), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
