from fastapi import FastAPI
from crud import test_router
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="password",
    database="inchuzumes",
    cursor_factory=RealDictCursor
    )

cursor = conn.cursor()


@app.get("/")
def get_a():
    return "A"


app.include_router(test_router)
