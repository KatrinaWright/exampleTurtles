import turtle
import random
import time

class MazeSolvera:
    def __init__(self):
        self.screen = turtle.Screen()
        self.turtle = turtle.Turtle()
        self.cell_size = 20
        self.maze_size = (10, 10)
        self.maze = None
        self.solving_time = 0
        self._setup_screen()
        
    def _setup_screen(self):
        """Configure the turtle screen"""
        width = self.maze_size[0] * self.cell_size * 2
        height = self.maze_size[1] * self.cell_size * 2
        self.screen.setup(width, height)
        self.screen.title("Maze Solver")
        self.turtle.speed(0)  # Fastest drawing speed
        self.screen.tracer(0)  # Turn off animation for faster drawing
        
    def draw_cell(self, x, y, is_wall=False):
        """Draw a single cell of the maze"""
        self.turtle.penup()
        screen_x = (x - self.maze_size[0]/2) * self.cell_size
        screen_y = (y - self.maze_size[1]/2) * self.cell_size
        self.turtle.goto(screen_x, screen_y)
        
        self.turtle.fillcolor('black' if is_wall else 'white')
        self.turtle.begin_fill()
        for _ in range(4):
            self.turtle.forward(self.cell_size)
            self.turtle.left(90)
        self.turtle.end_fill()
        
    def generate_maze(self):
        """Generate a random maze"""
        self.maze = [[1 for _ in range(self.maze_size[0])] 
                    for _ in range(self.maze_size[1])]
        
        # Generate paths using recursive backtracking
        def carve_path(x, y):
            self.maze[y][x] = 0
            directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
            random.shuffle(directions)
            
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if (0 <= new_x < self.maze_size[0] and 
                    0 <= new_y < self.maze_size[1] and 
                    self.maze[new_y][new_x] == 1):
                    self.maze[y + dy//2][x + dx//2] = 0
                    carve_path(new_x, new_y)
        
        # Start from the center
        start_x = self.maze_size[0] // 2
        start_y = self.maze_size[1] // 2
        carve_path(start_x, start_y)
        
        # Draw the maze
        for y in range(self.maze_size[1]):
            for x in range(self.maze_size[0]):
                self.draw_cell(x, y, self.maze[y][x] == 1)
        self.screen.update()
        
    def find_path(self, start, end):
        """Find a path from start to end using BFS"""
        if not self._is_valid_point(start) or not self._is_valid_point(end):
            raise ValueError("Invalid start or end point")
            
        queue = [(start, [start])]
        visited = {start}
        
        while queue:
            (x, y), path = queue.pop(0)
            if (x, y) == end:
                return path
                
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                next_x, next_y = x + dx, y + dy
                if (self._is_valid_point((next_x, next_y)) and 
                    self.maze[next_y][next_x] == 0 and 
                    (next_x, next_y) not in visited):
                    queue.append(((next_x, next_y), path + [(next_x, next_y)]))
                    visited.add((next_x, next_y))
        return None
        
    def _is_valid_point(self, point):
        """Check if a point is within maze bounds"""
        x, y = point
        return (0 <= x < self.maze_size[0] and 
                0 <= y < self.maze_size[1])
        
    def visualize_solution(self, path):
        """Visualize the solution path"""
        if not path:
            return
            
        self.turtle.penup()
        self.turtle.pensize(2)
        self.turtle.pencolor('green')
        
        # Move to start
        x, y = path[0]
        screen_x = (x - self.maze_size[0]/2) * self.cell_size + self.cell_size/2
        screen_y = (y - self.maze_size[1]/2) * self.cell_size + self.cell_size/2
        self.turtle.goto(screen_x, screen_y)
        
        self.turtle.pendown()
        for x, y in path[1:]:
            screen_x = (x - self.maze_size[0]/2) * self.cell_size + self.cell_size/2
            screen_y = (y - self.maze_size[1]/2) * self.cell_size + self.cell_size/2
            self.turtle.goto(screen_x, screen_y)
        self.screen.update()
        
    def solve_maze(self):
        """Main method to solve the maze"""
        self.generate_maze()
        start_time = time.time()
        
        # Find path from top-left to bottom-right (excluding walls)
        start = (1, 1)
        end = (self.maze_size[0]-2, self.maze_size[1]-2)
        path = self.find_path(start, end)
        
        self.solving_time = time.time() - start_time
        
        if path:
            self.visualize_solution(path)
            # Display solving time
            self.turtle.penup()
            self.turtle.goto(-self.maze_size[0] * self.cell_size / 2,
                           -self.maze_size[1] * self.cell_size / 2 - 20)
            self.turtle.write(f"Solved in {self.solving_time:.2f} seconds",
                            align="left", font=("Arial", 12, "normal"))
        else:
            self.turtle.write("No solution found!", align="center",
                            font=("Arial", 14, "bold"))
        self.screen.update()

# if __name__ == "__main__":
#     solver = MazeSolver()
#     solver.solve_maze()
#     turtle.done()
