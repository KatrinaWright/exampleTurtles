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

tree(50, "green")
turtle.penup()
turtle.forward(75)
turtle.pendown()
tree(75, "pink")
turtle.penup()
turtle.back(300)
turtle.right(90)
turtle.forward(300)
turtle.left(90)
turtle.pendown()
tree(150, "orange")
up(-100)
turtle.penup()
turtle.forward(100)
turtle.pendown()
tree(40, "blue")
# up(10)
# triangle(20, "green")
# up(10)
# triangle(10, "green")