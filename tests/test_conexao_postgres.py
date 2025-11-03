import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import pytest
from src.dependencias.db.conexao_postgres import ConexaoPostgres

@pytest.fixture(scope="module")
def conexao():
  """Inicializa a conexão apenas uma vez por módulo."""
  return ConexaoPostgres()

def test_conexao_postgres_disponivel(conexao):
  """
  Testa se o banco PostgreSQL está acessível e responde ao SELECT 1.
  """
  resultado = conexao.teste()

  # Exibe o resultado no log do pytest (útil para debugging)
  print(f"Resultado do teste de conexão: {resultado}")

  # Valida que a resposta contém os campos esperados
  assert "status" in resultado
  assert "resultado" in resultado

  # Valida que o status seja de sucesso e o texto correto
  assert resultado["status"] == "success", f"Falha na conexão: {resultado['resultado']}"
  assert "Conexão bem-sucedida" in resultado["resultado"]
