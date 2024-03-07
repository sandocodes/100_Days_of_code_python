import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
game_image = "blank_states_img.gif"
screen.addshape(game_image)


turtle.shape(game_image)

data = pandas.read_csv("50_states.csv", index_col=False)
# print(data)

# list of states
all_states = data["state"].to_list()
guessed_state = []


while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/{len(all_states)} State Correct", prompt="What's another state name?").title()

    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_state:
                missing_state.append(state)
    
        states_to_learn = {
            "state": missing_state,
        }

        df = pandas.DataFrame(states_to_learn)
        df.to_csv("states_to_learn.csv")
        
        break

    # Check if the state exists
    if (answer_state in all_states) and (answer_state not in guessed_state):
        # Create a turtle and make it goto the x and y coordinates
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == f"{answer_state}"]
        state_x = int(state_data.x.to_string(index=False))
        state_y = int(state_data.y.to_string(index=False))

        t.goto(state_x, state_y)
        t.write(answer_state)

        guessed_state.append(answer_state)

    elif answer_state in guessed_state:
        print(f"You already guessed this {answer_state}")









# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# screen.exitonclick()
