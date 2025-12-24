import sqlite3

with sqlite3.connect("testingReactPassing.db") as conn:
    curr = conn.cursor()
    curr.execute("CREATE TABLE names(name, time)")
    conn.commit()