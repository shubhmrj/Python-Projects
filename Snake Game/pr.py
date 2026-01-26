import turtle
screen = turtle.Screen()

a= screen.textinput(title="Enter Your Name ", prompt="Name")
print(f'{a}')
with open("HIGHSCORE.TXT" , mode="a") as file:
    file.write("\n new place.")