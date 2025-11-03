from typing import Optional
from pydantic import BaseModel, Field


class UserList(BaseModel):
  nome: Optional[str] =  Field()
  login: Optional[str] =  Field()

class UserModel(BaseModel):
  nome_completo: str =  Field(..., example="Teste da Silva")
  login: str = Field(..., example="login")
  email: str = Field(..., example="teste@email.com")
  password: str = Field(..., example="123456")
  
class UserUpdateModel(BaseModel):
  username: Optional[str] = Field()
  email: Optional[str] = Field()
  password: Optional[str] = Field()
  
class UsersModel(BaseModel):
  codigo: Optional[str] =  Field()
  nome: Optional[str] =  Field()
  login: Optional[str] =  Field()
  email: Optional[str] = Field()
  