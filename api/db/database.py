import os
from fastapi import Depends
from dotenv import load_dotenv
from sqlmodel import create_engine, Session, SQLModel
from typing import Annotated

load_dotenv()

engine = create_engine(os.getenv("SQL_SERVER_CONN_STR"))

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
