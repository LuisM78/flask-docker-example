import os
import psycopg2
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        conn = psycopg2.connect(
            host="db",
            database="mydb",
            user="myuser",
            password="mypass"
        )
        return "Change 5 Another change Connected to PostgreSQL from Flask in Docker Luis!"
    except Exception as e:
        return f"Error: {e}"
