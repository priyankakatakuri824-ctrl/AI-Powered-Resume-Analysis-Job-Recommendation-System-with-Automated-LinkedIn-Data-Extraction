import sqlite3

conn = sqlite3.connect("resume_app.db")
cur = conn.cursor()

cur.execute("SELECT user_id, name, email, created_at FROM users")
for row in cur.fetchall():
    print(row)

conn.close()
