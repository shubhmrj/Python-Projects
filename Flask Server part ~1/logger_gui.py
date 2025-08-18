import tkinter as tk
from tkinter import scrolledtext, messagebox
from PIL import Image, ImageTk
import threading

class LoggerSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(LoggerSingleton, cls).__new__(cls)
                cls._instance.logs = []
            return cls._instance

    def log(self, message):
        self.logs.append(message)

    def get_logs(self):
        return self.logs

class LoggerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Unique Logger System")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        # Load and set background image
        try:
            self.bg_image = Image.open("background.jpg")
            self.bg_image = self.bg_image.resize((700, 500), Image.ANTIALIAS)
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)
            self.bg_label = tk.Label(root, image=self.bg_photo)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            messagebox.showwarning("Background Image", f"Could not load background.jpg: {e}")

        # Unique interface styling
        self.frame = tk.Frame(root, bg='#2d2d44', bd=4, relief=tk.RIDGE)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=480, height=340)

        self.title_label = tk.Label(self.frame, text="Logger System", font=("Segoe Script", 20, "bold"), fg="#ffb347", bg="#2d2d44")
        self.title_label.pack(pady=(15, 5))

        self.log_entry = tk.Entry(self.frame, font=("Segoe UI", 12), width=35, bg="#f4e2d8")
        self.log_entry.pack(pady=10)

        self.log_button = tk.Button(self.frame, text="Add Log", font=("Segoe UI", 11, "bold"), bg="#5f4b8b", fg="white", command=self.add_log)
        self.log_button.pack(pady=5)

        self.logs_display = scrolledtext.ScrolledText(self.frame, font=("Consolas", 11), width=50, height=10, bg="#f4e2d8", fg="#2d2d44", wrap=tk.WORD)
        self.logs_display.pack(pady=10)
        self.logs_display.config(state=tk.DISABLED)

        self.refresh_button = tk.Button(self.frame, text="Refresh Logs", font=("Segoe UI", 10, "bold"), bg="#ffb347", fg="#2d2d44", command=self.refresh_logs)
        self.refresh_button.pack(pady=5)

        self.logger = LoggerSingleton()

    def add_log(self):
        message = self.log_entry.get().strip()
        if message:
            self.logger.log(message)
            self.log_entry.delete(0, tk.END)
            self.refresh_logs()
        else:
            messagebox.showinfo("Input Needed", "Please enter a log message.")

    def refresh_logs(self):
        self.logs_display.config(state=tk.NORMAL)
        self.logs_display.delete(1.0, tk.END)
        for idx, log in enumerate(self.logger.get_logs(), 1):
            self.logs_display.insert(tk.END, f"{idx}. {log}\n")
        self.logs_display.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = LoggerGUI(root)
    root.mainloop()
