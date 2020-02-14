import math
from grid import Grid
from ship import Ship
from shot import Shot

class Fleet:

    def __init__ (self, start_grid, grid_size):
        self.start_grid = start_grid
        self.grid_size = grid_size
        self.ships = []
        self.grid = Grid(start_grid, grid_size)
        self.shots = []

    # Is there a ship at this position that has sunk
    def is_ship_sunk_grid_pos (self, check_grid_pos):
        # find ship at that position
        for this_ship in self.ships:
            if (this_ship.includes_grid_pos(check_grid_pos)):
                return this_ship.is_sunk()
        # If there is no ship at this position then return False
        return False

    def add_ship (self, type, position, direction, hidden=False):
        self.ships.append(Ship(type, self.grid, position, direction, hidden))

    # check through ships to see if any still floating
    def all_sunk (self):
        for this_ship in self.ships:
            if not this_ship.is_sunk():
                return False
        return True

    # Draws entire fleet (each of the ships)
    def draw(self):
        for this_ship in self.ships:
            this_ship.draw()
        for this_shot in self.shots:
            this_shot.draw()

    def fire (self, pos):
        # Is this a hit
        for this_ship in self.ships:
            if (this_ship.fire(pos)):
                # Hit
                self.shots.append(Shot("hit",self.grid.grid_pos_to_screen_pos(pos)))
                #check if this ship sunk
                if this_ship.is_sunk():
                    # Ship sunk so make it visible
                    this_ship.hidden = False
                return True
        self.shots.append(Shot("miss",self.grid.grid_pos_to_screen_pos(pos)))
        return False

    def reset(self):
        self.ships = []
        self.shots = []