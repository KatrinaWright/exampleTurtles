import turtle

# Set up the Turtle screen
screen = turtle.Screen()
screen.title("Election Result Display")

# Set up the Turtle
pen = turtle.Turtle()
pen.speed(0)  # Fastest speed
pen.hideturtle()  # Hide the turtle cursor

# Define colors for each party
PARTY_COLORS = {
    "Republican": "red",
    "Democratic": "blue",
    "Independent": "green"
}

# Define the total number of electoral votes
TOTAL_ELECTORAL_VOTES = 538

# Initialize variables
remaining_states = ["California", "Texas", "Florida", "New York", "Illinois"]  # Example list of states
votes_drawn = 0
votes_remaining = TOTAL_ELECTORAL_VOTES

def draw_vote(party, x, y):
    """
    Draws a shape representing a vote for the given party at the specified coordinates.
    """
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.fillcolor(PARTY_COLORS[party])
    pen.begin_fill()
    pen.circle(10)  # Adjust the size of the shape as needed
    pen.end_fill()

def drawing_pic(state, party, votes):
    """
    Updates the election result display by drawing votes for the given state and party.
    """
    global votes_drawn, votes_remaining

    # Calculate the starting coordinates for the state's votes
    x_start = (votes_drawn % 20) * 30 - 300  # Adjust the spacing and starting position as needed
    y_start = 200 - (votes_drawn // 20) * 30

    # Draw the votes for the state
    for i in range(votes):
        x = x_start + (i % 20) * 30
        y = y_start - (i // 20) * 30
        draw_vote(party, x, y)
        votes_drawn += 1
        votes_remaining -= 1

    # Remove the state from the remaining states list
    remaining_states.remove(state)

    # Log the remaining states and vote counts
    print(f"Remaining states: {remaining_states}")
    print(f"Votes drawn: {votes_drawn}, Votes remaining: {votes_remaining}")
# Sample function call
drawing_pic("California", "Democratic", 55)
drawing_pic("Texas", "Republican", 38)
drawing_pic("Florida", "Republican", 29)
drawing_pic("New York", "Democratic", 29)
drawing_pic("Illinois", "Democratic", 20)

# Keep the window open until it's manually closed
screen.mainloop()