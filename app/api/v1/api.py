from fastapi import APIRouter
from fastapi_pagination import add_pagination

from .user import router

router_v1 = APIRouter()

router_v1.include_router(router, tags=["User"], prefix="/user")
add_pagination(router_v1)
