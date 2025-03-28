import unittest
from turtle import Screen, Turtle
from maze_solverb import MazeSolver
import time

class TestMazeSolver(unittest.TestCase):
    def setUp(self):
        self.screen = Screen()
        self.screen.setup(400, 400)
        self.solver = MazeSolver()

    def test_maze_generation(self):
        self.solver.generate_maze()
        # Capture the screen state
        self.screen.update()
        ps = self.screen.getcanvas().postscript(file="maze.eps")
        
        # Check if the file was created (indicating drawing occurred)
        import os
        self.assertTrue(os.path.exists("maze.eps"))
        
        # Basic check for maze complexity
        with open("maze.eps", "r") as f:
            content = f.read()
            # Check for multiple line segments (indicating walls)
            self.assertGreater(content.count("lineto"), 10)

    def tearDown(self):
        self.screen.clear()
        self.screen.bye()
    """ # Second Iteration test '"""
    def test_solve_maze(self):
        self.solver.generate_maze()
        start_time = time.time()
        path = self.solver.solve_maze()
        end_time = time.time()

        # Check if a path was found
        self.assertIsNotNone(path)
        
        # Check if the path reaches the bottom of the maze
        self.assertGreaterEqual(path[-1][1], -180)

        # Check solving time
        solving_time = end_time - start_time
        self.assertLess(solving_time, 5)  # Should solve in less than 5 seconds
    """ """

if __name__ == '__main__':
    unittest.main()
