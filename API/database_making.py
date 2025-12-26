# import sqlite3

# with sqlite3.connect("testingReactPassing.db") as conn:
#     curr = conn.cursor()
#     curr.execute("CREATE TABLE names(name, time)")
#     conn.commit()

# import psycopg2
# from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
# from psycopg2 import sql
# import contextlib

# with contextlib.closing(psycopg2.connect( 
#                                          database="local_test",
#                                          host='',
#                                          user='Betty',
#                                          password='')) as conn:
#     conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#     with conn.cursor() as cur:
#         cur.execute(sql.SQL("CREATE DATABASE {}")).format(sql.Identifier("local_test"))

# Source - https://stackoverflow.com/a
# Posted by Tom-db, modified by community. See post 'Timeline' for change history
# Retrieved 2025-12-26, License - CC BY-SA 4.0


from datetime import datetime
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

config = {
    'user': 'bettypotgieter',
    'password': '',
    'host': '127.0.0.1',
    'port': '5432',
    'dbname': 'bettypotgieter'
}


conn = psycopg2.connect(**config)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)


with conn.cursor() as cur:
    # cur.execute(sql.SQL("""CREATE TABLE names (
    #     name VARCHAR(50) UNIQUE NOT NULL, 
    #     time VARCHAR(50) UNIQUE NOT NULL)"""))
    t = str(datetime.now()).replace(" ","-").replace(":","_").strip()[0:40]
    print(t)
    cur.execute(sql.SQL(f"INSERT INTO names VALUES ('WOW', '{t}')"))
    
conn.commit()
conn.close()



