
from flask import Flask, jsonify, request, send_from_directory
import pymysql
import os
import time

from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from werkzeug.middleware.dispatcher import DispatcherMiddleware

# === Flask REST ===

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
    return send_from_directory(os.path.dirname(__file__), 'dashboard.html')

@app.route('/soap-ui')
def soap_dashboard():
    return send_from_directory(os.path.dirname(__file__), 'soap_dashboard.html')

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


# === SOAP Service ===
class GreetingService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def say_hello(ctx, name):
        try:
            conn = get_connection()
            with conn.cursor() as cur:
                cur.execute("SELECT message FROM greetings ORDER BY id DESC LIMIT 1")
                result = cur.fetchone()
            conn.close()
            if result:
                return f"{result[0]} (to {name})"
            else:
                return f"Hello, {name}!"
        except Exception as e:
            return f"DB error: {str(e)}"

soap_app = Application(
    [GreetingService],
    tns='spyne.greetings.soap',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

# Combine REST + SOAP
application = DispatcherMiddleware(app, {
    "/soap": WsgiApplication(soap_app)
})

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('0.0.0.0', 5000, application)
