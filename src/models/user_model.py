from typing import Optional
from pydantic import BaseModel, Field


class UserList(BaseModel):
  nome: Optional[str] =  Field()

class UserModel(BaseModel):
  nome: str =  Field(..., example="teste")
  email: str = Field(..., example="teste@email.com")
  password_hash: str = Field(..., example="123456")
  
class UserUpdateModel(BaseModel):
  username: Optional[str] = Field()
  email: Optional[str] = Field()
  password: Optional[str] = Field()
  
class UsersModel(BaseModel):
  codigo: Optional[str] =  Field()
  nome: Optional[str] =  Field()
  email: Optional[str] = Field()
  