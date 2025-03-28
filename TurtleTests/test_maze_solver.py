# test_maze_solver.py
import unittest
from unittest.mock import Mock, patch
from maze_solver import MazeSolver
import turtle
import time
from io import StringIO

class TestMazeSolver(unittest.TestCase):
    def setUp(self):
        # Create a mock screen and turtle for testing
        self.mock_screen = Mock()
        self.mock_turtle = Mock()
        # Patch turtle.Screen() and turtle.Turtle() to return our mocks
        self.screen_patcher = patch('turtle.Screen', return_value=self.mock_screen)
        self.turtle_patcher = patch('turtle.Turtle', return_value=self.mock_turtle)
        self.screen_patcher.start()
        self.turtle_patcher.start()
        
        # Create our maze solver instance
        self.maze_solver = MazeSolver()

    def tearDown(self):
        self.screen_patcher.stop()
        self.turtle_patcher.stop()

    ############################################################################
    # ITERATION 1: Basic Setup and Initialization
    ############################################################################
    
    def test_maze_solver_initialization(self):
        """Test that the maze solver initializes with correct default values"""
        self.assertIsNotNone(self.maze_solver.turtle)
        self.assertIsNotNone(self.maze_solver.screen)
        self.assertEqual(self.maze_solver.cell_size, 20)
        self.assertEqual(self.maze_solver.maze_size, (10, 10))

    def test_setup_screen_configuration(self):
        """Test that the screen is configured correctly"""
        # Verify screen setup was called with correct dimensions
        expected_width = self.maze_solver.maze_size[0] * self.maze_solver.cell_size * 2
        expected_height = self.maze_solver.maze_size[1] * self.maze_solver.cell_size * 2
        self.mock_screen.setup.assert_called_with(expected_width, expected_height)
        
    # ############################################################################
    # # ITERATION 2: Maze Generation
    # ############################################################################

    def test_draw_cell_wall(self):
        """Test that drawing a wall cell uses correct turtle commands"""
        self.maze_solver.draw_cell(0, 0, is_wall=True)
        
        # Verify turtle commands for wall cell
        self.mock_turtle.penup.assert_called()
        self.mock_turtle.goto.assert_called()
        self.mock_turtle.fillcolor.assert_called_with('black')
        self.mock_turtle.begin_fill.assert_called()
        self.mock_turtle.end_fill.assert_called()

    def test_draw_path_cell(self):
        """Test that drawing a path cell uses correct turtle commands"""
        self.maze_solver.draw_cell(0, 0, is_wall=False)
        
        # Verify turtle commands for path cell
        self.mock_turtle.fillcolor.assert_called_with('white')

    # def test_generate_maze_boundaries(self):
    #     """Test that maze generation creates proper boundaries"""
    #     self.maze_solver.generate_maze()
        
    #     # Verify outer walls exist
    #     maze = self.maze_solver.maze
    #     self.assertTrue(all(maze[0][j] for j in range(len(maze[0]))))  # Top wall
    #     self.assertTrue(all(maze[-1][j] for j in range(len(maze[-1]))))  # Bottom wall
    #     self.assertTrue(all(maze[i][0] for i in range(len(maze))))  # Left wall
    #     self.assertTrue(all(maze[i][-1] for i in range(len(maze))))  # Right wall

    # ############################################################################
    # # ITERATION 3: Path Finding
    # ############################################################################

    def test_find_path_exists(self):
        """Test that a path can be found in a simple maze"""
        # Create a simple test maze with known path
        test_maze = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]
        ]
        self.maze_solver.maze = test_maze
        path = self.maze_solver.find_path((1, 1), (3, 1))
        self.assertIsNotNone(path)
        self.assertTrue(len(path) > 0)

    def test_find_path_no_solution(self):
        """Test behavior when no path exists"""
        # Create a test maze with no possible path
        test_maze = [
            [1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1]
        ]
        self.maze_solver.maze = test_maze
        path = self.maze_solver.find_path((1, 1), (3, 1))
        self.assertIsNone(path)

    # ############################################################################
    # # ITERATION 4: Solution Visualization
    # ############################################################################

    def test_visualize_solution_path(self):
        """Test that solution path is visualized correctly"""
        test_path = [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3)]
        self.maze_solver.visualize_solution(test_path)
        
        # Verify turtle commands for path visualization
        self.mock_turtle.penup.assert_called()
        self.mock_turtle.pendown.assert_called()
        self.mock_turtle.pencolor.assert_called_with('green')
        # Verify goto was called for each path point
        self.assertEqual(self.mock_turtle.goto.call_count, len(test_path))

    def test_solving_time_tracking(self):
        """Test that solving time is tracked and displayed"""
        with patch('time.time') as mock_time:
            # Simulate 2.5 seconds passing
            mock_time.side_effect = [0, 2.5]
            self.maze_solver.solve_maze()
            
            # Verify time tracking
            self.assertAlmostEqual(self.maze_solver.solving_time, 2.5)
            # Verify time display
            self.mock_turtle.write.assert_called()

    # ############################################################################
    # # ITERATION 5: Performance and Edge Cases
    # ############################################################################

    def test_large_maze_performance(self):
        """Test that large mazes can be handled efficiently"""
        original_size = self.maze_solver.maze_size
        self.maze_solver.maze_size = (20, 20)
        
        start_time = time.time()
        self.maze_solver.generate_maze()
        end_time = time.time()
        
        # Assert generation takes less than 1 second
        self.assertLess(end_time - start_time, 1.0)
        
        # Reset maze size
        self.maze_solver.maze_size = original_size

    def test_invalid_start_end_points(self):
        """Test handling of invalid start/end points"""
        with self.assertRaises(ValueError):
            self.maze_solver.find_path((-1, -1), (5, 5))
        
        with self.assertRaises(ValueError):
            self.maze_solver.find_path((1, 1), (100, 100))