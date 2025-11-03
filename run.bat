@echo off
title CarteiraNaMao API - FastAPI Server

REM Ativa o ambiente virtual
call venv\Scripts\activate

REM Exibe uma mensagem de inicialização
echo ============================================
echo Iniciando o servidor FastAPI (Uvicorn)
echo Host: 127.0.0.1  Porta: 8088
echo ============================================

REM Executa o servidor
python -m uvicorn src.manage:app --reload --host 127.0.0.1 --port 8088

REM Ao finalizar (Ctrl+C), mantém a janela aberta
echo ============================================
echo Servidor encerrado.
echo ============================================

REM Desativa o ambiente virtual
deactivate

pause
