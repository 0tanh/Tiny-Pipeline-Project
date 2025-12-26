import os
from dotenv import load_dotenv

#sqlalchemy imports
from sqlalchemy import create_engine
# from sqlalchemy.orm import DeclarativeBase, Mroutered, mroutered_column, relationship

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
    
