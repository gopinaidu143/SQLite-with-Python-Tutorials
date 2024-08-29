import sqlite3
connection=sqlite3.connect("C:/SQLite3/student")
cur=connection.cursor()
cur.execute("update students set name='raghu' where id=5")
connection.commit()
connection.close()