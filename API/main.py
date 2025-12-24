import contextlib
import os
import sqlite3
from datetime import datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


#initilising environment variables
db = os.getenv("TEST_DB")
origins = os.getenv("ORIGINS")

class UsernameFromReact(BaseModel):
    """Basic class for test purposes"""
    name:str = Field(example="Betty_At_Home")
    

app = FastAPI()

app.add_middleware(CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/hw")
async def root():
    return {"message": "Hello World"}

@app.post("/new_name")
async def new_username(username: UsernameFromReact):
    print(username)
    
    data = (
        {"name" : username.name, "time":datetime.now()}
        )
    with contextlib.closing(sqlite3.connect(db)) as connection:
        with connection as conn:
            cur = connection.cursor()
            cur.execute("INSERT INTO 'names' VALUES (:name , :time)", data)
            conn.commit()
    
    return {
        "time": datetime.now(),
        "message":"db_insertion successful"
    }

@app.get("/lastName")
async def last_name():
    with contextlib.closing(sqlite3.connect(db)) as connection:
        with connection as conn:
            cur = connection.cursor()
            res = cur.execute("SELECT * FROM names ORDER BY time DESC")
            r = res.fetchone()
            conn.commit()
    return {
        "entry": r
    }

@app.get("/render_healthcheck")
async def render_health_check():
    return {
        "message":"still kicking"
    }