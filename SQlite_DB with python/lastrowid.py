import sqlite3
con=sqlite3.connect("C:/SQLite3/student")
cur=con.cursor()
cur.execute("insert into students values(9,'ajay','aids',56000)")
id = cur.lastrowid
print('last row id:',id)
con.close()

