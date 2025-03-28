import unittest
from unittest.mock import Mock, patch
import math
from turtle_spiral import SpiralGenerator
import os
from PIL import Image, ImageDraw

############################################################################
# ITERATION 1: Testing Basic Turtle Movement
# Strategy: Mock the turtle and verify correct movement commands are called
############################################################################

class TestSpiralGenerator_Movement(unittest.TestCase):
    def setUp(self):
        self.mock_turtle = Mock()
        self.spiral = SpiralGenerator(t=self.mock_turtle)
    
    def test_spiral_starts_at_center(self):
        """Verify the spiral starts drawing from (0,0)"""
        self.spiral.draw_spiral(size=100)
        self.mock_turtle.penup.assert_called_once()
        self.mock_turtle.goto.assert_called_with(0, 0)
        self.mock_turtle.pendown.assert_called_once()

    def test_spiral_moves_in_circular_pattern(self):
        """Verify the spiral makes circular movements"""
        self.spiral.draw_spiral(size=50)
        # Get all the goto calls
        goto_calls = [call[0] for call in self.mock_turtle.goto.call_args_list]
        
        # Verify points form a growing spiral pattern
        prev_distance = 0
        for x, y in goto_calls:
            current_distance = math.sqrt(x*x + y*y)
            self.assertGreater(current_distance, prev_distance)
            prev_distance = current_distance

############################################################################
# ITERATION 2: Testing Color Changes
# Strategy: Verify color changes based on position in spiral
############################################################################

# class TestSpiralGenerator_Colors(unittest.TestCase):
#     def setUp(self):
#         self.mock_turtle = Mock()
#         self.spiral = SpiralGenerator(t=self.mock_turtle)
    
#     def test_color_changes_with_angle(self):
#         """Verify color changes as spiral rotates"""
#         self.spiral.draw_spiral(size=50, color_change=True)
        
#         # Check that pencolor was called multiple times with different values
#         pencolor_calls = self.mock_turtle.pencolor.call_args_list
#         self.assertGreater(len(pencolor_calls), 1)
#         # Verify colors are different
#         colors = [call[0][0] for call in pencolor_calls]
#         self.assertGreater(len(set(colors)), 1)

############################################################################
# ITERATION 3: Testing Image Output
# Strategy: Generate actual image file and verify its properties
############################################################################

# class TestSpiralGenerator_Output(unittest.TestCase):
#     def setUp(self):
#         self.spiral = SpiralGenerator()
#         self.output_path = "test_spiral.png"

#     def tearDown(self):
#         # Clean up generated test files
#         if os.path.exists(self.output_path):
#             os.remove(self.output_path)

#     def test_save_generates_valid_image(self):
#         """Verify that saving produces a valid image file"""
#         self.spiral.draw_and_save(self.output_path, size=100)
        
#         # Verify file exists and is an image
#         self.assertTrue(os.path.exists(self.output_path))
#         img = Image.open(self.output_path)
#         self.assertEqual(img.format, 'PNG')

#     def test_image_contains_spiral_pattern(self):
#         """Verify the generated image contains non-white pixels in a spiral pattern"""
#         self.spiral.draw_and_save(self.output_path, size=100)
        
#         img = Image.open(self.output_path)
#         pixels = img.load()
        
#         # Check points along expected spiral path
#         found_drawn_pixels = False
#         center_x, center_y = img.size[0]//2, img.size[1]//2
        
#         for radius in range(10, 50, 10):
#             for angle in range(0, 360, 45):
#                 x = center_x + int(radius * math.cos(math.radians(angle)))
#                 y = center_y + int(radius * math.sin(math.radians(angle)))
#                 if 0 <= x < img.size[0] and 0 <= y < img.size[1]:
#                     if pixels[x, y] != (255, 255, 255):  # not white
#                         found_drawn_pixels = True
#                         break
        
#         self.assertTrue(found_drawn_pixels)