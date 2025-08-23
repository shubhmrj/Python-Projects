import json
import os
import random

USER_FILE = "users.json"


def load_users():
    """Loads user data from JSON or creates an empty file if missing."""
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w") as file:
            json.dump({"users": {}}, file, indent=4)

    with open(USER_FILE, "r") as file:
        return json.load(file)


def save_users(data):
    """Writes user data to JSON safely."""
    with open(USER_FILE, "w") as file:
        json.dump(data, file, indent=4)


def authenticate(user_id, password):
    """Authenticates user using ID and password."""
    users = load_users().get("users", {})
    return users.get(user_id) if user_id in users and users[user_id]["password"] == password else None


def signup(username, password, account_type):
    """Registers a new user and stores data in JSON."""
    users_data = load_users()

    # Generate unique user ID
    while True:
        user_id = str(random.randint(1000, 9999))
        if user_id not in users_data["users"]:
            break

    account_number = str(random.randint(1000000000, 9999999999))

    users_data["users"][user_id] = {
        "username": username,
        "password": password,
        "account_name": f"{username}'s Account",
        "account_number": account_number,
        "account_type": account_type,
        "balance": 0.0
    }

    save_users(users_data)
    return user_id
