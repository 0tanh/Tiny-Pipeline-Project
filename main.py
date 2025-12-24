from fastapi import FastAPI
from pydantic import BaseModel, Field

import time
import sqlite3
import os
import contextlib

from datetime import datetime

db = os.getenv("DB")

class UsernameFromReact(BaseModel):
    name:str = Field(example="Betty_At_Home")
    

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/new_name")
async def new_username(username: UsernameFromReact):
    print(username)
    
    data = (
        {"name" : username.name, "time":datetime.now()}
        )
    with contextlib.closing(sqlite3.connect("testingReactPassing.db")) as connection:
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
    with contextlib.closing(sqlite3.connect("testingReactPassing.db")) as connection:
        with connection as conn:
            cur = connection.cursor()
            res = cur.execute("SELECT * FROM names ORDER BY time ASC")
            r = res.fetchone()
    return {
        "entry": r
    }