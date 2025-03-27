from tkinter import *
import requests

def get_quote():
    response=requests.get("https://api.kanye.rest/")
    data = response.json()
    # print(response)
    # a=data["quote"]
    canvas.itemconfig(quote_text,text=data["quote"])



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="xyz", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)
canvas.itemconfig(quote_text,text=get_quote())

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()