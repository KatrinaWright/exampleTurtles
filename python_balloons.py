

# # import turtle
# # import time

# # class BalloonMaker:
# #     """
# #     A class to create and manage hot air balloon drawing functions
# #     """
# #     def __init__(self):
# #         self.balloon_turtle = turtle.Turtle()
# #         self.balloon_turtle.speed(0)  # Fastest speed
# #         self.balloon_turtle.hideturtle()
    
# #     def draw_balloon_body(self, x, y, color, size=100):
# #         """
# #         Draws the main balloon part
# #         Parameters:
# #             x (int): x-coordinate for balloon center
# #             y (int): y-coordinate for balloon center
# #             color (str): color of the balloon
# #             size (int): size of the balloon (default 100)
# #         """
# #         self.balloon_turtle.penup()
# #         self.balloon_turtle.goto(x, y)
# #         self.balloon_turtle.pendown()
# #         self.balloon_turtle.color(color)
# #         self.balloon_turtle.begin_fill()
# #         self.balloon_turtle.circle(size)
# #         self.balloon_turtle.end_fill()

# #     def draw_basket(self, x, y, color, size=30):
# #         """
# #         Draws the balloon basket
# #         Parameters:
# #             x (int): x-coordinate for basket center
# #             y (int): y-coordinate for basket bottom
# #             color (str): color of the basket
# #             size (int): size of the basket (default 30)
# #         """
# #         self.balloon_turtle.penup()
# #         self.balloon_turtle.goto(x - size/2, y)
# #         self.balloon_turtle.pendown()
# #         self.balloon_turtle.color(color)
# #         self.balloon_turtle.begin_fill()
# #         for _ in range(2):
# #             self.balloon_turtle.forward(size)
# #             self.balloon_turtle.left(90)
# #             self.balloon_turtle.forward(size*1.2)
# #             self.balloon_turtle.left(90)
# #         self.balloon_turtle.end_fill()

# #     def draw_ropes(self, x, y, balloon_size=100, basket_size=30):
# #         """
# #         Draws the ropes connecting balloon to basket
# #         Parameters:
# #             x (int): x-coordinate of balloon center
# #             y (int): y-coordinate of balloon center
# #             balloon_size (int): size of the balloon
# #             basket_size (int): size of the basket
# #         """
# #         self.balloon_turtle.penup()
# #         self.balloon_turtle.goto(x - basket_size/2, y)
# #         self.balloon_turtle.pendown()
# #         self.balloon_turtle.goto(x - balloon_size/2, y + balloon_size)
# #         self.balloon_turtle.penup()
# #         self.balloon_turtle.goto(x + basket_size/2, y)
# #         self.balloon_turtle.pendown()
# #         self.balloon_turtle.goto(x + balloon_size/2, y + balloon_size)

# # class CloudMaker:
# #     """
# #     A class to create and manage cloud drawing functions
# #     """
# #     def __init__(self):
# #         self.cloud_turtle = turtle.Turtle()
# #         self.cloud_turtle.speed(0)
# #         self.cloud_turtle.hideturtle()
    
# #     def draw_cloud(self, x, y, color="white"):
# #         """
# #         Draws a simple cloud shape
# #         Parameters:
# #             x (int): x-coordinate for cloud center
# #             y (int): y-coordinate for cloud center
# #             color (str): color of the cloud (default white)
# #         """
# #         self.cloud_turtle.penup()
# #         self.cloud_turtle.goto(x, y)
# #         self.cloud_turtle.color(color)
        
# #         # Draw three overlapping circles for cloud shape
# #         circles = [(0, 0, 30), (-35, -10, 40), (35, -10, 40)]
# #         for cx, cy, radius in circles:
# #             self.cloud_turtle.penup()
# #             self.cloud_turtle.goto(x + cx, y + cy)
# #             self.cloud_turtle.pendown()
# #             self.cloud_turtle.begin_fill()
# #             self.cloud_turtle.circle(radius)
# #             self.cloud_turtle.end_fill()

# # def setup_screen():
# #     """
# #     Sets up the turtle screen with a light blue background
# #     Returns:
# #         screen: The configured turtle screen
# #     """
# #     screen = turtle.Screen()
# #     screen.bgcolor("light blue")
# #     screen.title("Hot Air Balloons Scene")
# #     return screen

# # def main():
# #     """
# #     Main function containing the sequence of drawing commands.
# #     Students will need to complete this function by calling the appropriate
# #     methods with the correct parameters to create the final scene.
# #     """
# #     # Setup screen
# #     screen = setup_screen()
    
# #     # Create our turtle makers
# #     balloon_maker = BalloonMaker()
# #     cloud_maker = CloudMaker()
    
# #     # TODO: Students will need to add code here!
# #     # Here's an example of what one balloon looks like:
# #     balloon_maker.draw_balloon_body(-100, 0, "red", 80)
# #     balloon_maker.draw_basket(-100, -100, "brown", 40)
# #     balloon_maker.draw_ropes(-100, -60, 80, 40)
    
# #     # Example cloud:
# #     cloud_maker.draw_cloud(50, 150)
    
# #     # Keep the window open (comment this out while testing)
# #     screen.mainloop()

# # if __name__ == "__main__":
# #     main()

# # """
# # STUDENT ASSIGNMENT:

# # Welcome to the Hot Air Balloon Scene Creator! Your task is to create a beautiful sky scene
# # with multiple hot air balloons and clouds. The code above provides you with all the tools
# # you need - you just need to figure out how to use them!

# # BACKGROUND READING:
# # - Each drawing function takes parameters that tell it WHERE to draw (x, y coordinates)
# #   and HOW to draw (colors, sizes)
# # - The coordinate system starts at (0,0) in the center of the screen
# #   - Moving right increases x, moving left decreases x
# #   - Moving up increases y, moving down decreases y

# # YOUR TASKS:

# # 1. Read through the code above and understand what each class and function does.
# #    Pay special attention to the parameters each function accepts.

# # 2. In the main() function, create a scene with:
# #    - At least 3 hot air balloons of different colors and sizes
# #    - At least 2 clouds at different positions
# #    - Try to make the scene balanced and visually appealing

# # 3. For each object you add, you'll need to think about:
# #    - Where should it be positioned? (x, y coordinates)
# #    - What color should it be?
# #    - How big should it be?

# # 4. Some questions to consider:
# #    - Why do we use classes to organize our drawing functions?
# #    - How do the parameters flow from function calls to function definitions?
# #    - What happens if you change the order of your drawing commands?

# # HINTS:
# # - Test one piece at a time
# # - Remember that y coordinates increase as you go up
# # - Try to space your balloons evenly across the screen
# # - Experiment with different colors and sizes
# # - Look at the example function calls in the comments

# # Challenge: Can you modify one of the classes to add a new feature to either
# #           the balloons or clouds? (Ask your teacher for guidance!)
# # """

# # import turtle
# # import time

# # class BalloonRider:
# #     """
# #     A class representing a turtle character riding in a hot air balloon
# #     """
# #     def __init__(self, name, color):
# #         """
# #         Creates a new turtle character with their own balloon
# #         Parameters:
# #             name (str): The name of the turtle character
# #             color (str): The color of both the turtle and their balloon
# #         """
# #         # Create and customize the turtle character
# #         self.turtle = turtle.Turtle()
# #         self.turtle.shape("turtle")
# #         self.turtle.color(color)
# #         self.name = name
# #         self.balloon_color = color
        
# #         # Start turtle in default position
# #         self.turtle.speed(3)  # Slower speed to see movement
# #         self.turtle.penup()
# #         self.turtle.goto(0, -200)
        
# #     def fly_to_position(self, x, y, balloon_size=80):
# #         """
# #         Moves the turtle to a position and draws their balloon around them
# #         Parameters:
# #             x (int): x-coordinate for balloon center
# #             y (int): y-coordinate for balloon center
# #             balloon_size (int): size of the balloon (default 80)
# #         """
# #         # Move turtle to where basket will be
# #         self.turtle.penup()
# #         self.turtle.goto(x, y - 60)  # Position in basket
        
# #         # Draw the balloon
# #         self.draw_balloon_body(x, y, balloon_size)
# #         self.draw_basket(x, y - 60, balloon_size)
# #         self.draw_ropes(x, y - 60, balloon_size, 40)
        
# #         # Face the turtle right
# #         self.turtle.setheading(0)
    
# #     def draw_balloon_body(self, x, y, size):
# #         """
# #         Draws the main balloon part
# #         """
# #         helper = turtle.Turtle()
# #         helper.hideturtle()
# #         helper.speed(0)
# #         helper.penup()
# #         helper.goto(x, y)
# #         helper.pendown()
# #         helper.color(self.balloon_color)
# #         helper.begin_fill()
# #         helper.circle(size)
# #         helper.end_fill()
# #         helper.clear()
# #         del helper

# #     def draw_basket(self, x, y, balloon_size):
# #         """
# #         Draws the balloon basket
# #         """
# #         helper = turtle.Turtle()
# #         helper.hideturtle()
# #         helper.speed(0)
# #         helper.penup()
# #         helper.goto(x - 20, y)
# #         helper.pendown()
# #         helper.color("brown")
# #         helper.begin_fill()
# #         for _ in range(2):
# #             helper.forward(40)
# #             helper.left(90)
# #             helper.forward(48)
# #             helper.left(90)
# #         helper.end_fill()
# #         helper.clear()
# #         del helper

# #     def draw_ropes(self, x, y, balloon_size, basket_size):
# #         """
# #         Draws the ropes connecting balloon to basket
# #         """
# #         helper = turtle.Turtle()
# #         helper.hideturtle()
# #         helper.speed(0)
# #         helper.color("brown")
        
# #         # Left rope
# #         helper.penup()
# #         helper.goto(x - basket_size/2, y)
# #         helper.pendown()
# #         helper.goto(x - balloon_size/2, y + balloon_size)
        
# #         # Right rope
# #         helper.penup()
# #         helper.goto(x + basket_size/2, y)
# #         helper.pendown()
# #         helper.goto(x + balloon_size/2, y + balloon_size)
        
# #         helper.clear()
# #         del helper
    
# #     def wave(self):
# #         """Makes the turtle wave by rotating left and right"""
# #         for _ in range(2):
# #             self.turtle.left(30)
# #             time.sleep(0.2)
# #             self.turtle.right(60)
# #             time.sleep(0.2)
# #             self.turtle.left(30)

# # def setup_screen():
# #     """Sets up the turtle screen with a light blue background"""
# #     screen = turtle.Screen()
# #     screen.bgcolor("light blue")
# #     screen.title("Turtle Balloon Riders")
# #     return screen

# # def main():
# #     """
# #     Main function containing the sequence of drawing commands.
# #     Students will need to complete this function by creating and positioning
# #     their turtle balloon riders.
# #     """
# #     # Setup screen
# #     screen = setup_screen()
    
# #     # Create our first turtle balloon rider as an example
# #     red_rider = BalloonRider("Red", "red")
# #     red_rider.fly_to_position(-100, 0)
# #     red_rider.wave()
    
# #     # TODO: Students add their own turtle balloon riders here!
# #     # Example of how to create and position more riders:
# #     # blue_rider = BalloonRider("Blue", "blue")
# #     # blue_rider.fly_to_position(100, 50, balloon_size=100)
# #     # blue_rider.wave()
    
# #     # Keep the window open
# #     screen.mainloop()

# # if __name__ == "__main__":
# #     main()

# # """
# # STUDENT ASSIGNMENT:

# # Welcome to the Turtle Balloon Riders! In this assignment, you'll help different turtle
# # characters fly their hot air balloons in the sky. Each turtle gets their own balloon
# # in their favorite color!

# # BACKGROUND:
# # - Each turtle is created as a BalloonRider object
# # - When you create a BalloonRider, you give them:
# #   * A name (like "Red" or "Blue")
# #   * A color (which will be their balloon color too!)
# # - You can then tell each turtle where to fly their balloon using fly_to_position()
# # - After they reach their position, you can make them wave!

# # YOUR TASKS:

# # 1. Look at how the red turtle rider is created and positioned in the example.
# #    Watch what happens when you run the program!

# # 2. Add at least three more turtle balloon riders to create a scene:
# #    - Create each rider with a different name and color
# #    - Position them at different places in the sky
# #    - Try different balloon sizes
# #    - Make them wave when they reach their position

# # 3. For each new balloon rider, you'll need to:
# #    - Create them using BalloonRider(name, color)
# #    - Tell them where to fly using fly_to_position(x, y, balloon_size)
# #    - Optional: Make them wave using wave()

# # 4. Some questions to think about:
# #    - How does creating a new BalloonRider create a new turtle?
# #    - What happens when you call methods on different riders?
# #    - How do the function parameters affect each turtle differently?

# # HINTS:
# # - Try these colors: "blue", "purple", "green", "orange", "pink"
# # - Experiment with different x, y positions to spread out the balloons
# # - Try different balloon_size values to make some bigger or smaller
# # - Don't forget to make your turtles wave to each other!

# # Challenge: Can you figure out how to make all your turtles wave at the same time?
# #           (Ask your teacher for hints about using time.sleep()!)
# # """


# # import turtle
# # import time

# # class BalloonRider:
# #     """
# #     A class representing a turtle character riding in a hot air balloon
# #     """
# #     def __init__(self, name, color):
# #         """
# #         Creates a new turtle character with their own balloon
# #         Parameters:
# #             name (str): The name of the turtle character
# #             color (str): The color of both the turtle and their balloon
# #         """
# #         # Create and customize the turtle character
# #         self.turtle = turtle.Turtle()
# #         self.turtle.shape("turtle")
# #         self.turtle.color(color)
# #         self.name = name
# #         self.balloon_color = color
        
# #         # Start turtle in default position
# #         self.turtle.speed(3)  # Slower speed to see movement
# #         self.turtle.penup()
# #         self.turtle.goto(0, -200)
        
# #     def fly_to_position(self, x, y, balloon_size=80):
# #         """
# #         Moves the turtle to a position and draws their balloon around them
# #         Parameters:
# #             x (int): x-coordinate for balloon center
# #             y (int): y-coordinate for balloon center
# #             balloon_size (int): size of the balloon (default 80)
# #         """
# #         # Move turtle to starting position to build balloon
# #         self.turtle.penup()
# #         self.turtle.goto(x, y)
        
# #         # Turtle builds their own balloon!
# #         self.turtle.color(self.balloon_color)
# #         self.turtle.pendown()
# #         self.turtle.begin_fill()
# #         self.turtle.circle(balloon_size)
# #         self.turtle.end_fill()
        
# #         # Draw the ropes
# #         self.turtle.penup()
# #         self.turtle.goto(x - 20, y - 60)
# #         self.turtle.pendown()
# #         self.turtle.goto(x - balloon_size/2, y + balloon_size)
        
# #         self.turtle.penup()
# #         self.turtle.goto(x + 20, y - 60)
# #         self.turtle.pendown()
# #         self.turtle.goto(x + balloon_size/2, y + balloon_size)
        
# #         # Draw the basket
# #         self.turtle.penup()
# #         self.turtle.goto(x - 20, y - 100)
# #         self.turtle.color("brown")
# #         self.turtle.pendown()
# #         self.turtle.begin_fill()
# #         for _ in range(2):
# #             self.turtle.forward(40)
# #             self.turtle.left(90)
# #             self.turtle.forward(48)
# #             self.turtle.left(90)
# #         self.turtle.end_fill()
        
# #         # Move into basket and face upward
# #         self.turtle.penup()
# #         self.turtle.goto(x, y - 60)
# #         self.turtle.setheading(90)
# #         self.turtle.color(self.balloon_color)
    
# #     def wave(self):
# #         """Makes the turtle wave by rotating left and right"""
# #         for _ in range(10):
# #             self.turtle.left(30)
# #             time.sleep(0.2)
# #             self.turtle.right(60)
# #             time.sleep(0.2)
# #             self.turtle.left(30)

# # def setup_screen():
# #     """Sets up the turtle screen with a light blue background"""
# #     screen = turtle.Screen()
# #     screen.bgcolor("light blue")
# #     screen.title("Turtle Balloon Riders")
# #     return screen

# # def main():
# #     """
# #     Main function containing the sequence of drawing commands.
# #     Students will need to complete this function by creating and positioning
# #     their turtle balloon riders.
# #     """
# #     # Setup screen
# #     screen = setup_screen()
    
# #     # Create our first turtle balloon rider as an example
# #     red_rider = BalloonRider("Red", "red")
# #     red_rider.fly_to_position(-100, 0)
    

# #     blue_rider = BalloonRider("nemo", "blue")
# #     blue_rider.fly_to_position(150, 50)
# #     blue_rider.wave()
# #     red_rider.wave()
    
# #     # TODO: Students add their own turtle balloon riders here!
# #     # Example of how to create and position more riders:
# #     # blue_rider = BalloonRider("Blue", "blue")
# #     # blue_rider.fly_to_position(100, 50, balloon_size=100)
# #     # blue_rider.wave()
    
# #     # Keep the window open
# #     screen.mainloop()

# # if __name__ == "__main__":
# #     main()

# # """
# # STUDENT ASSIGNMENT:

# # Welcome to the Turtle Balloon Riders! In this assignment, you'll help different turtle
# # characters fly their hot air balloons in the sky. Each turtle gets their own balloon
# # in their favorite color!

# # BACKGROUND:
# # - Each turtle is created as a BalloonRider object
# # - When you create a BalloonRider, you give them:
# #   * A name (like "Red" or "Blue")
# #   * A color (which will be their balloon color too!)
# # - You can then tell each turtle where to fly their balloon using fly_to_position()
# # - Watch how each turtle builds their own balloon!
# # - After they reach their position, you can make them wave!

# # YOUR TASKS:

# # 1. Look at how the red turtle rider is created and positioned in the example.
# #    Watch what happens when you run the program!

# # 2. Add at least three more turtle balloon riders to create a scene:
# #    - Create each rider with a different name and color
# #    - Position them at different places in the sky
# #    - Try different balloon sizes
# #    - Make them wave when they reach their position

# # 3. For each new balloon rider, you'll need to:
# #    - Create them using BalloonRider(name, color)
# #    - Tell them where to fly using fly_to_position(x, y, balloon_size)
# #    - Optional: Make them wave using wave()

# # 4. Some questions to think about:
# #    - How does creating a new BalloonRider create a new turtle?
# #    - What happens when you call methods on different riders?
# #    - How do the function parameters affect each turtle differently?

# # HINTS:
# # - Try these colors: "blue", "purple", "green", "orange", "pink"
# # - Experiment with different x, y positions to spread out the balloons
# # - Try different balloon_size values to make some bigger or smaller
# # - Don't forget to make your turtles wave to each other!

# # Challenge: Can you figure out how to make all your turtles wave at the same time?
# #           (Ask your teacher for hints about using time.sleep()!)
# # """

# # import turtle
# # import time

# # class BalloonRider:
# #     """
# #     A class representing a turtle character riding in a hot air balloon
# #     """
# #     def __init__(self, color):
# #         """
# #         Creates a new turtle character with their own balloon
# #         Parameters:
# #             color (str): The color of both the turtle and their balloon
# #         """
# #         # Create and customize the turtle character
# #         self.turtle = turtle.Turtle()
# #         self.turtle.shape("turtle")
# #         self.turtle.color(color)
# #         self.balloon_color = color
        
# #         # Start turtle in default position
# #         self.turtle.speed(3)  # Slower speed to see movement
# #         self.turtle.penup()
# #         self.turtle.goto(0, -200)
        
# #     def fly_to_position(self, x, y, balloon_size=80):
# #         """
# #         Moves the turtle to a position and draws their balloon around them
# #         Parameters:
# #             x (int): x-coordinate for balloon center
# #             y (int): y-coordinate for balloon center
# #             balloon_size (int): size of the balloon (default 80)
# #         """
# #         # Move turtle to starting position to build balloon
# #         self.turtle.penup()
# #         self.turtle.goto(x, y)
        
# #         # Turtle builds their own balloon!
# #         self.turtle.color(self.balloon_color)
# #         self.turtle.pendown()
# #         self.turtle.begin_fill()
# #         self.turtle.circle(balloon_size)
# #         self.turtle.end_fill()
        
# #         # Draw the ropes
# #         self.turtle.penup()
# #         self.turtle.goto(x - 20, y - 60)
# #         self.turtle.pendown()
# #         self.turtle.goto(x - balloon_size/2, y + balloon_size)
        
# #         self.turtle.penup()
# #         self.turtle.goto(x + 20, y - 60)
# #         self.turtle.pendown()
# #         self.turtle.goto(x + balloon_size/2, y + balloon_size)
        
# #         # Draw the basket
# #         self.turtle.penup()
# #         self.turtle.goto(x - 20, y - 100)
# #         self.turtle.color("brown")
# #         self.turtle.pendown()
# #         self.turtle.begin_fill()
# #         for _ in range(2):
# #             self.turtle.forward(40)
# #             self.turtle.left(90)
# #             self.turtle.forward(48)
# #             self.turtle.left(90)
# #         self.turtle.end_fill()
        
# #         # Move into basket and face upward
# #         self.turtle.penup()
# #         self.turtle.goto(x, y - 60)
# #         self.turtle.setheading(90)
# #         self.turtle.color(self.balloon_color)
    
# #     def wave(self):
# #         """Makes the turtle wave by rotating left and right"""
# #         for _ in range(5):
# #             self.turtle.left(30)
# #             time.sleep(0.2)
# #             self.turtle.right(60)
# #             time.sleep(0.2)
# #             self.turtle.left(30)

# # def setup_screen():
# #     """Sets up the turtle screen with a light blue background"""
# #     screen = turtle.Screen()
# #     screen.bgcolor("light blue")
# #     screen.title("Turtle Balloon Riders")
# #     return screen

# # def main():
# #     """
# #     Main function containing the sequence of drawing commands.
# #     Students will need to complete this function by creating and positioning
# #     their turtle balloon riders.
# #     """
# #     # Setup screen
# #     screen = setup_screen()
    
# #     # Create our first turtle balloon rider as an example
# #     red_rider = BalloonRider("red")
# #     red_rider.fly_to_position(-100, 0)
    
# #     # Create a second turtle balloon rider
# #     blue_rider = BalloonRider("blue")
# #     blue_rider.fly_to_position(150, 50)
    
# #     # Make both turtles wave
# #     red_rider.wave()
# #     blue_rider.wave()
    
# #     # TODO: Students add their own turtle balloon riders here!
# #     # Example of how to create and position more riders:
# #     # green_rider = BalloonRider("green")
# #     # green_rider.fly_to_position(0, 100, balloon_size=100)
# #     # green_rider.wave()
    
# #     # Keep the window open
# #     screen.mainloop()

# # if __name__ == "__main__":
# #     main()

# # """
# # STUDENT ASSIGNMENT:

# # Welcome to the Turtle Balloon Riders! In this assignment, you'll help different turtle
# # characters fly their hot air balloons in the sky. Each turtle gets their own balloon
# # in their favorite color!

# # BACKGROUND:
# # - Each turtle is created as a BalloonRider object
# # - When you create a BalloonRider, you give them a color (which will be their balloon color too!)
# # - You can then tell each turtle where to fly their balloon using fly_to_position()
# # - Watch how each turtle builds their own balloon!
# # - After they reach their position, you can make them wave!

# # HOW TO CREATE YOUR OWN BALLOON RIDER:
# # 1. Create a new BalloonRider object:
# #    my_rider = BalloonRider("your_favorite_color")

# # 2. Make your rider fly to a position:
# #    my_rider.fly_to_position(x, y, balloon_size)
# #    - x and y are the coordinates in the sky (try different numbers!)
# #    - balloon_size is optional (default is 80)

# # 3. Make your rider wave:
# #    my_rider.wave()

# # YOUR TASKS:

# # 1. Look at how the red and blue turtle riders are created and positioned in the example.
# #    Watch what happens when you run the program!

# # 2. Add at least three more turtle balloon riders to create a scene:
# #    - Create each rider with a different color
# #    - Position them at different places in the sky
# #    - Try different balloon sizes
# #    - Make them wave when they reach their position

# # 3. For each new balloon rider, you'll need to:
# #    - Create them using BalloonRider(color)
# #    - Tell them where to fly using fly_to_position(x, y, balloon_size)
# #    - Optional: Make them wave using wave()

# # 4. Some questions to think about:
# #    - How does creating a new BalloonRider create a new turtle?
# #    - What happens when you call methods on different riders?
# #    - How do the function parameters affect each turtle differently?

# # HINTS:
# # - Try these colors: "purple", "green", "orange", "pink", "yellow"
# # - Experiment with different x, y positions to spread out the balloons
# # - Try different balloon_size values to make some bigger or smaller
# # - Don't forget to make your turtles wave to each other!

# # Challenge: Can you figure out how to make all your turtles wave at the same time?
# #           (Ask your teacher for hints about using time.sleep()!)
# # """


# # import turtle
# # import time

# # class BalloonRider:
# #     """
# #     A class representing a turtle character riding in a hot air balloon
# #     """
# #     def __init__(self, color):
# #         """
# #         Creates a new turtle character with their own balloon
# #         Parameters:
# #             color (str): The color of both the turtle and their balloon
# #         """
# #         # Create and customize the turtle character
# #         self.turtle = turtle.Turtle()
# #         self.turtle.shape("turtle")
# #         self.turtle.color(color)
# #         self.balloon_color = color
        
# #         # Start turtle in default position
# #         self.turtle.speed(3)  # Slower speed to see movement
# #         self.turtle.penup()
# #         self.turtle.goto(0, -200)
        
# #     def fly_to_position(self, x, y, balloon_size=80):
# #         """
# #         Moves the turtle to a position and draws their balloon around them
# #         Parameters:
# #             x (int): x-coordinate for balloon center
# #             y (int): y-coordinate for balloon center
# #             balloon_size (int): size of the balloon (default 80)
# #         """
# #         # Move turtle to starting position to build balloon
# #         self.turtle.penup()
# #         self.turtle.goto(x, y)
        
# #         # Turtle builds their own balloon!
# #         self.turtle.color(self.balloon_color)
# #         self.turtle.pendown()
# #         self.turtle.begin_fill()
# #         self.turtle.circle(balloon_size)
# #         self.turtle.end_fill()
        
# #         # Draw the ropes
# #         self.turtle.penup()
# #         self.turtle.goto(x - 20, y - 60)
# #         self.turtle.pendown()
# #         self.turtle.goto(x - balloon_size/2, y + balloon_size)
        
# #         self.turtle.penup()
# #         self.turtle.goto(x + 20, y - 60)
# #         self.turtle.pendown()
# #         self.turtle.goto(x + balloon_size/2, y + balloon_size)
        
# #         # Draw the basket
# #         self.turtle.penup()
# #         self.turtle.goto(x - 20, y - 100)
# #         self.turtle.color("brown")
# #         self.turtle.pendown()
# #         self.turtle.begin_fill()
# #         for _ in range(2):
# #             self.turtle.forward(40)
# #             self.turtle.left(90)
# #             self.turtle.forward(48)
# #             self.turtle.left(90)
# #         self.turtle.end_fill()
        
# #         # Move into basket and face upward
# #         self.turtle.penup()
# #         self.turtle.goto(x, y - 60)
# #         self.turtle.setheading(90)
# #         self.turtle.color(self.balloon_color)
    
# #     def wave(self):
# #         """Makes the turtle wave by rotating left and right"""
# #         for _ in range(10):
# #             self.turtle.left(30)
# #             time.sleep(0.2)
# #             self.turtle.right(60)
# #             time.sleep(0.2)
# #             self.turtle.left(30)

# # def setup_screen():
# #     """Sets up the turtle screen with a light blue background"""
# #     screen = turtle.Screen()
# #     screen.bgcolor("light blue")
# #     screen.title("Turtle Balloon Riders")
# #     return screen

# # def main():
# #     """
# #     Main function containing the sequence of drawing commands.
# #     Students will need to complete this function by creating and positioning
# #     their turtle balloon riders.
# #     """
# #     # Setup screen
# #     screen = setup_screen()
    
# #     # Create our first turtle balloon rider as an example
# #     red_rider = BalloonRider("red")
# #     red_rider.fly_to_position(-100, 0)
    
# #     # Create a second turtle balloon rider
# #     blue_rider = BalloonRider("blue")
# #     blue_rider.fly_to_position(150, 50)
    
# #     # Make both turtles wave
# #     red_rider.wave()
# #     blue_rider.wave()
    
# #     # TODO: Students add their own turtle balloon riders here!
# #     # Example of how to create and position more riders:
# #     # green_rider = BalloonRider("green")
# #     # green_rider.fly_to_position(0, 100, balloon_size=100)
# #     # green_rider.wave()
    
# #     # Keep the window open
# #     screen.mainloop()

# # # if __name__ == "__main__":
# # #     main()

# # """

# # # Answer key for the challenge: Making all turtles wave at the same time
# # """
# # def challenge_solution():
# #     screen = setup_screen()
    
# #     # Create multiple balloon riders
# #     riders = [
# #         BalloonRider("red"),
# #         BalloonRider("blue"),
# #         BalloonRider("green"),
# #         BalloonRider("purple"),
# #         BalloonRider("orange")
# #     ]
    
# #     # Position the riders
# #     positions = [(-150, 0), (-75, 50), (0, 100), (75, 50), (150, 0)]
# #     for rider, (x, y) in zip(riders, positions):
# #         rider.fly_to_position(x, y)
    
# #     # Make all riders wave simultaneously
# #     for _ in range(10):
# #         for rider in riders:
# #             rider.turtle.left(30)
# #         time.sleep(0.2)
# #         for rider in riders:
# #             rider.turtle.right(60)
# #         time.sleep(0.2)
# #         for rider in riders:
# #             rider.turtle.left(30)
    
# #     screen.mainloop()

# # # Uncomment the line below to run the challenge solution
# # challenge_solution()
# # """
# # STUDENT ASSIGNMENT:

# # Welcome to the Turtle Balloon Riders! In this assignment, you'll help different turtle
# # characters fly their hot air balloons in the sky. Each turtle gets their own balloon
# # in their favorite color!

# # BACKGROUND:
# # - Each turtle is created as a BalloonRider object
# # - When you create a BalloonRider, you give them a color (which will be their balloon color too!)
# # - You can then tell each turtle where to fly their balloon using fly_to_position()
# # - Watch how each turtle builds their own balloon!
# # - After they reach their position, you can make them wave!

# # HOW TO CREATE YOUR OWN BALLOON RIDER:
# # 1. Create a new BalloonRider object:
# #    my_rider = BalloonRider("your_favorite_color")

# # 2. Make your rider fly to a position:
# #    my_rider.fly_to_position(x, y, balloon_size)
# #    - x and y are the coordinates in the sky (try different numbers!)
# #    - balloon_size is optional (default is 80)

# # 3. Make your rider wave:
# #    my_rider.wave()

# # YOUR TASKS:

# # 1. Look at how the red and blue turtle riders are created and positioned in the example.
# #    Watch what happens when you run the program!

# # 2. Add at least three more turtle balloon riders to create a scene:
# #    - Create each rider with a different color
# #    - Position them at different places in the sky
# #    - Try different balloon sizes
# #    - Make them wave when they reach their position

# # 3. For each new balloon rider, you'll need to:
# #    - Create them using BalloonRider(color)
# #    - Tell them where to fly using fly_to_position(x, y, balloon_size)
# #    - Optional: Make them wave using wave()

# # 4. Some questions to think about:
# #    - How does creating a new BalloonRider create a new turtle?
# #    - What happens when you call methods on different riders?
# #    - How do the function parameters affect each turtle differently?

# # HINTS:
# # - Try these colors: "purple", "green", "orange", "pink", "yellow"
# # - Experiment with different x, y positions to spread out the balloons
# # - Try different balloon_size values to make some bigger or smaller
# # - Don't forget to make your turtles wave to each other!

# # Challenge: Can you figure out how to make all your turtles wave at the same time?
# #           (Ask your teacher for hints about using time.sleep()!)
# # """

# # import turtle
# # import time

# # class BalloonRider:
# #     """
# #     A class representing a turtle character riding in a hot air balloon
# #     """
# #     def __init__(self, color):
# #         """
# #         Creates a new turtle character with their own balloon
# #         Parameters:
# #             color (str): The color of both the turtle and their balloon
# #         """
# #         # Create and customize the turtle character
# #         self.turtle = turtle.Turtle()
# #         self.turtle.shape("turtle")
# #         self.turtle.color(color)
# #         self.balloon_color = color
        
# #         # Start turtle in default position
# #         self.turtle.speed(3)  # Slower speed to see movement
# #         self.turtle.penup()
# #         self.turtle.goto(0, -200)
        
# #     def fly_to_position(self, x, y, balloon_size=80):
# #         """
# #         Moves the turtle to a position and draws their balloon around them
# #         Parameters:
# #             x (int): x-coordinate for balloon center
# #             y (int): y-coordinate for balloon center
# #             balloon_size (int): size of the balloon (default 80)
# #         """
# #         # Move turtle to starting position to build balloon
# #         self.turtle.penup()
# #         self.turtle.goto(x, y)
        
# #         # Turtle builds their own balloon!
# #         self.turtle.color(self.balloon_color)
# #         self.turtle.pendown()
# #         self.turtle.begin_fill()
# #         self.turtle.circle(balloon_size)
# #         self.turtle.end_fill()
        
# #         # Draw the ropes
# #         self.turtle.penup()
# #         self.turtle.goto(x - 20, y - 60)
# #         self.turtle.pendown()
# #         self.turtle.goto(x - balloon_size/2, y + balloon_size)
        
# #         self.turtle.penup()
# #         self.turtle.goto(x + 20, y - 60)
# #         self.turtle.pendown()
# #         self.turtle.goto(x + balloon_size/2, y + balloon_size)
        
# #         # Draw the basket
# #         self.turtle.penup()
# #         self.turtle.goto(x - 20, y - 100)
# #         self.turtle.color("brown")
# #         self.turtle.pendown()
# #         self.turtle.begin_fill()
# #         for _ in range(2):
# #             self.turtle.forward(40)
# #             self.turtle.left(90)
# #             self.turtle.forward(48)
# #             self.turtle.left(90)
# #         self.turtle.end_fill()
        
# #         # Move into basket and face upward
# #         self.turtle.penup()
# #         self.turtle.goto(x, y - 60)
# #         self.turtle.setheading(90)
# #         self.turtle.color(self.balloon_color)
    
# #     def wave(self):
# #         """Makes the turtle wave by rotating left and right"""
# #         for _ in range(10):
# #             self.turtle.left(30)
# #             time.sleep(0.2)
# #             self.turtle.right(60)
# #             time.sleep(0.2)
# #             self.turtle.left(30)

# # def setup_screen():
# #     """Sets up the turtle screen with a light blue background"""
# #     screen = turtle.Screen()
# #     screen.bgcolor("light blue")
# #     screen.title("Turtle Balloon Riders")
# #     return screen

# # def main():
# #     """
# #     Main function containing the sequence of drawing commands.
# #     Students will need to complete this function by creating and positioning
# #     their turtle balloon riders.
# #     """
# #     # Setup screen
# #     screen = setup_screen()
    
# #     # Create our first turtle balloon rider as an example
# #     red_rider = BalloonRider("red")
# #     red_rider.fly_to_position(-100, 0)
    
# #     # Create a second turtle balloon rider
# #     blue_rider = BalloonRider("blue")
# #     blue_rider.fly_to_position(150, 50)
    
# #     # Make both turtles wave
# #     red_rider.wave()
# #     blue_rider.wave()
    
# #     # TODO: Students add their own turtle balloon riders here!
# #     # Example of how to create and position more riders:
# #     # green_rider = BalloonRider("green")
# #     # green_rider.fly_to_position(0, 100, balloon_size=100)
# #     # green_rider.wave()
    
# #     # Keep the window open
# #     screen.mainloop()

# # # if __name__ == "__main__":
# # #     main()

# # """

# # # Answer key for the challenge: Making all turtles wave at the same time
# # """
# # def challenge_solution():
# #     screen = setup_screen()
    
# #     # Create multiple balloon riders
# #     riders = [
# #         BalloonRider("red"),
# #         BalloonRider("blue"),
# #         BalloonRider("green"),
# #         BalloonRider("purple"),
# #         BalloonRider("orange")
# #     ]
    
# #     # Position the riders
# #     positions = [(-150, 0), (-75, 50), (0, 100), (75, 50), (150, 0)]
# #     for rider, (x, y) in zip(riders, positions):
# #         rider.fly_to_position(x, y)
    
# #     # Make riders do the wave in sequence
# #     for _ in range(3):  # Do the wave 3 times
# #         for rider in riders:
# #             # Each rider does one wave motion
# #             rider.turtle.left(30)
# #             time.sleep(0.1)
# #             rider.turtle.right(60)
# #             time.sleep(0.1)
# #             rider.turtle.left(30)
# #             time.sleep(0.1)  # Brief pause before next rider starts
    
# #     screen.mainloop()

# # # Uncomment the line below to run the challenge solution
# # challenge_solution()
# # """
# # STUDENT ASSIGNMENT:

# # Welcome to the Turtle Balloon Riders! In this assignment, you'll help different turtle
# # characters fly their hot air balloons in the sky. Each turtle gets their own balloon
# # in their favorite color!

# # BACKGROUND:
# # - Each turtle is created as a BalloonRider object
# # - When you create a BalloonRider, you give them a color (which will be their balloon color too!)
# # - You can then tell each turtle where to fly their balloon using fly_to_position()
# # - Watch how each turtle builds their own balloon!
# # - After they reach their position, you can make them wave!

# # HOW TO CREATE YOUR OWN BALLOON RIDER:
# # 1. Create a new BalloonRider object:
# #    my_rider = BalloonRider("your_favorite_color")

# # 2. Make your rider fly to a position:
# #    my_rider.fly_to_position(x, y, balloon_size)
# #    - x and y are the coordinates in the sky (try different numbers!)
# #    - balloon_size is optional (default is 80)

# # 3. Make your rider wave:
# #    my_rider.wave()

# # YOUR TASKS:

# # 1. Look at how the red and blue turtle riders are created and positioned in the example.
# #    Watch what happens when you run the program!

# # 2. Add at least three more turtle balloon riders to create a scene:
# #    - Create each rider with a different color
# #    - Position them at different places in the sky
# #    - Try different balloon sizes
# #    - Make them wave when they reach their position

# # 3. For each new balloon rider, you'll need to:
# #    - Create them using BalloonRider(color)
# #    - Tell them where to fly using fly_to_position(x, y, balloon_size)
# #    - Optional: Make them wave using wave()

# # 4. Some questions to think about:
# #    - How does creating a new BalloonRider create a new turtle?
# #    - What happens when you call methods on different riders?
# #    - How do the function parameters affect each turtle differently?

# # HINTS:
# # - Try these colors: "purple", "green", "orange", "pink", "yellow"
# # - Experiment with different x, y positions to spread out the balloons
# # - Try different balloon_size values to make some bigger or smaller
# # - Don't forget to make your turtles wave to each other!

# # Challenge: Can you make your turtles "do the wave" like in a stadium? 
# #           Make each turtle wave one after another in sequence!
# #           (Ask your teacher for hints about using lists and loops!)
# # """


# import turtle
# import time

# class BalloonRider:
#     """
#     A class representing a turtle character riding in a hot air balloon
#     """
#     def __init__(self, color):
#         """
#         Creates a new turtle character with their own balloon
#         Parameters:
#             color (str): The color of both the turtle and their balloon
#         """
#         # Create and customize the turtle character
#         self.turtle = turtle.Turtle()
#         self.turtle.shape("turtle")
#         self.turtle.color(color)
#         self.balloon_color = color
        
#         # Start turtle in default position
#         self.turtle.speed(3)  # Slower speed to see movement
#         self.turtle.penup()
#         self.turtle.goto(0, -200)
        
#     def fly_to_position(self, x, y, balloon_size=80):
#         """
#         Moves the turtle to a position and draws their balloon around them
#         Parameters:
#             x (int): x-coordinate for balloon center
#             y (int): y-coordinate for balloon center
#             balloon_size (int): size of the balloon (default 80)
#         """
#         # Move turtle to starting position to build balloon
#         self.turtle.penup()
#         self.turtle.goto(x, y)
        
#         # Turtle builds their own balloon!
#         self.turtle.color(self.balloon_color)
#         self.turtle.pendown()
#         self.turtle.begin_fill()
#         self.turtle.circle(balloon_size)
#         self.turtle.end_fill()
        
#         # Draw the ropes
#         self.turtle.penup()
#         self.turtle.goto(x - 20, y - 60)
#         self.turtle.pendown()
#         self.turtle.goto(x - balloon_size/2, y + balloon_size)
        
#         self.turtle.penup()
#         self.turtle.goto(x + 20, y - 60)
#         self.turtle.pendown()
#         self.turtle.goto(x + balloon_size/2, y + balloon_size)
        
#         # Draw the basket
#         self.turtle.penup()
#         self.turtle.goto(x - 20, y - 100)
#         self.turtle.color("brown")
#         self.turtle.pendown()
#         self.turtle.begin_fill()
#         for _ in range(2):
#             self.turtle.forward(40)
#             self.turtle.left(90)
#             self.turtle.forward(48)
#             self.turtle.left(90)
#         self.turtle.end_fill()
        
#         # Move into basket and face upward
#         self.turtle.penup()
#         self.turtle.goto(x, y - 60)
#         self.turtle.setheading(90)
#         self.turtle.color(self.balloon_color)
    
#     def wave(self):
#         """Makes the turtle wave by rotating left and right"""
#         for _ in range(10):
#             self.turtle.left(30)
#             time.sleep(0.2)
#             self.turtle.right(60)
#             time.sleep(0.2)
#             self.turtle.left(30)

# def setup_screen():
#     """Sets up the turtle screen with a light blue background"""
#     screen = turtle.Screen()
#     screen.bgcolor("light blue")
#     screen.title("Turtle Balloon Riders")
#     return screen

# def main():
#     """
#     Main function containing the sequence of drawing commands.
#     Students will need to complete this function by creating and positioning
#     their turtle balloon riders.
#     """
#     # Setup screen
#     screen = setup_screen()
    
#     # Create our first turtle balloon rider as an example
#     red_rider = BalloonRider("red")
#     red_rider.fly_to_position(-100, 0)
    
#     # Create a second turtle balloon rider
#     blue_rider = BalloonRider("blue")
#     blue_rider.fly_to_position(150, 50)
    
#     # Make both turtles wave
#     red_rider.wave()
#     blue_rider.wave()
    
#     # TODO: Students add their own turtle balloon riders here!
#     # Example of how to create and position more riders:
#     # green_rider = BalloonRider("green")
#     # green_rider.fly_to_position(0, 100, balloon_size=100)
#     # green_rider.wave()
    
#     # Keep the window open
#     screen.mainloop()

# # if __name__ == "__main__":
# #     main()

# """

# # Answer key for the challenge: Making turtles "do the wave"
# """
# def challenge_solution():
#     screen = setup_screen()
    
#     # Create multiple balloon riders
#     riders = [
#         BalloonRider("red"),
#         BalloonRider("blue"),
#         BalloonRider("green"),
#         BalloonRider("purple"),
#         BalloonRider("orange")
#     ]
#     reversed =  list(reversed(riders))
    
#     # Position the riders
#     positions = [(-150, 0), (-75, 50), (0, 100), (75, 50), (150, 0)]
#     for rider, (x, y) in zip(riders, positions):
#         rider.fly_to_position(x, y)
    
#     # Make all riders wave simultaneously
#     for _ in range(10):
#         for rider in riders:
#             rider.turtle.left(30)
#         time.sleep(0.1)
#         for rider in reversed:
#             rider.turtle.right(60)
#         time.sleep(0.1)
#         for rider in riders:
#             rider.turtle.left(30)
    
#     screen.mainloop()

# # Uncomment the line below to run the challenge solution
# challenge_solution()

# """
# STUDENT ASSIGNMENT:

# Welcome to the Turtle Balloon Riders! In this assignment, you'll help different turtle
# characters fly their hot air balloons in the sky. Each turtle gets their own balloon
# in their favorite color!

# BACKGROUND:
# - Each turtle is created as a BalloonRider object
# - When you create a BalloonRider, you give them a color (which will be their balloon color too!)
# - You can then tell each turtle where to fly their balloon using fly_to_position()
# - Watch how each turtle builds their own balloon!
# - After they reach their position, you can make them wave!

# HOW TO CREATE YOUR OWN BALLOON RIDER:
# 1. Create a new BalloonRider object:
#    my_rider = BalloonRider("your_favorite_color")

# 2. Make your rider fly to a position:
#    my_rider.fly_to_position(x, y, balloon_size)
#    - x and y are the coordinates in the sky (try different numbers!)
#    - balloon_size is optional (default is 80)

# 3. Make your rider wave:
#    my_rider.wave()

# YOUR TASKS:

# 1. Look at how the red and blue turtle riders are created and positioned in the example.
#    Watch what happens when you run the program!

# 2. Add at least three more turtle balloon riders to create a scene:
#    - Create each rider with a different color
#    - Position them at different places in the sky
#    - Try different balloon sizes
#    - Make them wave when they reach their position

# 3. For each new balloon rider, you'll need to:
#    - Create them using BalloonRider(color)
#    - Tell them where to fly using fly_to_position(x, y, balloon_size)
#    - Optional: Make them wave using wave()

# 4. Some questions to think about:
#    - How does creating a new BalloonRider create a new turtle?
#    - What happens when you call methods on different riders?
#    - How do the function parameters affect each turtle differently?

# HINTS:
# - Try these colors: "purple", "green", "orange", "pink", "yellow"
# - Experiment with different x, y positions to spread out the balloons
# - Try different balloon_size values to make some bigger or smaller
# - Don't forget to make your turtles wave to each other!

# Challenge: Can you make your turtles "do the wave"? 
#           Make each turtle wave one after the other in a sequence, 
#           creating a wave-like effect across all your balloons!
#           (Ask your teacher for hints about using lists and loops!)
# """

import turtle
import time

class BalloonRider:
    """
    A class representing a turtle character riding in a hot air balloon
    """
    def __init__(self, color):
        """
        Creates a new turtle character with their own balloon
        Parameters:
            color (str): The color of both the turtle and their balloon
        """
        # Create and customize the turtle character
        self.turtle = turtle.Turtle()
        self.turtle.shape("turtle")
        self.turtle.color(color)
        self.balloon_color = color
        
        # Start turtle in default position
        self.turtle.speed(3)  # Slower speed to see movement
        self.turtle.penup()
        self.turtle.goto(0, -200)
        
    def fly_to_position(self, x, y, balloon_size=80):
        """
        Moves the turtle to a position and draws their balloon around them
        Parameters:
            x (int): x-coordinate for balloon center
            y (int): y-coordinate for balloon center
            balloon_size (int): size of the balloon (default 80)
        """
        # Move turtle to starting position to build balloon
        self.turtle.penup()
        self.turtle.goto(x, y)
        
        # Turtle builds their own balloon!
        self.turtle.color(self.balloon_color)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.circle(balloon_size)
        self.turtle.end_fill()
        
        # Draw the ropes
        self.turtle.penup()
        self.turtle.goto(x - 20, y - 60)
        self.turtle.pendown()
        self.turtle.goto(x - balloon_size/2, y + balloon_size)
        
        self.turtle.penup()
        self.turtle.goto(x + 20, y - 60)
        self.turtle.pendown()
        self.turtle.goto(x + balloon_size/2, y + balloon_size)
        
        # Draw the basket
        self.turtle.penup()
        self.turtle.goto(x - 20, y - 100)
        self.turtle.color("brown")
        self.turtle.pendown()
        self.turtle.begin_fill()
        for _ in range(2):
            self.turtle.forward(40)
            self.turtle.left(90)
            self.turtle.forward(48)
            self.turtle.left(90)
        self.turtle.end_fill()
        
        # Move into basket and face upward
        self.turtle.penup()
        self.turtle.goto(x, y - 60)
        self.turtle.setheading(90)
        self.turtle.color(self.balloon_color)
    
    def wave(self):
        """Makes the turtle wave by rotating left and right"""
        for _ in range(10):
            self.turtle.left(30)
            time.sleep(0.2)
            self.turtle.right(60)
            time.sleep(0.2)
            self.turtle.left(30)

def setup_screen():
    """Sets up the turtle screen with a light blue background"""
    screen = turtle.Screen()
    screen.bgcolor("light blue")
    screen.title("Turtle Balloon Riders")
    return screen

def main():
    """
    Main function containing the sequence of drawing commands.
    Students will need to complete this function by creating and positioning
    their turtle balloon riders.
    """
    # Setup screen
    screen = setup_screen()
    
    # Create our first turtle balloon rider as an example
    red_rider = BalloonRider("red")
    red_rider.fly_to_position(-100, 0)
    
    # Create a second turtle balloon rider
    blue_rider = BalloonRider("blue")
    blue_rider.fly_to_position(150, 50)
    
    # Make both turtles wave
    red_rider.wave()
    blue_rider.wave()
    
    # TODO: Students add their own turtle balloon riders here!
    # Example of how to create and position more riders:
    # green_rider = BalloonRider("green")
    # green_rider.fly_to_position(0, 100, balloon_size=100)
    # green_rider.wave()
    
    # Keep the window open
    screen.mainloop()

# if __name__ == "__main__":
#     main()

"""

# Answer key for the challenge: Making all turtles wave at the same time
"""
def challenge_solution():
    screen = setup_screen()
    
    # Create multiple balloon riders
    riders = [
        BalloonRider("red"),
        BalloonRider("blue"),
        BalloonRider("green"),
        BalloonRider("purple"),
        BalloonRider("orange")
    ]
    
    # Position the riders
    positions = [(-150, 0), (-75, 50), (0, 100), (75, 50), (150, 0)]
    for rider, (x, y) in zip(riders, positions):
        rider.fly_to_position(x, y)
    
    # Make riders do the wave in sequence
    for _ in range(3):  # Do the wave 3 times
        for rider in riders:
            # Each rider does one wave motion
            rider.turtle.left(30)
            time.sleep(0.1)
            rider.turtle.right(60)
            time.sleep(0.1)
            rider.turtle.left(30)
            time.sleep(0.1)  # Brief pause before next rider starts
    
    screen.mainloop()

# Uncomment the line below to run the challenge solution
challenge_solution()
"""
STUDENT ASSIGNMENT:

Welcome to the Turtle Balloon Riders! In this assignment, you'll help different turtle
characters fly their hot air balloons in the sky. Each turtle gets their own balloon
in their favorite color!

BACKGROUND:
- Each turtle is created as a BalloonRider object
- When you create a BalloonRider, you give them a color (which will be their balloon color too!)
- You can then tell each turtle where to fly their balloon using fly_to_position()
- Watch how each turtle builds their own balloon!
- After they reach their position, you can make them wave!

HOW TO CREATE YOUR OWN BALLOON RIDER:
1. Create a new BalloonRider object:
   my_rider = BalloonRider("your_favorite_color")

2. Make your rider fly to a position:
   my_rider.fly_to_position(x, y, balloon_size)
   - x and y are the coordinates in the sky (try different numbers!)
   - balloon_size is optional (default is 80)

3. Make your rider wave:
   my_rider.wave()

YOUR TASKS:

1. Look at how the red and blue turtle riders are created and positioned in the example.
   Watch what happens when you run the program!

2. Add at least three more turtle balloon riders to create a scene:
   - Create each rider with a different color
   - Position them at different places in the sky
   - Try different balloon sizes
   - Make them wave when they reach their position

3. For each new balloon rider, you'll need to:
   - Create them using BalloonRider(color)
   - Tell them where to fly using fly_to_position(x, y, balloon_size)
   - Optional: Make them wave using wave()

4. Some questions to think about:
   - How does creating a new BalloonRider create a new turtle?
   - What happens when you call methods on different riders?
   - How do the function parameters affect each turtle differently?

HINTS:
- Try these colors: "purple", "green", "orange", "pink", "yellow"
- Experiment with different x, y positions to spread out the balloons
- Try different balloon_size values to make some bigger or smaller
- Don't forget to make your turtles wave to each other!

Challenge: Can you make your turtles "do the wave" like in a stadium? 
          Make each turtle wave one after another in sequence!
          (hint: use lists and loops!)
"""