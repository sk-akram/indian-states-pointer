import turtle
import pandas

screen = turtle.Screen()
turtle.bgpic("india-outline-map.png")
turtle.screensize(500, 589)
screen.title("Indian States Game")


data = pandas.read_csv("indian_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 32:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/32 States Correct",
                                    prompt="What's another state's name?").title()
    
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.dot(5, "black")
        t.write(answer_state, font=("Arial", 8, "bold"))
