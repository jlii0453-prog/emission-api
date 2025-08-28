from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "railway"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASS", ""),
        port=os.getenv("DB_PORT", "5432")
    )

@app.get("/emissions")
def get_emissions():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM emissions;") 
    rows = cur.fetchall()
    colnames = [desc[0] for desc in cur.description]
    cur.close()
    conn.close()
    return [dict(zip(colnames, row)) for row in rows]
