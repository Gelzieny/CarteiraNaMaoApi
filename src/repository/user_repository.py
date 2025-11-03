
from src.dependencias.db.conexao_postgres import ConexaoPostgres
from src.models.auth_model import CrendentialsModel
from src.models.user_model import UsersModel

class UserRepository:
  def __init__(self, db_connection: ConexaoPostgres):
    self.base = db_connection
    
