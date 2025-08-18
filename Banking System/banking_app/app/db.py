import sqlite3

TEST_MODE = False
DB_PATH = ":memory:" if TEST_MODE else "bank.db"

def get_conn():
    return sqlite3.connect(DB_PATH)

def init_db():
    with get_conn() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                account_number TEXT UNIQUE NOT NULL,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                balance REAL DEFAULT 0
            );
        """)
        conn.commit()

def set_test_mode(enabled=True):
    global TEST_MODE, DB_PATH
    TEST_MODE = enabled
    DB_PATH = ":memory:" if enabled else "bank.db"
