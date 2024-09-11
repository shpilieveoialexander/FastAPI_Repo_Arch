from db.session import DBSession
from repositories.user_repository import UserRepository
from schemas import v1 as schemas_v1


class UserService:
    def __init__(self, db: DBSession):
        self.user_repository = UserRepository(db)

    def create_user(self, user_create: schemas_v1.UserCreate):
        return self.user_repository.create(user_create)

    def get_user(self, user_id: int):
        return self.user_repository.get_by_id(user_id)

    def update_user(self, user_id: int, user_update: dict):
        return self.user_repository.update(user_id, user_update)

    def delete_user(self, user_id: int):
        return self.user_repository.delete(user_id)
