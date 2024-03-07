import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
game_image = "blank_states_img.gif"
screen.addshape(game_image)

turtle.shape(game_image)

# Import csv data
data = pandas.read_csv("50_states.csv", index_col=False)

# List of all states
all_states = data["state"].to_list()
guessed_state = []


while len(guessed_state) < 50:
    # Get input from the user and convert it to title-cased
    answer_state = screen.textinput(title=f"{len(guessed_state)}/{len(all_states)} State Correct", prompt="What's another state name?").title()

    # If the user enters "Exit"
    if answer_state == "Exit":
        missing_state = []

        # Check which states the user was unable to guess
        for state in all_states:
            if state not in guessed_state:
                # add those unguessed states to the missing_state list
                missing_state.append(state)
    
        # Create a dataframe of the missing states and save to a new file called 'states_to_learn.csv'
        df = pandas.DataFrame(missing_state)
        df.to_csv("states_to_learn.csv")

        # Exit(End) the game loop
        break

    # Check if the state exists
    if (answer_state in all_states) and (answer_state not in guessed_state):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == f"{answer_state}"]
        state_x_cor = int(state_data.x.to_string(index=False))
        state_y_cor = int(state_data.y.to_string(index=False))

        # Move state to it's necessary cordinates
        t.goto(state_x_cor, state_y_cor)
        t.write(answer_state)

        # Add user guessed (right) answers to the guessed_state list
        guessed_state.append(answer_state)










# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# screen.exitonclick()
