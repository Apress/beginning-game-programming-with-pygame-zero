from pgzero.actor import Actor

class SpaceShip(Actor):

    def set_speed (self, movement_speed):
        self.movement_speed = movement_speed

    def move (self, direction):
        if (direction == "up"):
            self.y -= self.movement_speed
        elif (direction == "down"):
            self.y += self.movement_speed
        elif (direction == "left"):
            self.x -= self.movement_speed
        elif (direction == "right"):
            self.x += self.movement_speed
        # Make sure that the ship remains on the screen
        if self.x < 20:
            self.x = 20
        if self.x > 780:
            self.x = 780
        if self.y < 20:
            self.y = 20
        if self.y > 580:
            self.y = 580
