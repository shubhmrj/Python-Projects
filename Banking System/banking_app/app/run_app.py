import tkinter as tk
from gui import BankApp
from db import init_db
init_db()

if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()
