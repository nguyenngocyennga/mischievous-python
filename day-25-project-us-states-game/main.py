import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
all_states = states_data.state.to_list()
guessed_states = []
# print(states_data)


def write_state(state_name, state_xcor, state_ycor):
    new_turtle = turtle.Turtle()
    new_turtle.hideturtle()
    new_turtle.penup()
    new_turtle.goto(state_xcor, state_ycor)
    new_turtle.write(state_name, align="center", font=("courier", 11, "normal"))


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        # states_to_learn = []
        # for i in all_states:
        #     if i not in guessed_states:
        #         states_to_learn.append(i)
        # new_data = pandas.DataFrame(states_to_learn)
        # new_data.to_csv("states_to_learn.csv")
        # break
        states_to_learn = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_choice = states_data[states_data.state == answer_state]
        write_state(str(state_choice.state.item()), int(state_choice.x), int(state_choice.y))
