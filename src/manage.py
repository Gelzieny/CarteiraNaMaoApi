from fastapi import FastAPI
from starlette.responses import RedirectResponse

from src.routes.user_router import user_router

app = FastAPI(
  title="Carteira Na Mão API",
  description="API para controle financeiro pessoal, construída com FastAPI.",
  version="1.0.0"
)

app.include_router(user_router)

@app.get("/", include_in_schema=False)
async def redirect_to_docs():
  return RedirectResponse(url="/docs")

@app.get("/monitor", tags=["Health"])
async def statusaplicacao():
  return True