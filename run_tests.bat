@echo off
REM ============================================================
REM  Script: run_tests.bat
REM  Descrição: Ativa o ambiente virtual e executa os testes da API
REM ============================================================

echo ------------------------------------------------------------
echo 🔹 Ativando ambiente virtual...
echo ------------------------------------------------------------
call venv\Scripts\activate

echo ------------------------------------------------------------
echo 🧪 Executando testes com cobertura...
echo ------------------------------------------------------------
pytest -v || goto :error

echo ------------------------------------------------------------
echo 📊 Gerando relatório de cobertura...
echo ------------------------------------------------------------
coverage run -m pytest
coverage report
coverage html

echo ------------------------------------------------------------
echo ✅ Testes concluídos com sucesso!
echo Relatório HTML disponível em: htmlcov\index.html
echo ------------------------------------------------------------

REM (Opcional) subir o servidor FastAPI depois dos testes
REM echo ------------------------------------------------------------
REM echo 🚀 Iniciando o servidor FastAPI...
REM echo ------------------------------------------------------------
REM uvicorn src.manage:app --reload --host 0.0.0.0 --port 8088

goto :end

:error
echo ------------------------------------------------------------
echo ❌ Erro ao rodar os testes!
echo ------------------------------------------------------------
exit /b 1

:end
REM Desativa o ambiente virtual
deactivate
