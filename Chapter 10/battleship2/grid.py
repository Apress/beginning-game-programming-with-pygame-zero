import math

class Grid:

    # Grid dimensions are in terms of screen pixels
    # Tools to convert between different values are
    # included as static methods
    def __init__ (self, start_grid, grid_size):
        self.start_grid = start_grid
        self.grid_size = grid_size

    # Does co-ordinates match this grid
    def check_in_grid (self, screen_pos):
        if (screen_pos[0] < self.start_grid[0] or
            screen_pos[1] < self.start_grid[1] or
            screen_pos[0] > self.start_grid[0] + (self.grid_size[0] * 10) or
            screen_pos[1] > self.start_grid[1] + (self.grid_size[1] * 10)):
                return False
        else:
            return True

    def get_grid_pos (self, screen_pos):
        x_offset = screen_pos[0] - self.start_grid[0]
        x = math.floor(x_offset / self.grid_size[0])
        y_offset = screen_pos[1] - self.start_grid[1]
        y = math.floor(y_offset / self.grid_size[1])
        if (x < 0 or y < 0 or x > 9 or y > 9):
            return None
        return (x,y)

    # Gets top left of a grid position - returns as screen position
    def grid_pos_to_screen_pos (self, grid_pos):
        x = self.start_grid[0] + (grid_pos[0] * self.grid_size[0])
        y = self.start_grid[1] + (grid_pos[1] * self.grid_size[1])
        return (x,y)