import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import random

# Dummy User Database
USER_CREDENTIALS = {"admin": "password123"}


class BankAccount:
    def __init__(self, owner, balance=1000, account_type="Savings"):
        self.owner = owner
        self.balance = balance
        self.account_type = account_type
        self.account_number = f"BA-{random.randint(10000, 99999)}"  # Random Account Number
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self.transactions.append(f"{datetime.now().strftime('%H:%M:%S')} - Deposited: ${amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        self.balance -= amount
        self.transactions.append(f"{datetime.now().strftime('%H:%M:%S')} - Withdrew: ${amount}")

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions


class BankingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Banking System with sql")
        self.root.geometry("500x500")
        self.root.resizable(False, False)

        self.current_user = None
        self.bank_account = None

        self.login_screen()

    def login_screen(self):
        """Login Screen"""
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.configure(bg="white")
        ttk.Label(self.root, text="Login", font=("Arial", 20, "bold")).pack(pady=10)

        ttk.Label(self.root, text="Username:").pack(pady=5)
        self.username_entry = ttk.Entry(self.root)
        self.username_entry.pack(pady=5)

        ttk.Label(self.root, text="Password:").pack(pady=5)
        self.password_entry = ttk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        ttk.Button(self.root, text="Login", command=self.authenticate).pack(pady=10)

    def authenticate(self):
        """Authenticates User"""
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            self.current_user = username
            self.bank_account = BankAccount(username)  # Create a new bank account
            self.main_screen()
        else:
            messagebox.showerror("Login Failed", "Invalid Username or Password")

    def main_screen(self):
        """Main Banking Screen"""
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.configure(bg="lightgray")

        ttk.Label(self.root, text=f"Welcome, {self.current_user}!", font=("Arial", 16, "bold")).pack(pady=10)
        ttk.Label(self.root, text=f"Account Number: {self.bank_account.account_number}", font=("Arial", 12)).pack()
        ttk.Label(self.root, text=f"Account Type: {self.bank_account.account_type}", font=("Arial", 12)).pack()

        self.balance_label = ttk.Label(self.root, text=f"Balance: ${self.bank_account.get_balance()}",
                                       font=("Arial", 14))
        self.balance_label.pack(pady=5)

        ttk.Label(self.root, text="Deposit Amount:").pack(pady=5)
        self.deposit_entry = ttk.Entry(self.root)
        self.deposit_entry.pack(pady=5)
        ttk.Button(self.root, text="Deposit", command=self.deposit_money).pack(pady=5)

        ttk.Label(self.root, text="Withdraw Amount:").pack(pady=5)
        self.withdraw_entry = ttk.Entry(self.root)
        self.withdraw_entry.pack(pady=5)
        ttk.Button(self.root, text="Withdraw", command=self.withdraw_money).pack(pady=5)

        ttk.Button(self.root, text="View Transactions", command=self.show_transactions).pack(pady=5)
        ttk.Button(self.root, text="Logout", command=self.login_screen).pack(pady=20)

    def deposit_money(self):
        """Handles Deposits"""
        try:
            amount = float(self.deposit_entry.get())
            self.bank_account.deposit(amount)
            self.update_balance()
            messagebox.showinfo("Success", f"Deposited ${amount} successfully!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def withdraw_money(self):
        """Handles Withdrawals"""
        try:
            amount = float(self.withdraw_entry.get())
            self.bank_account.withdraw(amount)
            self.update_balance()
            messagebox.showinfo("Success", f"Withdrew ${amount} successfully!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def update_balance(self):
        """Updates Balance Label"""
        self.balance_label.config(text=f"Balance: ${self.bank_account.get_balance()}")

    def show_transactions(self):
        """Displays Transaction History"""
        transactions = self.bank_account.get_transactions()
        if not transactions:
            messagebox.showinfo("Transaction History", "No transactions yet!")
            return

        history_window = tk.Toplevel(self.root)
        history_window.title("Transaction History")
        history_window.geometry("400x300")

        ttk.Label(history_window, text="Transaction History", font=("Arial", 14, "bold")).pack(pady=10)

        transaction_list = tk.Listbox(history_window, width=50, height=10)
        transaction_list.pack(pady=5)

        for transaction in transactions:
            transaction_list.insert(tk.END, transaction)


if __name__ == "__main__":
    root = tk.Tk()
    app = BankingApp(root)
    root.mainloop()
