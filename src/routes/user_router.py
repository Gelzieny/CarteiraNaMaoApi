from typing import List
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Body, HTTPException, Depends, status

from src.utils.utils import *
from src.models.user_model import *
from src.models.response_model import UserResponse
from src.repository.user_repository import UserRepository
from src.dependencias.db.conexao_postgres import ConexaoPostgres

user_router = APIRouter(prefix='/user', tags=['Usuários'])

def get_db_connection():
  return ConexaoPostgres() 
  
def get_user_repository(db: ConexaoPostgres = Depends(get_db_connection)):
  return UserRepository(db)

@user_router.post("/", response_model=List[UsersModel]) 
async def list_user(user: UserList = Body(), repo: UserRepository = Depends(get_user_repository)):
  param = {
    'username': user.nome,
    'login': user.login
  }
  
  result = repo.get_usuarios(retira_vazios(param))
  
  if not result:
    return JSONResponse(
      content={
        "success": True,
        "message": "Nenhum usuário encontrado."
      }, status_code=200)

  return result


@user_router.post("/create", response_model=UserResponse) 
async def create_user(user: UserModel = Body(), repo: UserRepository = Depends(get_user_repository)):
  param = {
    'username': user.nome_completo,
    'login': user.login,
    'email': user.email,
    'password': user.password
  }
  
  validar_campos_obrigatorios(param, ['username', 'login', 'email', 'password'])
  
  
  if 'email' in param and not email_valido(param['email']):
    raise HTTPException(status_code=400, detail="E-mail inválido.")
  
  
  param['password_hash'] = gerar_hash_senha(user.password)
  
  
  users_email = repo.get_usuarios({'email_user': param['email']})
  
  if users_email and len(users_email) > 0:
    raise HTTPException(
      status_code=400,
      detail="E-mail já cadastrado no sistema."
    )
  
  result =  repo.create_usuarios(param)
  
  return result