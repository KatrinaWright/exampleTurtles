import random
from turtle import Turtle, Screen

class MazeSolver:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.speed(0)
        self.turtle.hideturtle()

    def generate_maze(self):
        self.turtle.penup()
        self.turtle.goto(-180, 180)
        self.turtle.pendown()

        for _ in range(18):
            self.turtle.forward(360)
            self.turtle.right(90)
            self.turtle.forward(20)
            self.turtle.right(90)
            self.turtle.forward(360)
            self.turtle.left(90)
            self.turtle.forward(20)
            self.turtle.left(90)

        # Add some random vertical lines
        for _ in range(10):
            x = random.randint(-160, 160)
            self.turtle.penup()
            self.turtle.goto(x, 180)
            self.turtle.pendown()
            self.turtle.setheading(270)
            self.turtle.forward(random.randint(40, 360))

    def solve_maze(self):
        self.turtle.penup()
        self.turtle.goto(-180, 180)
        self.turtle.pendown()
        self.turtle.color("red")

        stack = [(-180, 180)]
        visited = set()

        while stack and self.turtle.ycor() > -180:
            x, y = stack.pop()
            if (x, y) not in visited:
                self.turtle.goto(x, y)
                visited.add((x, y))

                for dx, dy in [(20, 0), (0, -20), (-20, 0), (0, 20)]:
                    new_x, new_y = x + dx, y + dy
                    if not self.turtle.distance(new_x, new_y) < 2 and -180 <= new_x <= 180 and -180 <= new_y <= 180:
                        stack.append((new_x, new_y))

        return list(visited)