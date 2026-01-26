from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
import json



# ---------------------------- PASSWORD GENERATOR ------------------------------- #



def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]

    password_symbols = [choice(symbols) for char_1 in range(randint(2, 4))]

    password_numbers = [choice(numbers) for char_2 in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")

    #     in entry password entered
    password_entry.insert(0, password)

    #   password copy
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def student_info():
    student_argument = student_name.get()
    email_argument = email_entry.get()
    password_argument = password_entry.get()
    Roll_number_argument=Roll_number_entry.get()
    Subject_argument=Subject_entry.get()
    new_datas={
        student_argument:{
            "email":email_argument,
            "password":password_argument,
            "Roll Number:":Roll_number_argument,
            "Subject_name":Subject_argument
        }
    }

    if len(student_argument)==0 or len(email_argument)==0 or len(password_argument)==0:
        messagebox.showinfo(title="Alert!!", message="You Left Some Credential Entry")
    else:
        is_ok =messagebox.askokcancel(title=student_argument,message=f"Saved Information \n \nEmail: {email_argument}"f"\n \n Password: {password_argument}")

        if is_ok:
            try:
                with open("data.json","r") as filemanger:
                # filemanger.write(f"{website_argument}| {email_argument}|{password_argument} \n")

                # Reading old data
                    data = json.load(filemanger)
            except FileNotFoundError:
                with open("data.json" ,"w") as filemanger:
                # saving updating data
                    json.dump(new_datas, filemanger,indent=4)

            else:
                # updating old data with new data
                data.update(new_datas)
                with open("data.json" ,"w") as filemanger:
                    # saving updating data
                    json.dump(data, filemanger, indent=4)

            finally:
                student_name.delete(0,END)
                password_entry.delete(0,END)
                email_entry.delete(0,END)


def find_password():
    website=student_name.get()
    try:
        with open("data.json") as data_file:
            data=json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="error",message="no data found in file")

    else:
            if website in data:
                email=data[website]["email"]
                password=data[website]["password"]
                messagebox.showinfo(title=website,message=f"Email:{email} \n Password:{password}")
            else:
                messagebox.showinfo(title="Error",message=f"No data found in file {website}.")



# ---------------------------- UI SETUP ------------------------------- #


student_manager = Tk()
student_manager.title("Student Manager ")


student_manager.config(pady=50,padx=50)

# set up the image
canvas=Canvas(width=200,height=200,highlightthickness=0)
image_set=PhotoImage(file="student.png")
canvas.create_image(100,100,image=image_set)
canvas.grid(row=0,column=1)

# website icon setup
student_name=Label(text="Name:")
student_name.grid(row=1,column=0)

student_name=Entry(width=21)
student_name.grid(row=1,column=1)

# website_entry.insert(0,"abc.com")

# email icon setup
Email_name=Label(text="Email/Username:")
Email_name.grid(row=2,column=0)

email_entry=Entry(width=39)
email_entry.grid(row=2,column=1,columnspan=2)


# password icon setup
password_name=Label(text="Password:")
password_name.grid(row=3,column=0)

password_entry=Entry(width=21)
password_entry.grid(row=3,column=1)

Roll_number=Label(text="Roll Number")
Roll_number.grid(row=4,column=0)

Roll_number_entry=Entry(width=39)
Roll_number_entry.grid(row=4,column=1,columnspan=2)

# button work
generate_password_button=Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3,column=2)

Subject_name=Label(text="Department Name:")
Subject_name.grid(row=5,column=0)

Subject_entry=Entry(width=39)
Subject_entry.grid(row=5,column=1,columnspan=2)

add_button=Button(text="Add",width=30,command=student_info)
add_button.grid(row=6,column=1,columnspan=2)

# search button
search_button=Button(text="Search",command=find_password)
search_button.grid(row=1,column=2)

student_manager.mainloop()