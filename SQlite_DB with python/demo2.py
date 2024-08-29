import sqlite3
con = sqlite3.connect("C:\SQLite3\student")
cur = con.cursor()
try:
    id = input("Enter id :")
    date = input("Enter Date [yyyy-mm-dd] :")
    desc = input("Enter Description :")
    amt = input("Enter Amount :")
    row = (id,date,desc,amt)
    cur.execute("insert into orders values(?,?,?,?)", row)
    con.commit()
    print("Added successfully!")

except Exception as ex:
    print("Sorry! Error: ", ex)
finally:
    con.close()