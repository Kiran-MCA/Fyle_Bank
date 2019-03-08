import psycopg2

conn = psycopg2.connect(database = "Bank_Backup", user = "postgres", password = "kiran", host = "127.0.0.1", port = "5432")
print("Opened database successfully")
cur = conn.cursor()
cur.execute("SELECT name,id FROM banks limit 3")
rows = cur.fetchall()
for row in rows:
    print("Name:=",row[0])
    print("Bank_id:=",row[1])




print("Operation done successfully")
conn.close()
