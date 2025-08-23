from db import get_conn
from logger import logger

def register_user(name, account_number, username, password):
    try:
        with get_conn() as conn:
            conn.execute(
                "INSERT INTO users (name, account_number, username, password, balance) VALUES (?, ?, ?, ?, 0)",
                (name, account_number, username, password)
            )
            conn.commit()
            logger.info(f"User '{username}' registered.")
            return True
    except Exception as e:
        logger.warning(f"Registration failed: {e}")
        return False

def login_user(username, password):
    with get_conn() as conn:
        cur = conn.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        return cur.fetchone() is not None

def deposit(username, amount):
    with get_conn() as conn:
        conn.execute("UPDATE users SET balance = balance + ? WHERE username = ?", (amount, username))
        conn.commit()
        logger.info(f"Deposited {amount} to '{username}'.")
        return True

def withdraw(username, amount):
    with get_conn() as conn:
        cur = conn.execute("SELECT balance FROM users WHERE username = ?", (username,))
        row = cur.fetchone()
        if not row or row[0] < amount:
            return False
        conn.execute("UPDATE users SET balance = balance - ? WHERE username = ?", (amount, username))
        conn.commit()
        logger.info(f"Withdrew {amount} from '{username}'.")
        return True

def get_balance(username):
    with get_conn() as conn:
        cur = conn.execute("SELECT balance FROM users WHERE username = ?", (username,))
        row = cur.fetchone()
        return row[0] if row else 0

def get_user_data(username):
    with get_conn() as conn:
        cur = conn.execute("SELECT name, account_number FROM users WHERE username = ?", (username,))
        row = cur.fetchone()
        if row:
            return {"name": row[0], "account_number": row[1]}
        return {}
