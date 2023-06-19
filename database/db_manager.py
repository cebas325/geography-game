# File to manage database connection
import pandas as pd
import sqlite3


def connect_db():
    conn = sqlite3.connect("data/standings.db")
    return conn.cursor()


def create_spain_table():
    cur = connect_db()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Spain (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            surname TEXT,
            score FLOAT
        )
    """)