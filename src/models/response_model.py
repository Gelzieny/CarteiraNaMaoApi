from pydantic import BaseModel

class UserResponse(BaseModel):
  codigo: int
  message: str