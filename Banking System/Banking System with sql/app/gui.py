import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
from logic import register_user, login_user, deposit, withdraw, get_balance, get_user_data


class BankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MyBank App")
        self.root.geometry("600x450")
        self.root.resizable(False, False)

        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.name = tk.StringVar()
        self.account_number = tk.StringVar()
        self.amount = tk.StringVar()

        self.bg_image = Image.open("1.jpg")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image.resize((600, 450)))
        self.bg_label = tk.Label(root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.build_login()

    def clear_widgets(self):
        for widget in self.root.winfo_children():
            if widget != self.bg_label:
                widget.destroy()

    def styled_label(self, text, size=12, bold=False):
        font = ("Arial", size, "bold" if bold else "normal")
        return tk.Label(self.root, text=text, font=font, bg="#ffffff", fg="#333")

    def styled_entry(self, textvar, show=None):
        return tk.Entry(self.root, textvariable=textvar, font=("Arial", 12), show=show)

    def styled_button(self, text, command):
        return tk.Button(self.root, text=text, command=command,
                         font=("Arial", 12, "bold"), bg="#0066cc", fg="white",
                         activebackground="#0055aa", activeforeground="white", width=20)

    def build_login(self):
        self.clear_widgets()

        self.styled_label("Login to Your Account", 16, bold=True).pack(pady=20)
        self.styled_label("Username").pack()
        self.styled_entry(self.username).pack(pady=5)

        self.styled_label("Password").pack()
        self.styled_entry(self.password, show="*").pack(pady=5)

        self.styled_button("Login", self.login).pack(pady=10)
        self.styled_button("Register", self.build_register).pack()

    def build_register(self):
        self.clear_widgets()
        self.account_number.set(self.generate_account_number())

        self.styled_label("Create New Account", 16, bold=True).pack(pady=15)
        self.styled_label("Full Name").pack()
        self.styled_entry(self.name).pack(pady=3)

        self.styled_label("Account Number (auto)").pack()
        acc_field = self.styled_entry(self.account_number)
        acc_field.pack(pady=3)
        acc_field.config(state="readonly")

        self.styled_label("Username").pack()
        self.styled_entry(self.username).pack(pady=3)

        self.styled_label("Password").pack()
        self.styled_entry(self.password, show="*").pack(pady=3)

        self.styled_button("Submit Registration", self.register).pack(pady=10)
        self.styled_button("Back to Login", self.build_login).pack()

    def build_dashboard(self):
        self.clear_widgets()
        user = get_user_data(self.username.get())

        self.styled_label(f"Welcome, {user['name']}", 16, bold=True).pack(pady=10)
        self.styled_label(f"Account Number: {user['account_number']}", 12).pack(pady=5)

        self.styled_label("Enter Amount").pack(pady=5)
        self.styled_entry(self.amount).pack()

        self.styled_button("Deposit", self.deposit_amount).pack(pady=5)
        self.styled_button("Withdraw", self.withdraw_amount).pack(pady=5)
        self.styled_button("Check Balance", self.check_balance).pack(pady=5)
        self.styled_button("Logout", self.build_login).pack(pady=10)

    def register(self):
        if not all([self.name.get(), self.account_number.get(), self.username.get(), self.password.get()]):
            messagebox.showwarning("Input Error", "All fields required")
            return
        if register_user(self.name.get(), self.account_number.get(), self.username.get(), self.password.get()):
            messagebox.showinfo("Success", "Registered successfully")
            self.build_dashboard()
        else:
            messagebox.showerror("Error", "Username already exists")

    def login(self):
        if login_user(self.username.get(), self.password.get()):
            self.build_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    def deposit_amount(self):
        try:
            amt = float(self.amount.get())
            if amt <= 0:
                raise ValueError
            if deposit(self.username.get(), amt):
                messagebox.showinfo("Success", f"${amt} deposited")
        except ValueError:
            messagebox.showerror("Invalid", "Enter a valid positive number")

    def withdraw_amount(self):
        try:
            amt = float(self.amount.get())
            if amt <= 0:
                raise ValueError
            if withdraw(self.username.get(), amt):
                messagebox.showinfo("Success", f"${amt} withdrawn")
            else:
                messagebox.showerror("Error", "Insufficient balance or invalid user")
        except ValueError:
            messagebox.showerror("Invalid", "Enter a valid positive number")

    def check_balance(self):
        bal = get_balance(self.username.get())
        messagebox.showinfo("Balance", f"Your balance is ${bal:.2f}")

    def generate_account_number(self):
        return str(random.randint(10**9, 10**10 - 1))
