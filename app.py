import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World from Darby Hansen in 3308"

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://lab_10_dq2c_user:O2VsF0jbZhZceKGnbkVqYC4cxSCKLnup@dpg-cqld8irv2p9s73am406g-a/lab_10_dq2c")
    conn.close()
    return "Database connection successful."
