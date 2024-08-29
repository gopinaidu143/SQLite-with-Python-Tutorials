import sqlite3
con=sqlite3.connect("C:/SQLite3/student")
cur=con.cursor()
cur.execute("delete from students where id=4")
con.commit()
con.close()