from tkinter import *

Calc=Tk()
Calc.title("Calculator")
Calc.minsize(400,500)

# entry_point=Entry(width=80,)
Calc.config(padx=20,pady=20)
# entry_point.grid()

# def calc_button():
    # Calc.config(entry_point.get())

# button =Button(text="9")
# button.grid(column=0,row=0)
button = Button(text="Button-1", height=3, width=10)
button.grid(column=0,row=0)

button=Button(text="Button-2", height=3, width=10)
button.grid(column=1,row=0)



Calc.mainloop()