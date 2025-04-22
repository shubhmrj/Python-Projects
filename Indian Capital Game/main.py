import turtle
import pandas

data= pandas.read_csv("indian_capital.csv")
screen=turtle.Screen()
its = turtle.Turtle()
screen.title("Indian States Guess")
screen.addshape("Indian Map.gif")
turtle.shape("Indian Map.gif")

# Here generate X and y coordinate in map of each state

# def get_x_y(x, y):
#     state_name=screen.textinput(title="state_name", prompt="enter")
#     print(state_name)
#     print(x, y)
#
# screen.onscreenclick(get_x_y)
# turtle.mainloop()

guessed_state_list ={}

while len(guessed_state_list)<31:
    guess_states= (screen.textinput(title=f"{len(guessed_state_list)} |50 States Correct", prompt="Guess Indian States")
                   .title())

    states= data.States.to_list()

    if guess_states == "Exit":
        not_guess_state = []
        for i in states:
            if i not in guessed_state_list:
                not_guess_state.append(i)
        data = pandas.DataFrame(not_guess_state)
        data.to_csv('which you not answered.csv')
        break

    elif guess_states in states:

        if guess_states not in guessed_state_list:
            guessed_state_list.append(guess_states)
            its = turtle.Turtle()
            its.hideturtle()
            its.penup()
            coordinates=data[data.States==guess_states]
            its.goto(coordinates.x.item(), coordinates.y.item())
            its.write(guess_states)


screen .exitonclick()