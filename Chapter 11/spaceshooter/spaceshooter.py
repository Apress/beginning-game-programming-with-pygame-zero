import time
import sys
from constants import *
from spaceship import SpaceShip
from player import Player
from shot import Shot
from enemies import Enemies

WIDTH=800
HEIGHT=600
TITLE="Space shooter game"
ICON="spacecrafticon.png"

scroll_speed = 2

player = Player()

spacecraft = SpaceShip("spacecraft", (400,480))
spacecraft.set_speed(4)

enemies = Enemies((WIDTH,HEIGHT), "enemies.dat")

# List to track shots
shots = []
# shot last fired  timestamp - to ensure don't fire too many shots
shot_last_fired = 0
# time in seconds
time_between_shots = 0.5

scroll_position = 0

# spacecraft hit points
# positions relative to spacecraft centre which classes as a collide
spacecraft_hit_pos = [
    (0,-40), (10,-30), (-10,-30), (13,-15), (-13,-15), (25,-3), (-25,-3),
    (46,12), (-46,12), (25,24), (-25,24), (10,27), (-10,27), (0,27) ]

# Status
# "start" = Press fire to start
# "game" = Game in progress
# "gameover" = Game Over
status = "start"

# value for waiting when asking for option
wait_timer = 0

def draw ():
    # Scrolling background
    screen.blit("background", (0,scroll_position-600))
    screen.blit("background", (0,scroll_position))

    enemies.draw(screen)

    spacecraft.draw()
    # Shots
    for this_shot in shots:
        this_shot.draw()

    screen.draw.text("Score: {}".format(player.score), fontname="computerspeak", fontsize=40, topleft=(30,30), color=(255,255,255))
    screen.draw.text("Lives: {}".format(player.lives), fontname="computerspeak", fontsize=40, topright=(770,30), color=(255,255,255))

    if status == "start" or status == "start-wait":
        screen.draw.text("Press fire to start game", fontname="computerspeak", fontsize=40, center=(400,300), color=(255,255,255))
    elif status == "gameover" or status == "gameover-wait":
        screen.draw.text("Game Over", fontname="computerspeak", fontsize=40, center=(400,200), color=(255,255,255))


def update(time_interval):
    global status, scroll_position, shot_last_fired, wait_timer
    # Allow Escape to quit straight out of the game regardless of state of the game
    if keyboard.escape:
        sys.exit()
    # Wait on fire key press to start game
    if status == "start":
        # start timer
        wait_timer = time.time() + DELAY_TIME
        status = "start-wait"
    if status == "start-wait":
        if (time.time() < wait_timer):
            return
        if keyboard.space or keyboard.lshift:
            player.reset()
            enemies.reset()
            status = "game"
    elif status == "gameover":
        # start timer
        wait_timer = time.time() + DELAY_TIME
        status = "gameover-wait"
    elif status == "gameover-wait":
        if (time.time() < wait_timer):
            return
        if keyboard.space or keyboard.lshift:
            status = "start"
    elif status == "game":
        # Scroll screen
        scroll_position += scroll_speed
        if (scroll_position >= 600):
            scroll_position = 0

        # Update existing shots
        for this_shot in shots:
            # Update position of shot
            this_shot.update(time_interval)
            if this_shot.y <= 0:
                shots.remove(this_shot)
            # Check if hit asteroid or enemy
            elif enemies.check_shot(this_shot):
                player.score += 10
                # remove shot (otherwise it continues to hit others)
                shots.remove(this_shot)
                sounds.asteroid_explode.play()

        if enemies.check_crash(spacecraft, spacecraft_hit_pos):
            player.lives -= 1
            if player.lives < 1:
                status = "gameover"
                return
            else:
                sounds.space_crash.play()

        # Update enemies after checking for a shot hit
        enemies.update(time_interval)

        # Handle keyboard
        if keyboard.up:
            spacecraft.move("up")
        if keyboard.down:
            spacecraft.move("down")
        if keyboard.left:
            spacecraft.move("left")
        if keyboard.right:
            spacecraft.move("right")
        if keyboard.space or keyboard.lshift:
            # check if time since last shot reached
            if (time.time() > shot_last_fired + time_between_shots):
                # rest time last fired
                shot_last_fired = time.time()
                shots.append(Shot("shot",(spacecraft.x,spacecraft.y-25)))
                # Play sound of gun firing
                sounds.space_gun.play()