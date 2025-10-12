import sqlite3

conn = sqlite3.connect("my_database.db")  # creates file if not exists
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
""")
conn.commit()

cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 30))
conn.commit()

cursor.execute("SELECT * FROM users")  # to get the whole table data
rows = cursor.fetchall()

for row in rows:
    print(row)