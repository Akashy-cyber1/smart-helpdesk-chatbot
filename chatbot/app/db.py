import psycopg2

conn = psycopg2.connect(
    dbname="chatbot",
    user="postgres",
    password="password",
    host="localhost"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS chats (
    id SERIAL PRIMARY KEY,
    message TEXT,
    response TEXT
)
""")

conn.commit()