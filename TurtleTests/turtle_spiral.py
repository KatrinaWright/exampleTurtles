import unittest
from unittest.mock import Mock, patch

import turtle
from PIL import Image
import math
import os

class SpiralGenerator:
    
    def __init__(self, t=None):
        self.t = t or turtle.Turtle()
        self.screen = self.t.getscreen()
    
    def draw_spiral(self, size=100, color_change=False):
        self.t.penup()
        self.t.goto(0, 0)
        self.t.pendown()
        
        for angle in range(0, 360*3, 5):
            # Calculate radius based on angle
            radius = size * angle/(360*2)
            
            # Calculate position
            x = radius * math.cos(math.radians(angle))
            y = radius * math.sin(math.radians(angle))
            
            # Change color if enabled
            if color_change:
                hue = angle % 360 / 360.0
                self.pencolor(self._hsv_to_rgb(hue, 1.0, 1.0))
            
            self.t.goto(x, y)
    
    def draw_and_save(self, filename, size=100):
        # Clear any existing drawing
        self.t.clear()
        
        # Hide turtle and set up screen
        self.t.hideturtle()
        self.screen.tracer(0)
        
        # Draw the spiral
        self.draw_spiral(size)
        
        # Update screen and save
        self.screen.update()
        self.screen.getcanvas().postscript(file='temp.eps')
        
        # Convert to PNG
        img = Image.open('temp.eps')
        img.save(filename, 'PNG')
        os.remove('temp.eps')
    
    def _hsv_to_rgb(self, h, s, v):
        if s == 0.0:
            return (v, v, v)
        
        i = int(h * 6.0)
        f = (h * 6.0) - i
        p = v * (1.0 - s)
        q = v * (1.0 - s * f)
        t = v * (1.0 - s * (1.0 - f))
        i = i % 6
        
        if i == 0: return (v, t, p)
        if i == 1: return (q, v, p)
        if i == 2: return (p, v, t)
        if i == 3: return (p, q, v)
        if i == 4: return (t, p, v)
        if i == 5: return (v, p, q)

def main():
    print("turtle_spiral.py was accessed!")
    actual_turtle = turtle.Turtle()
    mock_turtle = Mock()
    spiral = SpiralGenerator(t=actual_turtle)

    mock_turtle.spiral.draw_spiral(size=100)
    actual_turtle.mock_turtle.penup.assert_called_once()
    actual_turtle.mock_turtle.goto.assert_called_with(0, 0)
    actual_turtle.mock_turtle.pendown.assert_called_once()

# main()