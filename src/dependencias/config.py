from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
  POSTGRES_PRODUCAO_USER: str
  POSTGRES_PRODUCAO_PASSWORD: str
  POSTGRES_PRODUCAO_HOST: str
  POSTGRES_PRODUCAO_PORT: int
  POSTGRES_PRODUCAO_DB: str

  
  SECRET_KEY: str
  ALGORITHM:str
  
  model_config = SettingsConfigDict(
    env_file=[".env"],  
  )

settings = Settings()