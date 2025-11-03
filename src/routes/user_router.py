from fastapi import APIRouter, Body, HTTPException, Depends, status
from fastapi.responses import JSONResponse

from src.models.user_model import *
from src.utils.utils import retira_vazios
from src.repository.user_repository import UserRepository
from src.dependencias.db.conexao_postgres import ConexaoPostgres

user_router = APIRouter(prefix='/user', tags=['Usuários'])

def get_db_connection():
  return ConexaoPostgres() 
  
def get_user_repository(db: ConexaoPostgres = Depends(get_db_connection)):
  return UserRepository(db)

@user_router.post("/", response_model=list[UsersModel]) 
async def list_user(user: UserList = Body(), repo: UserRepository = Depends(get_user_repository)):
  param = {
    'username': user.nome
  }
  
  result = repo.get_usuarios(retira_vazios(param))
  
  if not result:
    return JSONResponse(
      content={
        "success": True,
        "message": "Nenhum usuário encontrado."
      }, status_code=200)

  return result