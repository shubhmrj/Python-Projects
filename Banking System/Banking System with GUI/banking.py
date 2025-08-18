import json
import os

USER_FILE = "users.json"


def load_users():
    """Loads user data from JSON."""
    if not os.path.exists(USER_FILE):
        return {"users": {}}

    with open(USER_FILE, "r") as file:
        return json.load(file)


def save_users(data):
    """Writes user data to JSON."""
    with open(USER_FILE, "w") as file:
        json.dump(data, file, indent=4)


class BankAccount:
    def __init__(self, user_data):
        self.user_id = user_data["user_id"]
        self.username = user_data["username"]
        self.account_name = user_data["account_name"]
        self.account_number = user_data["account_number"]
        self.account_type = user_data["account_type"]
        self.balance = user_data["balance"]

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self.balance += amount
        self.update_balance()
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= amount
        self.update_balance()
        return self.balance

    def update_balance(self):
        """Updates balance in JSON."""
        data = load_users()
        if self.user_id in data["users"]:
            data["users"][self.user_id]["balance"] = self.balance
            save_users(data)

    def get_balance(self):
        return self.balance
