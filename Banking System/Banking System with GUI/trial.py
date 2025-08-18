import os
import json
import random
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pytest

USER_FILE = "users.json"

# ---------------- USER MANAGEMENT ----------------
def load_users():
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w") as file:
            json.dump({"users": {}}, file, indent=4)
    with open(USER_FILE, "r") as file:
        return json.load(file)

def save_users(data):
    with open(USER_FILE, "w") as file:
        json.dump(data, file, indent=4)

def authenticate(user_id, password):
    users = load_users().get("users", {})
    return users.get(user_id) if user_id in users and users[user_id]["password"] == password else None

def signup(username, password, account_type):
    users_data = load_users()
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

# ---------------- BANK ACCOUNT CLASS ----------------
class BankAccount:
    def __init__(self, user_id, user_data):
        self.user_id = user_id
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
        data = load_users()
        if self.user_id in data["users"]:
            data["users"][self.user_id]["balance"] = self.balance
            save_users(data)

    def get_balance(self):
        return self.balance

# ---------------- GUI APPLICATION ----------------
class BankingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("banking_app")
        self.root.geometry("600x500")
        self.current_user = None
        self.bank_account = None
        self.load_background()
        self.login_screen()

    def load_background(self):
        self.bg_image = Image.open("1.jpg").resize((600, 500))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.canvas = tk.Canvas(self.root, width=600, height=500)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.load_background()

    def login_screen(self):
        self.clear_screen()
        frame = tk.Frame(self.root)
        frame.place(relx=0.5, rely=0.5, anchor="center")
        ttk.Label(frame, text="User ID:").grid(row=0, column=0)
        self.user_id_entry = ttk.Entry(frame)
        self.user_id_entry.grid(row=0, column=1)
        ttk.Label(frame, text="Password:").grid(row=1, column=0)
        self.password_entry = ttk.Entry(frame, show="*")
        self.password_entry.grid(row=1, column=1)
        ttk.Button(frame, text="Login", command=self.authenticate_user).grid(row=2, column=1)
        ttk.Button(frame, text="Sign Up", command=self.signup_screen).grid(row=3, column=1)

    def authenticate_user(self):
        user_id = self.user_id_entry.get()
        password = self.password_entry.get()
        user_data = authenticate(user_id, password)
        if user_data:
            self.current_user = user_data["username"]
            self.bank_account = BankAccount(user_id, user_data)
            messagebox.showinfo("Login Successful", f"Welcome, {self.current_user}!")
        else:
            messagebox.showerror("Login Failed", "Invalid User ID or Password")

    def signup_screen(self):
        self.clear_screen()
        frame = tk.Frame(self.root)
        frame.place(relx=0.5, rely=0.5, anchor="center")
        ttk.Label(frame, text="Username:").grid(row=0, column=0)
        self.signup_username = ttk.Entry(frame)
        self.signup_username.grid(row=0, column=1)
        ttk.Label(frame, text="Password:").grid(row=1, column=0)
        self.signup_password = ttk.Entry(frame, show="*")
        self.signup_password.grid(row=1, column=1)
        ttk.Label(frame, text="Account Type:").grid(row=2, column=0)
        self.account_type = ttk.Combobox(frame, values=["Savings", "Checking"])
        self.account_type.grid(row=2, column=1)
        self.account_type.current(0)
        ttk.Button(frame, text="Register", command=self.register_user).grid(row=3, column=1)

    def register_user(self):
        username = self.signup_username.get()
        password = self.signup_password.get()
        account_type = self.account_type.get()
        if username and password:
            user_id = signup(username, password, account_type)
            messagebox.showinfo("Success", f"Account created! Your User ID is: {user_id}")
            self.login_screen()
        else:
            messagebox.showerror("Error", "Please fill all fields")

# ---------------- MAIN ----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = BankingApp(root)
    root.mainloop()
