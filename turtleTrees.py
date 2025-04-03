import turtle as t
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
  
def tree(size, color, x, y, turtle):
  if not size:
      size = 100
  random_size = random.randint(50, size) % 150 + 20
  stump(random_size, color, x, y, turtle)
  for i in range(random_size, 20, -10):
    triangle(i, color, turtle)
    up(20, turtle)
  

def setup_screen():
  canvas = t.Screen()
  canvas.setup(width=800, height=600)
  canvas.bgcolor("burlywood")
  turtle = t.Turtle()
  turtle.speed(0)
  return canvas, turtle

def grid_transitions(x_coordinate , random_number):
  
  color_parameters = {
    "spring": ["lightgreen", "pink", "turquoise", "palegreen", "aquamarine", "khaki", "plum", "springgreen", "mediumspringgreen", "mediumaquamarine", "mediumturquoise", "mediumseagreen"],
    "summer": ["darkgreen", "green", "teal", "YellowGreen", "OliveDrab", "LimeGreen" ],
    "fall": ["orange", "red", "yellow", "OrangeRed", "brown", "coral", "goldenrod", "gold", "tomato"],
    "winter": ["chocolate", "tan", "teal", "saddlebrown", "lavender", "wheat", "beige", "thistle", "mistyrose"]
  }

  length_list = [-400, -200, 0, 200, 400]
  color_list = color_parameters["spring"]
  if x_coordinate < length_list[1] and x_coordinate >= length_list[0]:
    color_list = color_parameters["spring"]
  elif x_coordinate < length_list[2] and x_coordinate >= length_list[1]:
    color_list = color_parameters["summer"]
  elif x_coordinate < length_list[3] and x_coordinate  >= length_list[2]:
    color_list = color_parameters["fall"]
  elif x_coordinate < length_list[4] and x_coordinate >= length_list[3]:
    color_list = color_parameters["winter"]  
  modifier = random_number % len(color_list)

  return color_list[modifier]

def main():
  canvas, turtle = setup_screen()
  previous = 0
  for y_coordinate in range(100, -300, -58):
    for x_coordinate in range(-400, 401, 83):
      random_number = random.randint(0, 15)
      if random_number <= previous:
        color = grid_transitions(x_coordinate - random_number, random_number)
        tree(200 - y_coordinate + random_number, color, x_coordinate-random_number, y_coordinate - 5, turtle)
      elif random_number % 7 == 0:
        color = grid_transitions(x_coordinate + random_number, random_number)
        tree(200 - y_coordinate + random_number, color, x_coordinate+ random_number, y_coordinate+5, turtle)
      else:
        color = grid_transitions(x_coordinate, random_number)
        tree(200 - y_coordinate + random_number, color, x_coordinate, y_coordinate, turtle)
      previous = random_number

  t.done()

if __name__ == "__main__":
  main()
