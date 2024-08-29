import sqlite3

con = sqlite3.connect()     # Connection
cur = con.cursor()                                            # Cursor

cur.execute()
for row in cur.fetchall():
    print(row[0],row[1],row[2])