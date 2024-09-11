from fastapi import APIRouter, Depends, HTTPException, status

from db.session import DBSession, get_session
from schemas import v1 as schemas_v1
from services.user_service import UserService

router = APIRouter()


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schemas_v1.UserResponse
)
def create_user(
    user_create: schemas_v1.UserCreate, db: DBSession = Depends(get_session)
):
    user_service = UserService(db)
    return user_service.create_user(user_create)


@router.get("/{user_id}", response_model=schemas_v1.UserResponse)
def get_user(user_id: int, db: DBSession = Depends(get_session)):
    user_service = UserService(db)
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=schemas_v1.UserResponse)
def update_user(
    user_id: int,
    user_update: schemas_v1.UserUpdate,
    db: DBSession = Depends(get_session),
):
    user_service = UserService(db)

    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    update_data = user_update.dict(exclude_unset=True)
    updated_user = user_service.update_user(user_id, update_data)
    return updated_user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: DBSession = Depends(get_session)):
    user_service = UserService(db)
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user_service.delete_user(user_id)
    return user
