@echo off
REM Ativa o ambiente virtual
call venv\Scripts\activate

REM Sobe o servidor FastAPI com Uvicorn
uvicorn src.manage:app --reload --host 0.0.0.0 --port 8088

REM Desativa o ambiente virtual
deactivate
