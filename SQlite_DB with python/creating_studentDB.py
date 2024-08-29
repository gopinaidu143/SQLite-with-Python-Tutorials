import sqlite3
connection=sqlite3.connect("C:\SQLite3\student")
cur=connection.cursor()
cur.execute("create table if not exists students(id int not null,name text(20),branch text(20),fee int);")

connection.commit()
connection.close()