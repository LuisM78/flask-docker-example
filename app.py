import sqlite3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        conn = sqlite3.connect('mydata.db')
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, text TEXT)')
        cur.execute('INSERT INTO messages (text) VALUES (?)', ('Hello from SQLite inside Docker!',))
        conn.commit()
        cur.execute('SELECT * FROM messages')
        rows = cur.fetchall()
        return f"📦 Messages: {rows}"
    except Exception as e:
        return f"❌ DB error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)