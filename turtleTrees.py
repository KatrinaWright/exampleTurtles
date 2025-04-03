import turtle

def triangle(size, color):
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.begin_fill()
  for i in range(3):
    turtle.forward(size)
    turtle.left(120)
  turtle.end_fill()
    
    
def up(distance):
  turtle.penup()
  turtle.left(90)
  turtle.forward(distance)
  turtle.right(90)
  turtle.forward(distance/4)
  turtle.pendown()
  
def stump(size, color):
  turtle.penup()
  turtle.forward(size*(5/8))
  turtle.pendown()
  turtle.color("brown")
  turtle.fillcolor("brown")
  turtle.begin_fill()
  for i in range(4):
    turtle.right(90)
    turtle.forward(size/4)
  turtle.end_fill()
  turtle.color(color)
  turtle.back(size*(5/8))
  
def tree(size, color):
  stump(size, color)
  for i in range(size, 20, -10):
    triangle(i, color)
    up(20)
  
  # triangle(50, color)
  # up(20)
  # triangle(40, color)
  # up(20)
  # triangle(30, color)
  # up(20)

# Clear the screen and set starting position
turtle.clear()
turtle.penup()
turtle.goto(-300, -200)  # Start from the left-bottom
turtle.pendown()

# Spring: Light green trees
for i in range(3):
    tree(50 + i * 10, "lightgreen")
    turtle.penup()
    turtle.forward(75)
    turtle.pendown()

# Summer: Dark green trees
for i in range(3):
    tree(50 + i * 10, "darkgreen")
    turtle.penup()
    turtle.forward(75)
    turtle.pendown()

# Fall: Orange and red trees
for i in range(3):
    tree(50 + i * 10, ["orange", "red"][i % 2])  # Alternate colors
    turtle.penup()
    turtle.forward(75)
    turtle.pendown()

# Winter: Brown trees (bare) with optional white "snow"
for i in range(3):
    tree(50 + i * 10, "brown")
    # Optional: Add small white triangles on top for snow
    turtle.penup()
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(50 + i * 10)  # Move to top of tree
    turtle.right(90)
    turtle.pendown()
    triangle(10, "white")  # Small snow triangle
    turtle.penup()
    turtle.right(90)
    turtle.back(50 + i * 10)  # Return to base
    turtle.left(90)
    turtle.back(10)
    turtle.forward(75)  # Move to next tree position
    turtle.pendown()

turtle.hideturtle()  # Hide the turtle cursor at the end
turtle.done()  # Keep the window open