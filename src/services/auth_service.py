from src.dependencias.jwt import *
from src.models.auth_model import *
from src.repository.auth_repository import UserRepository

class AuthService:
  async def verify_login(self, user: CrendentialsModel) -> TokenModel:
    dao = UserRepository()
    user = dao.check_credentials(user)
    if user is None:
      return {}, 401

    return TokenModel(
      access_token=create_jwt_token(dict(user))
    )
