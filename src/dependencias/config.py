from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
  POSTGRES_PRODUCAO_USER: str
  POSTGRES_PRODUCAO_PASSWORD: str
  POSTGRES_PRODUCAO_HOST: str
  POSTGRES_PRODUCAO_PORT: int
  POSTGRES_PRODUCAO_DB: str

  
  SECRET_KEY: str
  ALGORITHM:str
  ACCESS_TOKEN_EXPIRE_MINUTES = 60
  
  model_config = SettingsConfigDict(
    env_file=[".env"],  
  )

settings = Settings()