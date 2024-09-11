from db import models
from db.session import DBSession
from schemas import v1 as schemas_v1
from utils.security import hash_password


class UserRepository:
    def __init__(self, db: DBSession):
        self.db = db

    def create(self, user_create: schemas_v1.UserCreate) -> models.User:
        hashed_password = hash_password(user_create.password)
        new_user = models.User(
            username=user_create.username,
            email=user_create.email,
            hash_password=hashed_password,
        )
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def get_by_id(self, user_id: int) -> models.User:
        return self.db.query(models.User).filter(models.User.id == user_id).first()

    def get_by_email(self, email: str) -> models.User:
        return self.db.query(models.User).filter(models.User.email == email).first()

    def update(self, user_id: int, user_update: dict) -> models.User:
        user = self.get_by_id(user_id)
        for key, value in user_update.items():
            setattr(user, key, value)
        self.db.commit()
        return user

    def delete(self, user_id: int):
        user = self.get_by_id(user_id)
        if user:
            self.db.delete(user)
            self.db.commit()
