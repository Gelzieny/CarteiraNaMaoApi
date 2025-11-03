from pydantic import BaseModel, Field

class UserModel(BaseModel):
  nome: str =  Field(..., example="teste")
  email: str = Field(..., example="teste@email.com")
  password_hash: str = Field(..., example="123456")
  
class UserUpdateModel(BaseModel):
  username: Optional[str] = Field()
  email: Optional[str] = Field()
  password: Optional[str] = Field()
  
class UsersModel(BaseModel):
  codigo: str =  Field()
  nome: str =  Field()
  email: str = Field()
  