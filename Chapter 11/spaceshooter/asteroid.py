from pgzero.actor import Actor
import time
from constants import *

class Asteroid(Actor):

    def __init__ (self, start_time, image, start_pos, velocity):
        Actor.__init__(self, image, (start_pos))
        self.start_pos = start_pos
        self.start_time = start_time
        self.velocity = velocity
        self.status = STATUS_WAITING

    def update(self, level_time, time_interval):
        if self.status == STATUS_WAITING:
            # Check if time reached
            if (time.time() > level_time + self.start_time):
                # Reset to start position
                self.x = self.start_pos[0]
                self.y = self.start_pos[1]
                self.status = STATUS_VISIBLE
        elif self.status == STATUS_VISIBLE:
            self.y+=self.velocity * 60 * time_interval

    def reset(self):
        self.status = STATUS_WAITING

    def draw(self):
        if self.status == STATUS_VISIBLE:
            Actor.draw(self)

    def hit(self):
        self.status = STATUS_DESTROYED