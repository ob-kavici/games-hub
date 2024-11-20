from fastapi import FastAPI
from app.api.routes import router

app = FastAPI()

app.include_router(router, prefix="/api", tags=["games"])

@app.get("/")
async def read_root():
    return {"service": "games-hub"}