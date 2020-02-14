import random
import pygame

WIDTH=800
HEIGHT=600

SKY_COLOR = (165, 182, 209)
GROUND_COLOR = (9,84,5)  

# How big a chunk to split up x axis
LAND_CHUNK_SIZE = 20
# Max that land can go up or down within chunk size
LAND_MAX_CHG = 20
# Max height of ground
LAND_MIN_Y = 200

# Position of the two tanks - set to zero, update before use
left_tank_position = (0,0)
right_tank_position = (0,0)
    
def draw():
    screen.fill(SKY_COLOR)
    pygame.draw.polygon(screen.surface, GROUND_COLOR, land_positions)

# Setup game - allows create new game    
def setup():
    global left_tank_position, right_tank_position, land_positions
    # Setup landscape (these positions represent left side of platform)
    # Choose a random position
    # The complete x,y co-ordinates will be saved in a 
    # tuple in left_tank_rect and right_tank_rect
    left_tank_x_position = random.randint (10,300)
    right_tank_x_position = random.randint (500,750)
    
    # Sub divide screen into chunks for the landscape
    # store as list of x positions (0 is first position)
    current_land_x = 0
    current_land_y = random.randint (300,400)
    land_positions = [(current_land_x,current_land_y)]
    while (current_land_x < WIDTH):
        if (current_land_x == left_tank_x_position):
            # handle tank platform
            left_tank_position = (current_land_x, current_land_y)
            # Create level ground for the tank to sit on
            # Add another 50 pixels further along at same y position
            current_land_x += 60
            land_positions.append((current_land_x, current_land_y))
            continue
        elif (current_land_x == right_tank_x_position):
            # handle tank platform
            right_tank_position = (current_land_x, current_land_y)
            # Create level ground for the tank to sit on
            # Add another 50 pixels further along at same y position
            current_land_x += 60
            land_positions.append((current_land_x, current_land_y))
            continue
        # Checks to see if next position will be where the tanks are
        if (current_land_x < left_tank_x_position and current_land_x +
            LAND_CHUNK_SIZE >= left_tank_x_position):
            # set x position to tank position
            current_land_x = left_tank_x_position
        elif (current_land_x < right_tank_x_position and current_land_x + 
            LAND_CHUNK_SIZE >= right_tank_x_position):
            # set x position to tank position
            current_land_x = right_tank_x_position
        elif (current_land_x + LAND_CHUNK_SIZE > WIDTH):
            current_land_x = WIDTH 
        else:
            current_land_x += LAND_CHUNK_SIZE
        # Set the y height
        current_land_y += random.randint(0-LAND_MAX_CHG,LAND_MAX_CHG)
        # check not too high or too low 
        # Note the reverse logic as high y is bottom of screen
        if (current_land_y > HEIGHT):   # Bottom of screen
            current_land_y = HEIGHT
        if (current_land_y < LAND_MIN_Y):
            current_land_y = LAND_MIN_Y
        # Add to list
        land_positions.append((current_land_x, current_land_y))
    # Add end corners
    land_positions.append((WIDTH,HEIGHT))
    land_positions.append((0,HEIGHT))
        

# Setup the game (at end so that it can see the other functions)
setup()