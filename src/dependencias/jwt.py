import jwt

from src.dependencias.config import settings

_JWT_SECRET_KEY = settings.SECRET_KEY
_JWT_ALGORITHM = settings.ALGORITHM


def create_jwt_token(info_data:dict) -> str:
  encoded_jwt = jwt.encode(info_data, _JWT_SECRET_KEY, algorithm=_JWT_ALGORITHM)
  return encoded_jwt


def decode_jwt_token(token: str) -> dict | None:
  try:
    payload: dict = jwt.decode(token, _JWT_SECRET_KEY, algorithms=_JWT_ALGORITHM)
    return payload
  except Exception as e:
    return None
