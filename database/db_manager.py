# File to manage database connection
import pandas as pd
import sqlite3


conn = sqlite3.connect("data/standings.db")
pd.read_sql_query("""
    CREATE TABLE IF NOT EXISTS Spain (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT,
    score FLOAT
    )
""")