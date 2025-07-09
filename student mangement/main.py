import pandas as pd
from tkinter import *
from tkinter import ttk


data=pd.read_csv("student.csv")

# Color Configuration
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

# Window Configuration
password_manager = Tk()
password_manager.configure(bg=YELLOW)
password_manager.title("Student Management")
password_manager.config(pady=100,padx=100)

# set up the lock_image
canvas=Canvas(width=200,height=200,highlightthickness=0)
image_set=PhotoImage(file="student.png")
canvas.create_image(100,100,image=image_set)
canvas.grid(row=0,column=1)

# label
label_pop=Label(text="Enter Your Name",font=("Arial", 16, "bold"))
label_pop.grid(row=1,column=0,columnspan=2)

label_pop=Label(text="Select Subject",font=("Arial", 16, "bold"))
label_pop.grid(row=3,column=0,columnspan=2)

# Name  Entry Section

name_entry=Entry(width=35)
name_entry.grid(row=2,column=1,columnspan=2)
# name_entry.insert(0,"Enter Your Name")


states = data.name.to_list()

print(states)

option=[
    "iwt",
    "dsa"
]

# # datatype of menu text
# clicked = StringVar()
#
# # initial menu text
# clicked.set( "Subject" )

drop = ttk.Combobox( password_manager ,textvariable= StringVar() )
drop["values"]=option
drop.grid(row=4,column=1,columnspan=2)

# print(data[hey])

def button_func():
    gather_info = name_entry.get()
    # hey = drop.get()
    if gather_info in states:
        coordinates = data[data.name == gather_info]
        a = coordinates.coa.item()
        print(a)


check_button=Button(text="Check",command=button_func)
check_button.grid(row=5,column=1,columnspan=2)


password_manager.mainloop()


