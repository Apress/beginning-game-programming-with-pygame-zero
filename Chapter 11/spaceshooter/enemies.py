import sys
import time
import csv
from constants import *
from pgzero.actor import Actor
from asteroid import Asteroid

# Enemies is anything that needs to be destroyed
# Could be an asteroid or a enemy fighter etc.

class Enemies:

    def __init__(self, screen_size, configfile):
        self.screen_size = screen_size
        self.asteroids = []
        # Time that this level started
        self.level_time = time.time()
        self.level_end = None
        # Load the config file
        try:
            with open(configfile, 'r') as file:
                csv_reader = csv.reader(file)
                for enemy_details in csv_reader:
                    if enemy_details[1] == "end":
                        self.level_end = float(enemy_details[0])
                    elif enemy_details[1] == "asteroid":
                        start_time = float(enemy_details[0])
                        # value 1 is type
                        image = enemy_details[2]
                        start_pos = (int(enemy_details[3]),
                            int(enemy_details[4]))
                        velocity = float(enemy_details[5])
                        self.asteroids.append(Asteroid(start_time, image, start_pos, velocity))
        except IOError:
            print ("Error reading configuration file "+configfile)
            # Just end as cannot play without config file
            sys.exit()
        except:
            print ("Corrupt configuration file "+configfile)
            sys.exit()


    # Next level reset time
    def next_level (self):
        self.level_time = time.time()
        for this_asteroid in self.asteroids:
            this_asteroid.reset()

    def reset (self):
        self.level_time = time.time()
        for this_asteroid in self.asteroids:
            this_asteroid.reset()
    # Updates positions of all enemies
    def update(self, time_interval):
        # Check for level end reached
        if (self.level_end != None and
            time.time() > self.level_time + self.level_end):
                self.next_level()

        for this_asteroid in self.asteroids:
            this_asteroid.update(self.level_time, time_interval)


    # Draws all active enemies on the screen
    def draw(self, screen):
        for this_asteroid in self.asteroids:
            this_asteroid.draw()

    # Check if a shot hits something - return True if hit
    # otherwise return False
    def check_shot(self, shot):
        # check for any visible objects colliding with shot
        for this_asteroid in self.asteroids:
            # skip any that are not visible
            if this_asteroid.status != STATUS_VISIBLE:
                continue
            if (this_asteroid.colliderect(shot)):
                this_asteroid.hit()
                return True
        return False

    # Check if crashed - return True if crashed
    # otherwise return False
    def check_crash(self, spacecraft, collide_points=None):
        for this_asteroid in self.asteroids:
            # skip any that are not visible
            if this_asteroid.status != STATUS_VISIBLE:
                continue
            # Crude detection based on rectangles
            if (this_asteroid.colliderect(spacecraft)):
                # More accurate detection, but more time consuming
                # (optional if collide_points default to None)
                if (collide_points == None):
                    this_asteroid.status = STATUS_DESTROYED
                    return True
                for this_point in collide_points:
                    if this_asteroid.collidepoint(
                        spacecraft.x+this_point[0],
                        spacecraft.y+this_point[1] ):
                            this_asteroid.status = STATUS_DESTROYED
                            return True
        return False