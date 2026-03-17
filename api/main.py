from fastapi import FastAPI

from infrastructure.database import create_db_and_tables
from presentation.router import router

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(router)