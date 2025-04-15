import turtle

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

# Main recursive functions that determine the path
def alpha(x, y, start_x=0, start_y=0):
    """Initial decision point: Choose between different paths based on x and y values"""
    if x > y:
        return beta(x - y, y, start_x, start_y)
    elif x < y:
        return gamma(x, y - x, start_x, start_y)
    else:
        return delta(x, y, start_x, start_y)

def beta(a, b, start_x=0, start_y=0):
    """Second level decision: Choose between night scene or spiral"""
    if a % 2 == 0:
        return epsilon(a // 2, b, start_x, start_y)  # Draw spiral
    else:
        return zeta(a, b * 2, start_x, start_y)  # Draw night scene

def gamma(p, q, start_x=0, start_y=0):
    """House path decisions"""
    if p < 10:
        return draw_house_with_garden(p + q, q, start_x, start_y)
    else:
        return draw_house_with_sun(p, q + 5, start_x, start_y)

def delta(m, n, start_x=0, start_y=0):
    """Flower garden decision path"""
    return draw_flower_garden(m + n, start_x, start_y)

def epsilon(j, k, start_x=0, start_y=0):
    """Spiral art decision path"""
    if j < k:
        return draw_spiral(j * 2, k, start_x, start_y)
    else:
        return draw_double_spiral(j, k * 2, start_x, start_y)

def zeta(r, s, start_x=0, start_y=0):
    """Night scene decision path"""
    return draw_night_scene(r + s, s - r, start_x, start_y)

# Drawing functions
def draw_house_base(t, size, x, y):
    """Helper function to draw basic house structure"""
    move_to_position(t, x - size/2, y - size/2)
    t.color('brown', 'tan')
    t.setheading(0)  # Set heading to 0 (east) before drawing
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()
    
    # Draw roof
    t.penup()
    t.goto(x - size/2, y + size/2)
    t.pendown()
    t.color('red', 'red')
    t.begin_fill()
    t.setheading(0)
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()
    
    # Draw door
    t.penup()
    t.goto(x - size/6, y - size/2)
    t.setheading(90)
    t.color('brown')
    t.begin_fill()
    for _ in range(2):
        t.forward(size/2)
        t.right(90)
        t.forward(size/3)
        t.right(90)
    t.end_fill()

def draw_house_with_garden(p, q, start_x=0, start_y=0):
    """Draw house with a garden"""
    t = setup_turtle()
    size = q * 5  # Scale the house size
    
    # Draw house
    draw_house_base(t, size, start_x, start_y)
    
    # Draw flowers in garden
    garden_start_x = start_x - size/2
    garden_start_y = start_y - size/2
    flower_spacing = size/4
    
    for i in range(3):
        draw_small_flower(t, garden_start_x + (i+1)*flower_spacing, garden_start_y - 20)
    
    t.hideturtle()
    return "house_with_garden"

def draw_house_with_sun(p, q, start_x=0, start_y=0):
    """Draw house with sun"""
    t = setup_turtle()
    size = q * 5
    
    # Draw sun
    t.penup()
    t.goto(start_x + size, start_y + size)
    t.color('yellow', 'yellow')
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    
    # Draw rays
    for _ in range(12):
        t.penup()
        t.goto(start_x + size, start_y + size)
        t.setheading(_ * 30)
        t.pendown()
        t.forward(40)
    
    # Draw house
    draw_house_base(t, size, start_x, start_y)
    
    t.hideturtle()
    return "house_with_sun"

def draw_small_flower(t, x, y):
    """Helper function to draw a small flower"""
    move_to_position(t, x, y)
    t.color('yellow', 'yellow')
    
    # Draw petals
    for _ in range(6):
        t.begin_fill()
        t.circle(10, 60)
        t.left(120)
        t.circle(10, 60)
        t.left(120)
        t.end_fill()
        t.left(60)

def draw_flower_garden(size, start_x=0, start_y=0):
    """Draw a garden full of flowers"""
    t = setup_turtle()
    
    # Draw multiple flowers in a pattern
    positions = [
        (0, 0), (-50, 50), (50, 50),
        (-50, -50), (50, -50)
    ]
    
    for pos_x, pos_y in positions:
        move_to_position(t, start_x + pos_x, start_y + pos_y)
        t.color('yellow', 'yellow')
        
        # Draw petals
        for _ in range(12):
            t.begin_fill()
            t.circle(20, 60)
            t.left(120)
            t.circle(20, 60)
            t.left(120)
            t.end_fill()
            t.left(30)
        
        # Draw center
        t.penup()
        t.goto(start_x + pos_x, start_y + pos_y - 10)
        t.color('brown', 'brown')
        t.begin_fill()
        t.circle(10)
        t.end_fill()
    
    t.hideturtle()
    return "flower_garden"

def draw_spiral(j, k, start_x=0, start_y=0):
    """Draw a spiral pattern"""
    t = setup_turtle()
    move_to_position(t, start_x, start_y)
    t.color('blue')
    
    # Using smaller increments for a smoother spiral
    for i in range(k * 4):  # More iterations for a fuller spiral
        t.forward(2 + (i * 0.5))  # Smaller initial size and gentler growth
        t.right(20)  # Constant angle for a more regular spiral
    
    t.hideturtle()
    return "spiral"

def draw_double_spiral(j, k, start_x=0, start_y=0):
    """Draw a double spiral pattern"""
    t = setup_turtle()
    move_to_position(t, start_x, start_y)
    
    colors = ['blue', 'purple']
    for color in colors:
        t.color(color)
        for i in range(k):
            t.forward(i * 3)
            t.right(j/2)
        move_to_position(t, start_x, start_y)
        t.setheading(180)  # Start second spiral in opposite direction
    
    t.hideturtle()
    return "double_spiral"

def draw_night_scene(r, s, start_x=0, start_y=0):
    """Draw a night scene with stars and moon"""
    t = setup_turtle()
    
    # Draw night sky background
    t.color('navy', 'navy')
    move_to_position(t, start_x - 100, start_y - 100)
    t.begin_fill()
    for _ in range(4):
        t.forward(200)
        t.left(90)
    t.end_fill()
    
    # Draw moon
    t.color('white', 'white')
    move_to_position(t, start_x + 50, start_y + 50)
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    
    # Draw stars
    t.color('white')
    for _ in range(10):
        x = start_x + (_ * 20 - 100)
        y = start_y + ((_ * 17) % 150 - 75)
        move_to_position(t, x, y)
        t.begin_fill()
        for _ in range(5):
            t.forward(10)
            t.right(144)
        t.end_fill()
    
    t.hideturtle()
    return "night_scene"

def main():
    """Test different paths through the recursive art generator"""
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.title("Recursive Art Generator")
    
    # Test cases that lead to different outcomes
    test_cases = [
        ((10, 25), "Path 1: House with Sun"),      # Ensures p >= 10 in gamma
        ((8, 12), "Path 2: House with Garden"),     # p < 10 in gamma
        ((20, 20), "Path 3: Flower Garden"),        # Equal values go to delta
        ((25, 10), "Path 4: Night Scene"),         # Odd difference for night scene
        ((31, 15), "Path 5: Spiral") ]              # Even difference for spiral
    
    for i, ((x, y), description) in enumerate(test_cases):
        clear_screen()
        result = alpha(x, y)
        print(f"\nTest {i+1}: {description}")
        print(f"Input: x={x}, y={y}")
        print(f"Result: {result}")
        input("Press Enter to continue to next test...")

if __name__ == "__main__":
    main()