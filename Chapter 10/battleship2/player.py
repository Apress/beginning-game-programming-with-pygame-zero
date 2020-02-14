import random
from grid import Grid

# Provides Ai Player
class Player:

    NA = 0
    MISS = 1
    HIT = 2

    def __init__ (self):
        # Own grid for positioning own ships
        # Set to hit where a ship is positioned
        self.owngrid = [ [Player.NA for y in range(10)] for x in range(10) ]

    def check_ship_fit (self, ship_size, direction, start_pos):
        #print ("Checking {} {} {}".format(ship_size, direction, start_pos))
        if (direction == "horizontal"):
            # Check if it won't fit on the grid
            # -1 as start_pos is included in the size
            if ((start_pos[0] + ship_size -1) > 9):
                return False
            # check that there are no ships in the way
            # range goes to one less than max size - so no need for the -1
            for x_pos in range(start_pos[0],start_pos[0]+ship_size):
                if (self.owngrid[x_pos][start_pos[1]] == Player.HIT):
                    return False
            return True
        # Otherwise vertical
        else:
            # Check if it won't fit on the grid
            # -1 as start_pos is included in the size
            if ((start_pos[1] + ship_size -1) > 9):
                return False
            # check that there are no ships in the way
            # range goes to one less than max size - so no need for the -1
            for y_pos in range (start_pos[1],start_pos[1]+ship_size):
                if (self.owngrid[start_pos[0]][y_pos] == Player.HIT):
                    return False
            return True

    # Place ship is used during ship placement
    # Updates grid with location of ship
    def place_ship (self, ship_size, direction, start_pos):
        if (direction == "horizontal"):
            for x_pos in range (start_pos[0],start_pos[0]+ship_size):
                self.owngrid[x_pos][start_pos[1]] = Player.HIT
        # otherwise vertical
        else:
            for y_pos in range (start_pos[1],start_pos[1]+ship_size):
                self.owngrid[start_pos[0]][y_pos] = Player.HIT

    def reset(self):
        self.owngrid = [ [Player.NA for y in range(10)] for x in range(10) ]