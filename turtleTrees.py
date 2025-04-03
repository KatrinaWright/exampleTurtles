import turtle
import random

def triangle(size, color, turtle):
  turtle.color(color)
  turtle.fillcolor(color)
  turtle.begin_fill()
  for i in range(3):
    turtle.forward(size)
    turtle.left(120)
  turtle.end_fill()
    
    
def up(distance, turtle):
  turtle.penup()
  turtle.left(90)
  turtle.forward(distance)
  turtle.right(90)
  turtle.forward(distance/4)
  turtle.pendown()
  
def stump(size, color, x, y, turtle):
  turtle.penup()
  turtle.goto(x, y)
  turtle.forward(size*(5/8))
  turtle.pendown()
  turtle.color("brown")
  turtle.fillcolor("brown")
  turtle.begin_fill()
  for i in range(5):
    turtle.left(90)
    turtle.forward(size/4)
  turtle.end_fill()
  turtle.right(90)
  turtle.color(color)
  turtle.back(size*(5/8))
  
def tree(size, color, x, y, t):

  random_size = random.randint(50, size) % 150 + 20
  stump(random_size, color, x, y, t)
  for i in range(random_size, 20, -10):
    triangle(i, color, t)
    up(20, t)
  

def setup_screen():
  canvas = turtle.Screen()
  canvas.setup(width=800, height=600)
  canvas.bgcolor("burlywood")
  t = turtle.Turtle()
  t.speed(0)
  return canvas, t
def grid_transitions(x, r):
  
  color_parameters = {
    "spring": ["lightgreen", "pink", "turquoise", "palegreen", "aquamarine", "khaki", "plum", "springgreen", "mediumspringgreen", "mediumaquamarine", "mediumturquoise", "mediumseagreen"],
    "summer": ["darkgreen", "green", "teal", "YellowGreen", "OliveDrab", "LimeGreen" ],
    "fall": ["orange", "red", "yellow", "OrangeRed", "brown", "coral", "goldenrod", "gold", "tomato"],
    "winter": ["chocolate", "tan", "teal", "saddlebrown", "lavender", "wheat", "beige", "thistle", "mistyrose"]
  }

  length_list = [-400, -200, 0, 200, 400]
  color = color_parameters["spring"]
  if x < length_list[1] and x >= length_list[0]:
    color = color_parameters["spring"]
  elif x < length_list[2] and x >= length_list[1]:
    color = color_parameters["summer"]
  elif x < length_list[3] and x >= length_list[2]:
    color = color_parameters["fall"]
  elif x < length_list[4] and x >= length_list[3]:
    color = color_parameters["winter"]  
  modifier = r % len(color)

  return color[modifier]

def main():
  canvas, t = setup_screen()
  prev = 0
  for j in range(100, -300, -58):
    for i in range(-400, 401, 83):
      odd_calc = random.randint(0, 15)
      if odd_calc <= prev:
        color = grid_transitions(i - odd_calc, odd_calc)
        tree(200 - j + odd_calc, color, i-odd_calc, j - 5, t)
      elif odd_calc % 7 == 0:
        color = grid_transitions(i + odd_calc, odd_calc)
        tree(200 - j + odd_calc, color, i+ odd_calc, j+5, t)
      else:
        color = grid_transitions(i, odd_calc)
        tree(200 - j + odd_calc, color, i, j, t)
      prev = odd_calc

  turtle.done()

if __name__ == "__main__":
  main()
