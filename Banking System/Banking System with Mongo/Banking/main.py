import tkinter as tk
from tkinter import messagebox
from Banking import BankAccount


class BankingApp:
    def __init__(self, root):
        self.bank_account = BankAccount("John Doe", 1000)

        self.root = root
        self.root.title("Banking Application")
        self.root.config(padx=50,pady=50)

        self.balance_label1 = tk.Label(root, text="Account Name: Shubham Raj",fg="red")
        self.balance_label1.grid(row=0, column=0)

        self.balance_label1 = tk.Label(root, text="Account Number: 968520452562",fg="red")
        self.balance_label1.grid(row=1, column=0)


        self.balance_label2 = tk.Label(root, text="")
        self.balance_label2.grid(row=2, column=0)

        self.balance_label = tk.Label(root, text=f"Balance: ${self.bank_account.get_balance()}")
        self.balance_label.grid(row=3,column=0)

        self.deposit_entry = tk.Entry(root)
        self.deposit_entry.grid(row=4, column=0)

        self.deposit_button = tk.Button(root, text="Deposit", command=self.deposit)
        self.deposit_button.grid(row=4,column=1)

        self.balance_label3 = tk.Label(root, text="")
        self.balance_label3.grid(row=5, column=0)

        self.withdraw_entry = tk.Entry(root)
        self.withdraw_entry.grid(row=6,column=0)

        self.withdraw_button = tk.Button(root, text="Withdraw", command=self.withdraw)
        self.withdraw_button.grid(row=7,column=0)

    def deposit(self):
        amount = self.deposit_entry.get()
        try:
            amount = float(amount)
            self.bank_account.deposit(amount)
            self.balance_label.config(text=f"Balance: ${self.bank_account.get_balance()}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def withdraw(self):
        amount = self.withdraw_entry.get()
        try:
            amount = float(amount)
            self.bank_account.withdraw(amount)
            self.balance_label.config(text=f"Balance: ${self.bank_account.get_balance()}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = BankingApp(root)
    root.mainloop()
