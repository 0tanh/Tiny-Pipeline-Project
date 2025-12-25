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



import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

config = {
    'user': 'Betty',
    'password': '',
    'host': '127.0.0.1',
    'port': '8001',
    'dbname': 'local_test'
}

new_database_name = 'local_db'

try:
    conn = psycopg2.connect(**config)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
except ConnectionRefusedError:
    print("still not workign bitch")

with conn.cursor() as cur:
    cur.execute(sql.SQL("CREATE DATABASE {}").format(
        sql.Identifier(new_database_name))
    )

print(f"Database '{new_database_name}' created successfully!")
conn.close()



