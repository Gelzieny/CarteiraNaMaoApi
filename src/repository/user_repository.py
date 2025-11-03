
from src.dependencias.db.conexao_postgres import ConexaoPostgres
from src.models.auth_model import CrendentialsModel
from src.models.user_model import UsersModel

class UserRepository:
  def __init__(self, db_connection: ConexaoPostgres):
    self.cx = db_connection
    
  def get_usuarios(self, user: dict) -> dict:
    sql = """ SELECT CODIGO NOME, LOGIN, EMAIL, PASSWORD_HASH FROM USUARIOS WHERE 1 = 1 """
    
    if "username" in user:
      sql += "AND NOME = :username"
    
    if "email_user" in user:
      sql += "AND EMAIL = :email_user" 
      
    sql += f"""ORDER BY NOME ASC"""  
  
    ret = self.cx.select(sql, user)
    
    return ret