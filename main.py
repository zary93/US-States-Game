import turtle
import pandas


def correct_answer(title):
    if title in data["state"].values:
        global score
        score += 1
        state_row = data.loc[data["state"] == title]
        x_coord = state_row.iloc[0]["x"]
        y_coord = state_row.iloc[0]["y"]
        tim = turtle.Turtle()
        tim.penup()
        tim.hideturtle()
        tim.goto(x=x_coord, y=y_coord)
        tim.write(f"{title}")


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("./50_states.csv")
state_list = data.state.to_list()
score = 0
while score < 50:
    state = screen.textinput(title=f"{score}/50 Guess the State", prompt="What's another state's name?")
    state_title = state.title()
    if state_title == "Exit":
        state_list2 = [states for states in state_list if state_title != states]
        new_data = pandas.DataFrame(state_list2)
        new_data.to_csv("LIst of State2.csv")
        break
    else:
        correct_answer(state_title)
