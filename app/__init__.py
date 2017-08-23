from flask import Flask
import sqlite3
DATABASE_PATH = 'database.sqlite3'

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
app.database = 'database.sqlite3'
from app import views


def get_db():
    db = getattr(g, '_db', None)
    if db is None:
        db = g._db = sqlite3.connect(DATABASE_PATH)
    return db

def close_connection():
    db = getattr(g, '_db', None)
    if db:
        db.close()
