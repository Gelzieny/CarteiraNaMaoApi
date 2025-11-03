import re
import bcrypt
from fastapi import HTTPException


def retira_vazios(param):
  ret = {}
  for i in param:
    if not (len(str(param[i])) == 0  or param[i] is None):
      ret.update({i: param[i]})

  return ret


def email_valido(email: str) -> bool:
  """
  Valida o formato de e-mail (aceita domínios com múltiplos pontos, hífens e subdomínios).
  """
  if not email:
      return False
  
  padrao = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
  return re.match(padrao, email) is not None

def validar_campos_obrigatorios(dados: dict, campos_obrigatorios: list[str]):
  """
  Verifica se os campos obrigatórios estão preenchidos.
  Lança HTTPException caso algum campo esteja vazio, None ou apenas espaços.
  """
  for campo in campos_obrigatorios:
    valor = dados.get(campo)
    if valor is None or (isinstance(valor, str) and not valor.strip()):
      raise HTTPException(
        status_code=400,
        detail=f"O campo '{campo}' é obrigatório e não pode estar vazio."
      )
      
def gerar_hash_senha(senha: str) -> str:
  """
  Criptografa uma senha em texto puro usando bcrypt.
  """
  if not senha:
    return None
  
  senha_bytes = senha.encode('utf-8')
  salt = bcrypt.gensalt()
  hash_senha = bcrypt.hashpw(senha_bytes, salt)
  
  return hash_senha.decode('utf-8')      

def verificar_senha(senha: str, hash_senha: str) -> bool:
  """
  Compara a senha informada com o hash armazenado.
  """
  if not senha or not hash_senha:
    return False
  
  return bcrypt.checkpw(senha.encode('utf-8'), hash_senha.encode('utf-8'))
