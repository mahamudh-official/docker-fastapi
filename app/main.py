from fastapi import FastAPI
from sqlmodel import create_engine
import os

DATABASE_URL = os.getenv("DATABASE_URL") 

engine = create_engine(DATABASE_URL)

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Docker FastAPI API v2"}

@app.get("/db-test")
def db_test():
    with engine.connect() as connection:
        return {"message": "Database connected"}
