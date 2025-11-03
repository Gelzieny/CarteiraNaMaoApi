from pydantic import BaseModel, Field

class TokenModel(BaseModel):
  access_token: str
  expires_in: int = Field(default=3600)
  token_type: str = Field(default="Bearer")


class CrendentialsModel(BaseModel):
  client_id: str = Field(default="")
  client_secret: str = Field(default="")
