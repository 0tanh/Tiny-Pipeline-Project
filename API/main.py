#Python Standard Library Imports
import contextlib
import os
from datetime import datetime
from functools import _lru_cache_wrapper
from dotenv import load_dotenv

#FastAPI imports
from fastapi import FastAPI, Response, status
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

#sqlalchemy imports
from sqlalchemy import create_engine, select, insert, delete, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

#Psycopg imports
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# FastAPI config
# # import config

# # @_lru_cache_wrapper
# # def get_settings():
# #     return config.Settings

# # get_settings()

#initilising environment variables
load_dotenv()
db = os.getenv("DB")
origins = os.getenv("ORIGINS")

#load sqlAlchemy engine:
url = os.getenv("DB_URL")    
config = {
    'user': os.getenv('USER'),
    'password': os.getenv('PASSWORD'),
    'host': os.getenv('HOST'),
    'port': os.getenv('PORT'),
    'dbname': os.getenv('DBNAME')
}

if url:
    to_connect = os.getenv("DB_URL")
    engine = create_engine(to_connect)
else:
    to_connect = f"postgresql+psycopg2://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['dbname']}"
    engine = create_engine(to_connect)
    

#Setting Up API Query BaseModels
class UsernameFromReact(BaseModel):
    """Basic class for test purposes"""
    name:str = Field(example="Betty_At_Home")
  
#Initialising Application
app = FastAPI()

app.add_middleware(CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

#API ROUTES
@app.get("/")
async def entry():
    return {"message":"Welcome"}

@app.get("/hw",
         summary="returns a hello world", 
         description="sends a get request and returns a hello world",
         response_description="Literally Just Hello World")
async def hello_world():
    return {"message": "Hello World"}

@app.post("/new_name",
          status_code=201,
          summary="Adds a new user",
          description="Adds a new user and when they joined to my silly little database",
          response_description="Tells you that it was successful")
async def new_username(username: UsernameFromReact):
    data = {
        "name" : username.name, 
        "time":datetime.now()
         }
    
    with contextlib.closing(engine.connect()) as conn:
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute("INSERT INTO names VALUES (%(name)s , %(time)s)", data)
        conn.commit()
    
    return {
        "time": datetime.now(),
        "message":"db_insertion successful"
    }

@app.get("/lastName",
         summary="Last added user",
         description="Asks you for last added user and returns who that is",
         response_description="Tells you the last added user and when they joined")
async def last_name():
    with contextlib.closing(engine.connect()) as conn:
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute("""SELECT * FROM {table} ORDER BY {column} DESC
                    """.format(table="names", 
                               column="time"))
        r = cur.fetchone()
        conn.commit()
    return {
        "name": r[0],
        "when": r[1]
    }

@app.post("/is_it_there")
async def is_it_there(username: UsernameFromReact):
    with contextlib.closing(psycopg2.connect(**config)) as conn:
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor() 
        cur.execute("""
                    SELECT {username} FROM {table}
                    """.format(
                        username=username.name,
                        table="names"))
        r = cur.fetchone()
        conn.commit()

@app.get("/rr", 
         response_class=RedirectResponse,
         summary="Haha",
         description="get rekt skrub",
         response_description="call me and see hehe")
async def rr():
    return "https://youtu.be/dQw4w9WgXcQ"

@app.get("/render_healthcheck")
async def render_health_check():
    return {
        "message":"still kicking"
    }