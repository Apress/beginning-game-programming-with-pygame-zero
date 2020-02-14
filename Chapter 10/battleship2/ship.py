from pgzero.actor import Actor
from grid import Grid

# Ship is referred to using an x,y position

class Ship (Actor):

    def __init__ (self, ship_type, grid, grid_pos, direction, hidden=False):
        Actor.__init__(self, ship_type, (10,10))
        self.ship_type = ship_type
        self.grid = grid
        self.image = ship_type
        self.grid_pos = grid_pos
        self.topleft = self.grid.grid_pos_to_screen_pos((grid_pos))
        # Set the actor anchor position to centre of the first square
        self.anchor = (38/2, 38/2)
        self.direction = direction
        if (direction == 'vertical'):
            self.angle = -90
        self.hidden = hidden
        if (ship_type == "destroyer"):
            self.ship_size = 2
            self.hits = [False, False]
        elif (ship_type == "cruiser"):
            self.ship_size = 3
            self.hits = [False, False, False]
        elif (ship_type == "submarine"):
            self.ship_size = 3
            self.hits = [False, False, False]
        elif (ship_type == "battleship"):
            self.ship_size = 4
            self.hits = [False, False, False, False]
        elif (ship_type == "carrier"):
            self.ship_size = 5
            self.hits = [False, False, False, False, False]

    def draw(self):
        if (self.hidden):
            return
        Actor.draw(self)

    def is_sunk (self):
        if (False in self.hits):
            return False
        return True

    def fire (self, fire_grid_pos):
        if self.direction == 'horizontal':
            if (fire_grid_pos[0] >= self.grid_pos[0] and
                fire_grid_pos[0] < self.grid_pos[0]+self.ship_size and
                fire_grid_pos[1] == self.grid_pos[1]):
                self.hits[fire_grid_pos[0]-self.grid_pos[0]] = True
                return True
        else:
            if (fire_grid_pos[0] == self.grid_pos[0] and
                fire_grid_pos[1] >= self.grid_pos[1] and
                fire_grid_pos[1] < self.grid_pos[1]+self.ship_size):
                self.hits[fire_grid_pos[1]-self.grid_pos[1]] = True
                return True
        return False

    # Does this ship cover this grid_position
    def includes_grid_pos (self, check_grid_pos):
        # If first pos then return True
        if (self.grid_pos == check_grid_pos):
            return True
        # check x axis
        elif (self.direction == 'horizontal' and
            self.grid_pos[1] == check_grid_pos[1] and
            check_grid_pos[0] >= self.grid_pos[0] and
            check_grid_pos[0] < self.grid_pos[0] + self.ship_size):
            return True
        elif (self.direction == 'vertical' and
            self.grid_pos[0] == check_grid_pos[0] and
            check_grid_pos[1] >= self.grid_pos[1] and
            check_grid_pos[1] < self.grid_pos[1] + self.ship_size):
            return True
        else :
            return False