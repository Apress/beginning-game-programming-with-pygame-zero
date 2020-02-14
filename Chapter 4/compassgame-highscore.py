import random
import math 

WIDTH = 800
HEIGHT = 600

BACKGROUND_IMG = "compassgame_background_01"
OBSTACLE_IMG = "compassgame_obstacle_01"
HIGH_SCORE_FILENAME = "compassgame_score.dat"

high_score = 0

game_state = ''
target_direction = ''

#Player character
player = Actor('compassgame_person_down_1', (WIDTH/2,HEIGHT/2))
# Which image is being displayed
player_step_count = 1
# Direction that player is facing
direction = 'down'

# Number of seconds to play when the timer starts 
timer_start = 10.9
# This is the actual timer set to the initial start value
timer = timer_start

#Rectangles for compass points for collision detection to ensure player is in correct position
box_size = 50 
north_box = Rect((0, 0), (WIDTH, box_size))
east_box = Rect((WIDTH-box_size, 0), (WIDTH, HEIGHT))
south_box = Rect((0, HEIGHT-box_size), (WIDTH, HEIGHT))
west_box = Rect((0, 0), (box_size, HEIGHT))

# Current score for this game
score = 0
# Score for each level
score_per_level = 20

# What level are we on 
level = 1

#Obstacles - these are actors, but stationary ones - default positions
obstacles = []
# Positions to place obstacles Tuples: (x,y)
obstacle_positions = [(200,200), (400, 400), (500,500), (80,120), (700, 150), (750,540), (200,550), (60,320), (730, 290), (390,170), (420,500) ]

def draw():
    global score, timer, obstacle_positions
    screen.blit(BACKGROUND_IMG, (0,0))

    # If game not running then give instruction
    if (game_state == ''):
        # Display message on screen
        screen.draw.text("Press space bar to start", center=(WIDTH/2,HEIGHT/2), fontsize=60, shadow=(1,1), color=(255,255,255), scolor="#202020")
    elif (game_state == 'end'):
        high_score = get_high_score()
        screen.draw.text("Game Over\nScore "+str(score)+"\nHigh score "+str(high_score)+"\nPress map or duck button to start", fontsize=60, center=(WIDTH/2,HEIGHT/2), shadow=(1,1), color=(255,255,255), scolor="#202020")
    else:
        screen.draw.text(target_direction, center=(WIDTH/2,50), fontsize=60, shadow=(1,1), color=(255,255,255), scolor="#202020")
        screen.draw.text('Score '+str(score), fontsize=60, center=(WIDTH-130,50), shadow=(1,1), color=(255,255,255), scolor="#202020")
        screen.draw.text('Time: '+str(math.floor(timer)), fontsize=60, center=(100,50), shadow=(1,1), color=(255,255,255), scolor="#202020")
        player.draw()
    
    for i in range (0,len(obstacles)):
        obstacles[i].draw()
    
def update(time_interval):
    # Need to be able to update global variable direction
    global direction, game_state, target_direction, score, timer_start, timer_decrement, timer, level
    
    # If state is not running then we give option to start or quit
    if (game_state == '' or game_state == 'end'):
        # Display instructions (in draw() rather than here)
        # If space key then start game
        if (keyboard.space):
            # Reset the game level and score
            set_level(1)
            high_score = get_high_score()
            if (score > high_score) :
                set_high_score(score)
            score = 0
            game_state = "playing"
            timer = timer_start
            target_direction = get_new_direction()
        # If escape then quit the game
        if (keyboard.escape):
            quit()
        return
    
    # Update timer with difference from previous
    timer -= time_interval
    # Check to see if timer has run out
    if (timer < 0.9): 
        game_state = 'end'
        return
    
    # Check for direction keys pressed
    # Can have multiple pressed in which case we move in all the directions
    # The last one in the order below is set as the direction to determine the 
    # image to use 
    new_direction = ''
    if (keyboard.up):
        new_direction = 'up'
        move_actor(new_direction)
    if (keyboard.down):
        new_direction = 'down'
        move_actor(new_direction)
    if (keyboard.left) :
        new_direction = 'left'
        move_actor(new_direction)
    if (keyboard.right) :
        new_direction = 'right'
        move_actor(new_direction)
    # If new direction is not "" then we have a move button pressed
    # so set appropriate image
    if (new_direction != '') :
        # Set image based on new_direction
        set_actor_image (new_direction)
        direction = new_direction
        
    if (reach_target(target_direction)):
        target_direction = get_new_direction()
        score += 1
        # check if we need to move up a level 
        if (score >= level * score_per_level): 
            set_level(level + 1)
        # Level score is the number of points scored in this level
        level_score = score - ((level - 1) * score_per_level)
        # Update timer - subtracting timer decrement for each point scored
        timer = timer_start + 1.5 - (timer_start * (level_score/ (level_score + 10)))
            
    # detect if collision with obstacle (game over)
    for current_obstacle in obstacles:
        if player.colliderect(current_obstacle):
            game_state = "end"
            return
        
        
def reach_target(target_direction):
    if (target_direction == 'north'):
        if (player.colliderect(north_box)): 
            return True
        else: 
            return False
    elif (target_direction == 'south'):
        if (player.colliderect(south_box)): 
            return True
        else: 
            return False
    elif (target_direction == 'east'):
        if (player.colliderect(east_box)): 
            return True
        else: 
            return False
    elif (target_direction == 'west'):
        if (player.colliderect(west_box)): 
            return True
        else: 
            return False


    
def move_actor(direction, distance = 5):
    if (direction == 'up'):
        player.y -= distance
    if (direction == 'right'):
        player.x += distance
    if (direction == 'down'):
        player.y += distance
    if (direction == 'left'):
        player.x -= distance
    
    # Check not moved past the edge of the screen
    if (player.y <= 30):
        player.y = 30
    if (player.x <= 12):
        player.x = 12
    if (player.y >= HEIGHT - 30):
        player.y = HEIGHT - 30
    if (player.x >= WIDTH - 12):
        player.x = WIDTH - 12
        

        
        
# Show image matching new_direction and current step count
def set_actor_image (new_direction):
    global player, player_step_count
    
    step_delay = 5
    player_step_count += 1

    if player_step_count >= 4 * step_delay:
        player_step_count = 1
        
    player_step_position = math.floor(player_step_count / step_delay) +1
    player.image = "compassgame_person_"+new_direction+"_"+str(player_step_position)

def get_new_direction():
    move_choices = ['north', 'east', 'south', 'west']
    return random.choice(move_choices)
    
def set_level(level_number):
    global level, obstacles, obstacle_positions
    
    level = level_number
    
    # Reset / remove all obstacles
    obstacles = []
    if (level < 1):
        return
    # Add appropriate number of obstacles - up to maximum available positions
    for i in range (0,len(obstacle_positions)):
        # If we have already added more than the obstacle level number then stop adding more
        if (i >= level_number - 1):
            break
        obstacles.append(Actor(OBSTACLE_IMG, obstacle_positions[i]))
        

# Reads high score from file and returns as a number
def get_high_score():
    try:
        file = open(HIGH_SCORE_FILENAME, 'r')
        entry = file.readline()
        file.close()
        high_score = int(entry)
    except Exception as e:
        print ("An error occured reading the high score file :" + str(e))
        high_score = 0
    return high_score
    
    
# Writes a high score to the file
def set_high_score(new_score):
    global high_score
    high_score = new_score
    try:
        file = open(HIGH_SCORE_FILENAME, 'w')
        file.write(str(high_score))
        file.close()
    except Exception as e:
        print ("An error occured writing to the high score file :" + str(e))