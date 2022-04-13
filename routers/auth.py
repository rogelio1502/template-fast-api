from fastapi import APIRouter


from .admin import router_admin

auth_router = APIRouter(
    prefix="/auth",
)


auth_router.include_router(router_admin)
