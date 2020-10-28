import sqlite3
conn = sqlite3.connect("db")
cur = conn.cursor()
cur.execute("select * from CAR_ID limit 5;")
results = cur.fetchall()
print(results)
