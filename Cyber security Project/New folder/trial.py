import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

# def button_equal():
#     try:
#         expression = entry.get()
#         result = eval(expression)  # Use eval() cautiously in real-world applications!
#         entry.delete(0, tk.END)
#         entry.insert(0, result)
#     except (SyntaxError, NameError, ZeroDivisionError):
#         entry.delete(0, tk.END)
#         entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, padx=40, pady=20, command=lambda text=button_text: button_click(text) if text != '=' else button_equal() if text != 'C' else button_clear())
    button.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

clear_button = tk.Button(root, text="C", padx=40, pady=20, command=button_clear)
clear_button.grid(row=row, column=col)

root.mainloop()