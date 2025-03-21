from flask import Flask, jsonify, request, send_from_directory
import pymysql
import os
import time

app = Flask(__name__)

db_config = {
    "host": os.environ.get("DB_HOST", "localhost"),
    "user": os.environ.get("DB_USER", "root"),
    "password": os.environ.get("DB_PASSWORD", ""),
    "database": os.environ.get("DB_NAME", "flaskdb")
}

def get_connection(retries=5):
    while retries > 0:
        try:
            conn = pymysql.connect(**db_config)
            return conn
        except Exception as e:
            print(f"DB connection failed: {e}")
            retries -= 1
            time.sleep(2)
    raise Exception("Could not connect to DB")

@app.route('/')
def dashboard():
    return send_from_directory('.', 'dashboard.html')

@app.route('/greet', methods=['POST'])
def add_greeting():
    data = request.get_json()
    greeting = data.get("message", "Hello!")
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("CREATE TABLE IF NOT EXISTS greetings (id INT AUTO_INCREMENT PRIMARY KEY, message VARCHAR(255))")
        cur.execute("INSERT INTO greetings (message) VALUES (%s)", (greeting,))
    conn.commit()
    conn.close()
    return jsonify(status="stored", message=greeting)

@app.route('/greet', methods=['GET'])
def list_greetings():
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute("SELECT id, message FROM greetings")
        rows = cur.fetchall()
    conn.close()
    return jsonify(greetings=[{"id": row[0], "message": row[1]} for row in rows])

@app.route('/health')
def health():
    return jsonify(status="OK")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
