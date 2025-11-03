from fastapi import APIRouter, Body


from src.models.auth_model import *
from src.services.auth_service import *

auth_router = APIRouter()

service = AuthService(tags=['Auth'])


@auth_controller.post('/auth', responses={
    200: {'model': TokenModel}
})
async def get_date_example(user: CrendentialsModel = Body()):
    return await service.verify_login(user)
