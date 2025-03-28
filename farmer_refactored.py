
import turtle
import time

# Global variables for call stack tracking
call_stack = []
execution_step = 0
stack_turtle = None  # Will be initialized in setup()

def setup():
    """Set up the screen and create turtles"""
    screen = turtle.Screen()
    screen.setup(1000, 800)
    screen.title("Farm with Call Stack Visualization")
    screen.bgcolor("white")
    
    # Create main drawing turtle
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    t.pensize(2)
    t.hideturtle()
    
    # Create a dedicated turtle for the call stack visualization
    global stack_turtle
    stack_turtle = turtle.Turtle()
    stack_turtle.speed(0)
    stack_turtle.hideturtle()
    stack_turtle.penup()
    
    # Create a turtle for explanatory text
    text_turtle = turtle.Turtle()
    text_turtle.hideturtle()
    text_turtle.speed(0)
    text_turtle.penup()
    
    # Show title and explanation at the beginning
    text_turtle.goto(0, 300)
    text_turtle.write("Farm with Function Call Visualization", align="center", font=("Arial", 20, "bold"))
    
    text_turtle.goto(-300, 260)
    text_turtle.write("Notice how functions call other functions, building up the call stack.", font=("Arial", 12))
    text_turtle.goto(-300, 240)
    text_turtle.write("The stack visualization on the left shows this process.", font=("Arial", 12))
    
    # Add initial instruction
    text_turtle.goto(0, 200)
    text_turtle.write("Observe the call stack on the left as the farm is drawn...", align="center", font=("Arial", 14, "italic"))
    
    # Draw the call stack container and title - this stays throughout execution
    draw_stack_container()
    
    return t, screen, text_turtle

def draw_stack_container():
    """Draw the container for the call stack visualization"""
    global stack_turtle
    
    stack_x = -450
    stack_y = 300
    
    # Clear any previous drawings
    stack_turtle.clear()
    
    # Draw container outline
    draw_rectangle(stack_turtle, stack_x - 10, stack_y + 60, 140, 350, "#f8f8f8")
    
    # Draw title
    stack_turtle.penup()
    stack_turtle.goto(stack_x + 60, stack_y + 40)
    stack_turtle.write("Call Stack", align="center", font=("Arial", 14, "bold"))
    
    # Draw divider line
    stack_turtle.goto(stack_x - 10, stack_y + 30)
    stack_turtle.pendown()
    stack_turtle.forward(140)
    stack_turtle.penup()

def function_wrapper(func, stack_name, color="#E6FFE6"):
    """A decorator to handle stack visualization and position saving/restoration"""
    def wrapper(t, *args, **kwargs):
        visualize_stack(stack_name, "push", color)
        
        # Save position
        original_pos = t.position()
        original_heading = t.heading()
        
        # Call the original function
        result = func(t, *args, **kwargs)
        
        # Restore position and heading
        t.penup()
        t.goto(original_pos)
        t.setheading(original_heading)
        
        visualize_stack(stack_name, "pop")
        return result
    return wrapper

def draw_rectangle(t, x, y, width, height, fill_color=None):
    """Helper function to draw a rectangle"""
    t.penup()
    t.goto(x, y)
    
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    
    t.pendown()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    
    if fill_color:
        t.end_fill()
    
    t.penup()

def draw_circle(t, x, y, radius, fill_color=None):
    """Helper function to draw a circle"""
    t.penup()
    t.goto(x, y)
    
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    
    t.pendown()
    t.circle(radius)
    
    if fill_color:
        t.end_fill()
    
    t.penup()

def visualize_stack(function_name, action="push", color="lightblue"):
    """Visualize the call stack by drawing rectangles"""
    global call_stack, execution_step, stack_turtle
    
    # Starting position for call stack visualization
    stack_x = -450
    stack_y = 300
    
    if action == "push":
        # Add function to call stack
        call_stack.append((function_name, color))
        execution_step += 1
        
        # Draw new frame without clearing everything
        # Create a new turtle for this frame that will stay around
        frame_turtle = turtle.Turtle()
        frame_turtle.hideturtle()
        frame_turtle.speed(0)
        frame_turtle.penup()
        
        # Calculate position based on how many items are in the stack
        y_pos = stack_y - (len(call_stack) - 1) * 30
        
        # Draw the rectangle
        frame_turtle.goto(stack_x, y_pos)
        frame_turtle.pendown()
        frame_turtle.fillcolor(color)
        frame_turtle.begin_fill()
        for _ in range(2):
            frame_turtle.forward(120)
            frame_turtle.right(90)
            frame_turtle.forward(25)
            frame_turtle.right(90)
        frame_turtle.end_fill()
        
        # Write the function name
        frame_turtle.penup()
        frame_turtle.goto(stack_x + 60, y_pos - 18)
        frame_turtle.write(function_name, align="center", font=("Courier", 10, "normal"))
        
        # Update step counter
        stack_turtle.goto(stack_x, stack_y + 10)
        stack_turtle.write(f"Step: {execution_step}", font=("Arial", 10, "normal"))
        
        # Add a small pause to see the stack change
        time.sleep(0.5)
    
    elif action == "pop":
        # Remove the last function from call stack
        if call_stack:
            call_stack.pop()
            execution_step += 1
            
            # Just update the step counter - the frame itself will be covered by bg color when needed
            stack_turtle.goto(stack_x, stack_y + 10)
            stack_turtle.write(f"Step: {execution_step}", font=("Arial", 10, "normal"))
            
            # Add small pause for visualization
            time.sleep(0.5)

@function_wrapper("draw_barn()", "lightcyan")
def draw_barn(t):
    """Draw a simple barn"""
    # Position barn on the ground
    t.penup()
    t.goto(-300, -150)  # Now on the ground level
    t.pendown()
    
    # Draw barn body
    t.color("darkred")
    draw_rectangle(t, -300, -150, 150, 100, "#C0392B")
    
    # Draw roof
    t.penup()
    t.goto(-300, -50)  # Adjusted for new barn position
    t.pendown()
    t.fillcolor("#7F8C8D")
    t.begin_fill()
    t.goto(-225, 0)  # Peak of roof
    t.goto(-150, -50)
    t.goto(-300, -50)
    t.end_fill()
    
    # Draw door
    draw_rectangle(t, -240, -150, 30, 50, "#784212")
    
    # Draw windows
    draw_rectangle(t, -280, -80, 25, 25, "#F7DC6F")
    draw_rectangle(t, -195, -80, 25, 25, "#F7DC6F")
    
    # Label
    t.penup()
    t.goto(-225, -170)
    t.write("draw_barn()", align="center", font=("Arial", 12, "normal"))

def draw_corn_plant(t, x, y):
    """Draw an individual corn plant"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    # Draw stalk
    t.color("darkgreen")
    t.pensize(3)
    t.setheading(90)  # Point up
    t.forward(70)
    
    # Draw leaves
    t.pensize(2)
    
    # First leaf pair
    t.goto(x, y + 20)
    t.goto(x - 20, y + 5)
    t.goto(x, y + 20)
    t.goto(x + 20, y + 5)
    
    # Second leaf pair
    t.goto(x, y + 40)
    t.goto(x - 15, y + 25)
    t.goto(x, y + 40)
    t.goto(x + 15, y + 25)
    
    t.penup()

def draw_tomato_plant(t, x, y):
    """Draw an individual tomato plant"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    # Draw stem
    t.color("green")
    t.pensize(2)
    t.setheading(90)  # Point up
    t.forward(50)
    
    # Draw leaves
    draw_circle(t, x, y + 40, 10, "green")
    
    # Draw tomatoes
    draw_circle(t, x + 12, y + 30, 8, "#FF6347")
    draw_circle(t, x - 8, y + 25, 8, "#FF6347")

def draw_carrot_plant(t, x, y):
    """Draw an individual carrot plant"""
    t.penup()
    t.goto(x, y)
    
    # Draw carrot top (leaves)
    t.color("darkgreen")
    t.pensize(2)
    
    # First leaves
    t.penup()
    t.goto(x - 10, y - 10)
    t.pendown()
    t.goto(x, y)
    t.goto(x + 10, y - 10)
    
    # Second leaves
    t.penup()
    t.goto(x - 7, y - 5)
    t.pendown()
    t.goto(x, y + 5)
    t.goto(x + 7, y - 5)
    
    # Third leaves
    t.penup()
    t.goto(x - 5, y)
    t.pendown()
    t.goto(x, y + 10)
    t.goto(x + 5, y)
    
    # Draw carrot
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("orange")
    t.pensize(6)
    t.setheading(270)  # Point down
    t.forward(40)
    
    t.penup()

def plant_row(t, plant_func, start_x, start_y, row_name, color):
    """Generic function to plant a row of plants"""
    visualize_stack(row_name, "push", color)
    
    # Save position
    original_pos = t.position()
    original_heading = t.heading()
    
    # Set starting position
    t.penup()
    t.goto(start_x, start_y)
    
    # Draw several plants
    for i in range(3):
        x = start_x + i * 40
        plant_func(t, x, start_y)
    
    # Label
    t.penup()
    t.goto(start_x + 60, start_y - 30)
    t.write(row_name, align="center", font=("Arial", 10, "normal"))
    
    # Return to original position
    t.penup()
    t.goto(original_pos)
    t.setheading(original_heading)
    
    visualize_stack(row_name, "pop")

def plant_corn_row(t, start_x, start_y):
    plant_row(t, draw_corn_plant, start_x, start_y, "plant_corn_row()", "#FFFFCC")

def plant_tomato_row(t, start_x, start_y):
    plant_row(t, draw_tomato_plant, start_x, start_y, "plant_tomato_row()", "#FFE6CC")

def plant_carrot_row(t, start_x, start_y):
    plant_row(t, draw_carrot_plant, start_x, start_y, "plant_carrot_row()", "#E6E6FF")

@function_wrapper("plant_crops()", "#E6FFE6")
def plant_crops(t):
    """Plant all crops in rows"""
    # Plant different crop types in rows - now on ground level
    plant_corn_row(t, 0, -150)
    plant_tomato_row(t, 150, -150)
    plant_carrot_row(t, 300, -150)
    
    # Add a label
    t.penup()
    t.goto(180, -210)
    t.color("black")
    t.write("plant_crops()", align="center", font=("Arial", 14, "bold"))

@function_wrapper("draw_fence()", "#FFE6FF")
def draw_fence(t):
    """Draw a fence around the farm"""
    t.penup()
    t.goto(-400, -150)
    t.pendown()
    
    t.color("saddlebrown")
    t.pensize(3)
    
    # Draw horizontal fence boards
    for y in [0, 30]:
        t.penup()
        t.goto(-400, -150 + y)
        t.pendown()
        t.forward(800)
    
    # Draw vertical posts
    for x in range(-400, 401, 100):
        t.penup()
        t.goto(x, -150)
        t.pendown()
        t.setheading(90)  # Up
        t.forward(40)
    
    # Add a label
    t.penup()
    t.goto(0, -180)
    t.color("black")
    t.write("draw_fence()", align="center", font=("Arial", 12, "normal"))

def draw_farm():
    """Main function to draw the entire farm"""
    t, screen, text_turtle = setup()
    visualize_stack("draw_farm()", "push", "#FFE6E6")
    
    # Clear any previous drawings (but not the explanatory text)
    t.clear()
    
    # Draw sky
    screen.bgcolor("#87CEEB")
    
    # Draw ground
    t.penup()
    t.goto(-500, -150)
    t.pendown()
    t.color("saddlebrown")
    t.fillcolor("#8B4513")
    t.begin_fill()
    for _ in range(2):
        t.forward(1000)
        t.right(90)
        t.forward(250)
        t.right(90)
    t.end_fill()
    
    # Draw components of the farm
    draw_barn(t)
    plant_crops(t)
    draw_fence(t)
    
    visualize_stack("draw_farm()", "pop")
    
    # Final completion message
    text_turtle.clear()  # Clear the initial message
    text_turtle.goto(0, -250)
    text_turtle.write("Drawing Complete!", align="center", font=("Arial", 16, "bold"))
    text_turtle.goto(0, -275)
    text_turtle.write("Click to exit", align="center", font=("Arial", 12))
    
    # Keep the window open
    screen.exitonclick()

# Run the farm drawing - must be at the end of the file
if __name__ == "__main__":
    draw_farm()
