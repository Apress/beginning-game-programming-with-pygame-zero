import random
from grid import Grid

# Provides Ai Player
class Ai:

    NA = 0
    MISS = 1
    HIT = 2

    def __init__ (self):
        # Create 2 dimension list with no shots fired
        # access using [x value][y value]
        # Pre-populate with NA
        self.shots = [ [Ai.NA for y in range(10)] for x in range(10) ]
        # Hit ship is the position of the first successful hit on a ship
        self.hit_ship = None

    def fire_shot(self):
        # If not targetting hit ship
        if (self.hit_ship == None):
            return (self.get_random())
        else:
            # Have scored a hit - so find neighbouring positions
            # copy hit_ship into separate values to make easier to follow
            hit_x = self.hit_ship[0]
            hit_y = self.hit_ship[1]
            # Try horizontal if not at edge
            if (hit_x < 9):
                for x in range (hit_x+1,10):
                    if (self.shots[x][hit_y] == Ai.NA):
                        return (x,hit_y)
                    if (self.shots[x][hit_y] == Ai.MISS):
                        break
            if (hit_x > 0):
                for x in range (hit_x-1,-1, -1):
                    if (self.shots[x][hit_y] == Ai.NA):
                        return (x,hit_y)
                    if (self.shots[x][hit_y] == Ai.MISS):
                        break
            if (hit_y < 9):
                for y in range (hit_y+1,10):
                    if (self.shots[hit_x][y] == Ai.NA):
                        return (hit_x,y)
                    if (self.shots[hit_x][y] == Ai.MISS):
                        break
            if (hit_y > 0):
                for y in range (hit_y-1,-1, -1):
                    if (self.shots[hit_x][y] == Ai.NA):
                        return (hit_x,y)
                    if (self.shots[hit_x][y] == Ai.MISS):
                        break
            # Catch all - shouldn't get this, but just in case guess random
            return (self.get_random())

    def fire_result(self, grid_pos, result):
        x_pos = grid_pos[0]
        y_pos = grid_pos[1]
        if (result == True):
            result_value = Ai.HIT
            if (self.hit_ship == None):
                self.hit_ship = grid_pos
        else:
            result_value = Ai.MISS
        self.shots[x_pos][y_pos] = result_value

    def get_random(self):
        # Copy only non used positions into a temporary list
        non_shots = []
        for x_pos in range (0,10):
            for y_pos in range (0,10):
                if self.shots[x_pos][y_pos] == Ai.NA:
                    non_shots.append((x_pos,y_pos))
        return random.choice(non_shots)

    # Let Ai know that the last shot sunk a ship
    # list_pos is provided, but not currently used
    def ship_sunk(self, grid_pos):
        # reset hit ship
        self.hit_ship = None