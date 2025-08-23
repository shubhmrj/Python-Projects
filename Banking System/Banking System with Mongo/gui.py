import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from user_auth import authenticate, signup
from banking import BankAccount, load_users

class BankingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Banking System with sql")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        self.current_user = None
        self.bank_account = None

        self.load_background()
        self.login_screen()

    def load_background(self):
        self.bg_image = Image.open("1.jpg")
        self.bg_image = self.bg_image.resize((600, 500), Image.LANCZOS)
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

        login_frame = tk.Frame(self.root, bg="white", padx=20, pady=20)
        login_frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(login_frame, text="User ID:", background="white").grid(row=1, column=0, pady=5, sticky="e")
        self.user_id_entry = ttk.Entry(login_frame)
        self.user_id_entry.grid(row=1, column=1, pady=5)

        ttk.Label(login_frame, text="Password:", background="white").grid(row=2, column=0, pady=5, sticky="e")
        self.password_entry = ttk.Entry(login_frame, show="*")
        self.password_entry.grid(row=2, column=1, pady=5)

        ttk.Button(login_frame, text="Login", command=self.authenticate_user).grid(row=3, column=1, pady=5)
        ttk.Button(login_frame, text="Sign Up", command=self.signup_screen).grid(row=4, column=1, pady=5)

    def authenticate_user(self):
        user_id = self.user_id_entry.get()
        password = self.password_entry.get()

        user_data = authenticate(user_id, password)
        if user_data:
            self.current_user = user_data["username"]
            self.bank_account = BankAccount({"user_id": user_id, **user_data})
            messagebox.showinfo("Login Successful", f"Welcome, {self.current_user}!")
        else:
            messagebox.showerror("Login Failed", "Invalid User ID or Password")

    def signup_screen(self):
        self.clear_screen()

        signup_frame = tk.Frame(self.root, bg="white", padx=20, pady=20)
        signup_frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(signup_frame, text="Username:", background="white").grid(row=1, column=0, pady=5, sticky="e")
        self.signup_username = ttk.Entry(signup_frame)
        self.signup_username.grid(row=1, column=1, pady=5)

        ttk.Label(signup_frame, text="Password:", background="white").grid(row=2, column=0, pady=5, sticky="e")
        self.signup_password = ttk.Entry(signup_frame, show="*")
        self.signup_password.grid(row=2, column=1, pady=5)

        ttk.Label(signup_frame, text="Account Type:", background="white").grid(row=3, column=0, pady=5, sticky="e")
        self.account_type = ttk.Combobox(signup_frame, values=["Savings", "Checking"])
        self.account_type.grid(row=3, column=1, pady=5)
        self.account_type.current(0)

        ttk.Button(signup_frame, text="Register", command=self.register_user).grid(row=4, column=1, pady=10)
