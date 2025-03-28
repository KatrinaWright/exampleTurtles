import turtle
import time

# Global variables for call stack tracking
call_stack = []
execution_history = []
execution_step = 0
history_start_index = 0  # Index to start displaying history entries
stack_turtle = None
history_turtle = None
current_stack_turtle = None

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
    
    # Create turtles for the call stack visualization
    global stack_turtle, history_turtle, current_stack_turtle
    
    # Turtle for drawing static container elements
    stack_turtle = turtle.Turtle()
    stack_turtle.speed(0)
    stack_turtle.hideturtle()
    stack_turtle.penup()
    
    # Turtle for drawing history entries
    history_turtle = turtle.Turtle()
    history_turtle.speed(0)
    history_turtle.hideturtle()
    history_turtle.penup()
    
    # Turtle for drawing current stack entries
    current_stack_turtle = turtle.Turtle()
    current_stack_turtle.speed(0)
    current_stack_turtle.hideturtle()
    current_stack_turtle.penup()
    
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
    text_turtle.write("The stack visualization on the right shows this process.", font=("Arial", 12))
    
    # Add initial instruction
    text_turtle.goto(0, 200)
    text_turtle.write("Observe the call stack on the right as the farm is drawn...", align="center", font=("Arial", 14, "italic"))
    
    # Draw the call stack container and title - this stays throughout execution
    draw_stack_container()
    
    return t, screen, text_turtle

def draw_stack_container():
    """Draw the container for the call stack visualization"""
    global stack_turtle
    
    # Position the stack display on the right side to avoid the barn
    stack_x = 350
    stack_y = 300
    
    # Clear any previous drawings
    stack_turtle.clear()
    
    # Draw container outline
    stack_turtle.penup()
    stack_turtle.goto(stack_x - 10, stack_y + 60)
    stack_turtle.pendown()
    stack_turtle.fillcolor("#f8f8f8")
    stack_turtle.begin_fill()
    for _ in range(2):
        stack_turtle.forward(220)
        stack_turtle.right(90)
        stack_turtle.forward(550)  # Make it taller to accommodate more entries
        stack_turtle.right(90)
    stack_turtle.end_fill()
    
    # Draw title
    stack_turtle.penup()
    stack_turtle.goto(stack_x + 100, stack_y + 40)
    stack_turtle.write("Call Stack & Execution History", align="center", font=("Arial", 14, "bold"))
    
    # Draw divider line
    stack_turtle.goto(stack_x - 10, stack_y + 30)
    stack_turtle.pendown()
    stack_turtle.forward(220)
    stack_turtle.penup()
    
    # Draw current stack label
    stack_turtle.goto(stack_x + 10, stack_y + 10)
    stack_turtle.write("Current Stack:", font=("Arial", 12, "bold"))
    
    # Draw execution history label
    stack_turtle.goto(stack_x + 10, stack_y - 100)
    stack_turtle.write("Execution History:", font=("Arial", 12, "bold"))

def draw_current_stack():
    """Draw the current call stack with indentation"""
    global current_stack_turtle, call_stack
    
    # Position for stack visualization
    stack_x = 350
    stack_y = 300
    
    # Clear previous stack entries
    current_stack_turtle.clear()
    
    # Draw the current call stack with indentation
    for i, (func, color) in enumerate(call_stack):
        # Draw bullet
        current_stack_turtle.penup()
        current_stack_turtle.goto(stack_x + 20 + (i * 15), stack_y - 20 - (i * 20))
        current_stack_turtle.dot(8, color)
        
        # Draw function name
        current_stack_turtle.goto(stack_x + 30 + (i * 15), stack_y - 23 - (i * 20))
        current_stack_turtle.color("black")
        current_stack_turtle.write(func, font=("Courier", 10, "normal"))

def draw_history():
    """Draw the execution history"""
    global history_turtle, execution_history, history_start_index
    
    # Position for history visualization
    stack_x = 350
    stack_y = 300
    
    # Clear previous history entries
    history_turtle.clear()
    
    # Determine how many entries can fit in the visible area
    max_visible_entries = 15
    available_entries = len(execution_history) - history_start_index
    entries_to_draw = min(max_visible_entries, available_entries)
    
    # Draw each history entry
    for i in range(entries_to_draw):
        idx = history_start_index + i
        step, action_type, func, level = execution_history[idx]
        
        y_offset = stack_y - 150 - (i * 20)
        
        # Draw step number
        history_turtle.penup()
        history_turtle.goto(stack_x + 10, y_offset)
        history_turtle.color("black")
        history_turtle.write(f"{step:3}.", font=("Courier", 9, "normal"))
        
        # Draw indentation based on level
        indentation = " " * (level * 2)
        
        # Draw different symbols for enter vs exit
        if action_type == "Enter":
            symbol = "→"
            history_turtle.color("blue")
        else:  # Exit
            symbol = "←"
            history_turtle.color("red")
            
        # Write the execution history entry
        history_turtle.goto(stack_x + 40, y_offset)
        history_turtle.write(f"{symbol} {indentation}{func}", font=("Courier", 9, "normal"))

def visualize_stack(function_name, action="push", color="lightblue"):
    """Update the call stack and history visualizations"""
    global call_stack, execution_history, execution_step, history_start_index
    
    # Increment step counter regardless of action
    execution_step += 1
    
    if action == "push":
        # Add function to call stack
        call_stack.append((function_name, color))
        
        # Add to execution history
        execution_history.append((execution_step, "Enter", function_name, len(call_stack) - 1))
    
    elif action == "pop":
        # Add to execution history before popping
        if call_stack:
            func_to_pop = call_stack[-1][0]
            execution_history.append((execution_step, "Exit", func_to_pop, len(call_stack) - 1))
            
            # Remove the function from call stack
            call_stack.pop()
    
    # Update stack visualization
    draw_current_stack()
    
    # Check if we need to scroll history (if we've reached max visible entries)
    max_visible_entries = 15
    if len(execution_history) - history_start_index > max_visible_entries:
        history_start_index = len(execution_history) - max_visible_entries
    
    # Update history visualization
    draw_history()
    
    # Add a small pause to see the stack change
    time.sleep(0.3)

def draw_with_label(t, draw_func, label_text):
    """Draw an element and add a label above it"""
    # Save original position and heading
    original_pos = t.position()
    original_heading = t.heading()
    
    # Draw the element
    draw_func(t)
    
    # Return to original position
    t.penup()
    t.goto(original_pos)
    t.setheading(original_heading)

def draw_barn_element(t):
    """Draw a simple barn"""
    visualize_stack("draw_barn()", "push", "lightcyan")
    
    # Position barn on the ground
    t.penup()
    t.goto(-300, -150)
    
    # Add label above
    label_pos = t.position()
    t.goto(label_pos[0] + 75, label_pos[1] + 120)
    t.write("draw_barn()", align="center", font=("Arial", 12, "normal"))
    
    # Back to position for drawing
    t.goto(-300, -150)
    t.pendown()
    
    # Draw barn body
    t.color("darkred")
    t.fillcolor("#C0392B")
    t.begin_fill()
    for _ in range(2):
        t.forward(150)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.end_fill()
    
    # Draw roof
    t.penup()
    t.goto(-300, -50)
    t.pendown()
    t.fillcolor("#7F8C8D")
    t.begin_fill()
    t.goto(-225, 0)  # Peak of roof
    t.goto(-150, -50)
    t.goto(-300, -50)
    t.end_fill()
    
    # Draw door
    t.penup()
    t.goto(-240, -150)
    t.pendown()
    t.fillcolor("#784212")
    t.begin_fill()
    for _ in range(2):
        t.forward(30)
        t.left(90)
        t.forward(50)
        t.left(90)
    t.end_fill()
    
    # Draw windows
    t.penup()
    t.goto(-280, -80)
    t.pendown()
    t.fillcolor("#F7DC6F")
    t.begin_fill()
    for _ in range(4):
        t.forward(25)
        t.left(90)
    t.end_fill()
    
    t.penup()
    t.goto(-195, -80)
    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.forward(25)
        t.left(90)
    t.end_fill()
    
    visualize_stack("draw_barn()", "pop")

def draw_plant(t, x, y, plant_type):
    """Draw a plant based on its type"""
    if plant_type == "corn":
        draw_corn_plant(t, x, y)
    elif plant_type == "tomato":
        draw_tomato_plant(t, x, y)
    elif plant_type == "carrot":
        draw_carrot_plant(t, x, y)

def plant_row(t, start_x, start_y, plant_type):
    """Draw a row of plants of the specified type"""
    func_name = f"plant_{plant_type}_row()"
    
    visualize_stack(func_name, "push", 
                    "#FFFFCC" if plant_type == "corn" else 
                    "#FFE6CC" if plant_type == "tomato" else "#E6E6FF")
    
    # Position for row
    t.penup()
    t.goto(start_x, start_y)
    
    # Add label above
    label_pos = t.position()
    t.goto(label_pos[0] + 60, label_pos[1] + 50)
    t.write(func_name, align="center", font=("Arial", 10, "normal"))
    
    # Draw plants in a row
    for i in range(3):
        x = start_x + i * 40
        draw_plant(t, x, start_y, plant_type)
    
    visualize_stack(func_name, "pop")

def draw_corn_plant(t, x, y):
    """Draw an individual corn plant"""
    visualize_stack("draw_corn_plant()", "push", "#FFFFAA")
    
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
    
    visualize_stack("draw_corn_plant()", "pop")

def draw_tomato_plant(t, x, y):
    """Draw an individual tomato plant"""
    visualize_stack("draw_tomato_plant()", "push", "#FFCCAA")
    
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    # Draw stem
    t.color("green")
    t.pensize(2)
    t.setheading(90)
    t.forward(50)
    
    # Draw leaves
    t.penup()
    t.goto(x, y + 40)
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    
    # Draw tomatoes
    t.penup()
    t.goto(x + 12, y + 30)
    t.pendown()
    t.fillcolor("#FF6347")
    t.begin_fill()
    t.circle(8)
    t.end_fill()
    
    t.penup()
    t.goto(x - 8, y + 25)
    t.pendown()
    t.begin_fill()
    t.circle(8)
    t.end_fill()
    
    t.penup()
    
    visualize_stack("draw_tomato_plant()", "pop")

def draw_carrot_plant(t, x, y):
    """Draw an individual carrot plant"""
    visualize_stack("draw_carrot_plant()", "push", "#CCCCFF")
    
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
    t.setheading(270)
    t.forward(40)
    
    t.penup()
    
    visualize_stack("draw_carrot_plant()", "pop")

def plant_crops(t):
    """Plant all crops in rows"""
    visualize_stack("plant_crops()", "push", "#E6FFE6")
    
    # Add label at the top
    t.penup()
    t.goto(180, -90)
    t.color("black")
    t.write("plant_crops()", align="center", font=("Arial", 14, "bold"))
    
    # Plant different crop types in rows
    plant_row(t, 0, -150, "corn")
    plant_row(t, 150, -150, "tomato")
    plant_row(t, 300, -150, "carrot")
    
    visualize_stack("plant_crops()", "pop")

def draw_fence(t):
    """Draw a fence around the farm"""
    visualize_stack("draw_fence()", "push", "#FFE6FF")
    
    # Add label at the top
    t.penup()
    t.goto(0, -110)
    t.color("black")
    t.write("draw_fence()", align="center", font=("Arial", 12, "normal"))
    
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
        t.setheading(90)
        t.forward(40)
    
    visualize_stack("draw_fence()", "pop")

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
    draw_barn_element(t)
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

# Run the farm drawing
if __name__ == "__main__":
    draw_farm()