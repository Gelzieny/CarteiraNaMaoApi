import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.manage import app
from fastapi.testclient import TestClient


client = TestClient(app)

def test_root():
  response = client.get("/monitor")
  assert response.status_code == 200
  assert response.json() is True
