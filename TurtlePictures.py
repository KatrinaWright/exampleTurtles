import turtle
import math

def setup_turtle():
    """Initialize a new turtle with some default settings"""
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    t.pensize(2)
    return t

def clear_screen():
    """Clear the screen and reset all turtles"""
    turtle.clear()
    turtle.resetscreen()

def move_to_position(t, x, y):
    """Move turtle to position without drawing"""
    t.penup()
    t.goto(x, y)
    t.pendown()

def alpha(x, y, start_x=0, start_y=0):
    """Entry point function that routes to different drawings"""
    if x > y:
        return beta(x - y, y, start_x, start_y)  # Routes to stop sign
    elif x < y:
        return gamma(x, y - x, start_x, start_y)  # Routes to house
    else:
        return delta(x, y, start_x, start_y)  # Routes to flower

def beta(a, b, start_x=0, start_y=0):
    """Creates a stop sign"""
    t = setup_turtle()
    move_to_position(t, start_x - a/2, start_y - a/2)  # Center the stop sign
    t.color('red', 'red')
    t.begin_fill()
    
    # Draw octagon
    for _ in range(8):
        t.forward(a)
        t.left(45)
    t.end_fill()
    
    # Write "STOP"
    t.penup()
    t.color('white')
    # Position text more centered
    t.goto(start_x - a/3, start_y - a/6)
    t.write("STOP", font=('Arial', int(a/2), 'bold'))
    t.hideturtle()
    return "What traffic sign did I draw?"

def gamma(p, q, start_x=0, start_y=0):
    """Creates a house"""
    t = setup_turtle()
    size = q  # Base size for the house
    
    # Position at bottom-left of house
    move_to_position(t, start_x - size/2, start_y - size/2)
    
    # Draw square base
    t.color('brown', 'tan')
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()
    
    # Move to start drawing roof
    t.penup()
    t.goto(start_x - size/2, start_y + size/2)
    t.pendown()
    
    # Draw triangle roof
    t.color('red', 'red')
    t.begin_fill()
    t.setheading(0)
    roof_size = size
    for _ in range(3):
        t.forward(roof_size)
        t.left(120)
    t.end_fill()
    
    # Draw door
    t.penup()
    t.goto(start_x - size/6, start_y - size/2)  # Center the door
    t.setheading(90)
    t.color('brown')
    t.begin_fill()
    for _ in range(2):
        t.forward(size/2)
        t.right(90)
        t.forward(size/3)
        t.right(90)
    t.end_fill()
    
    t.hideturtle()
    return "What building did I draw?"

def delta(m, n, start_x=0, start_y=0):
    """Creates a flower"""
    t = setup_turtle()
    move_to_position(t, start_x, start_y)
    t.color('yellow', 'yellow')
    
    # Draw petals
    petal_size = m/4
    for _ in range(12):
        t.begin_fill()
        t.circle(petal_size, 60)
        t.left(120)
        t.circle(petal_size, 60)
        t.left(120)
        t.end_fill()
        t.left(30)
    
    # Draw center
    t.penup()
    t.goto(start_x, start_y-(petal_size/2))  # Return to center
    t.color('brown', 'brown')
    t.begin_fill()
    t.circle(petal_size/2)
    t.end_fill()
    
    t.hideturtle()
    return "What plant did I draw?"

def epsilon(j, k, start_x=0, start_y=0):
    """Creates a spiral"""
    t = setup_turtle()
    move_to_position(t, start_x, start_y)
    t.color('blue')
    
    for i in range(k):
        t.forward(i * 5)  # Reduced multiplier to keep spiral more compact
        t.right(j)
    
    t.hideturtle()
    return "What mathematical pattern did I draw?"

def zeta(r, s, start_x=0, start_y=0):
    """Creates a star"""
    t = setup_turtle()
    move_to_position(t, start_x, start_y - r/2)  # Center the star
    t.color('gold', 'yellow')
    t.begin_fill()
    
    for _ in range(5):
        t.back(r)
        t.right(144)
    
    t.end_fill()
    t.hideturtle()
    return "What celestial object did I draw?"

def main(config="default"):
    """Draw all test images in a circle around the center
    
    Args:
        config (str): Which configuration to use. Either "default" or "alternative"
    """
    # Set up the screen
    screen = turtle.Screen()
    screen.setup(800, 800)  # Set up a larger window
    screen.title("Mystery Turtle Drawings")
    clear_screen()
    
    # Calculate positions in a circle
    center_x, center_y = 0, 0  # Center of the screen
    radius = 200  # Radius of the circle where drawings will be placed
    num_drawings = 5  # Number of test drawings
    
    # Calculate angles for each drawing
    angle_step = 360 / num_drawings
    
    # Create all drawings based on configuration
    if config == "default":
        drawings = [
            (lambda x, y: alpha(100, 50, x, y), "Stop Sign"),
            (lambda x, y: alpha(50, 100, x, y), "House"),
            (lambda x, y: alpha(100, 100, x, y), "Flower"),
            (lambda x, y: epsilon(90, 20, x, y), "Spiral"),
            (lambda x, y: zeta(100, 50, x, y), "Star")
        ]
    else:  # alternative configuration
        drawings = [
            (lambda x, y: alpha(80, 40, x, y), "Stop Sign"),    # Smaller stop sign
            (lambda x, y: zeta(120, 60, x, y), "Star"),         # Larger star
            (lambda x, y: alpha(60, 120, x, y), "House"),       # Taller house
            (lambda x, y: delta(120, 120, x, y), "Flower"),     # Direct flower call
            (lambda x, y: epsilon(45, 30, x, y), "Spiral")      # Different spiral
        ]
    
    # Draw each shape at its position
    for i, (draw_func, name) in enumerate(drawings):
        # Calculate position on the circle
        angle = math.radians(i * angle_step)
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        
        # Draw the shape
        question = draw_func(x, y)
        
        # Add a label
        t = setup_turtle()
        t.penup()
        t.goto(x, y - 80)  # Position label below the drawing
        t.color('black')
        t.write(f"Drawing {i+1}", align="center", font=('Arial', 12, 'normal'))
        t.hideturtle()
    
    # Add title
    t = setup_turtle()
    t.penup()
    t.goto(0, 300)
    t.color('black')
    t.write("Mystery Turtle Drawings", align="center", font=('Arial', 20, 'bold'))
    t.hideturtle()
    
    # Keep the window open
    screen.mainloop()

if __name__ == "__main__":
    main("alternate")