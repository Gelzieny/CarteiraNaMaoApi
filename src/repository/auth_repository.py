
from src.models.user_model import UsersModel
from src.models.auth_model import CrendentialsModel
from src.dependencias.db.conexao_postgres import ConexaoPostgres

class UserRepository:
  def __init__(self, db_connection: ConexaoPostgres):
    self.cx = db_connection
    
  def check_credentials(self, user: CrendentialsModel) -> UsersModel:
    sql = """
      SELECT CODIGO NOME, LOGIN, EMAIL, PASSWORD_HASH FROM USUARIOS
      WHERE LOGIN = :client_id
      AND PASSWORD_HASH = :client_secret
    """
    
    u = self.cx.select(sql, user)
    
    if len(u) == 0:
      return None
      
    u = u[0]
    return UsersModel(
      nome=u['NOME'],
      email=u['CLIENTE'],
      codigo=u['CODIGO']
    )