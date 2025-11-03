from fastapi import APIRouter, Body

from src.models.auth_model import TokenModel
from src.models.user_model import UserModel

user_router = APIRouter(prefix='/user', tags=['Usuários'])

@user_router.post('/', responses={
  200: {'model': TokenModel}
})
async def get_list_user(user: CrendentialsModel = Body()):
  pass

