import random
import math 

WIDTH = 800
HEIGHT = 600

BACKGROUND_IMG = "compassgame_background_01"

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

def draw():
    global score, timer
    screen.blit(BACKGROUND_IMG, (0,0))

    # If game not running then give instruction
    if (game_state == ''):
        # Display message on screen
        screen.draw.text("Press space bar to start", center=(WIDTH/2,HEIGHT/2), fontsize=60, shadow=(1,1), color=(255,255,255), scolor="#202020")
    elif (game_state == 'end'):
        screen.draw.text("Game Over "+str(score)+"\nPress space bar to start again", center=(WIDTH/2,HEIGHT/2), fontsize=60, shadow=(1,1), color=(255,255,255), scolor="#202020")
    else:
        screen.draw.text(target_direction, center=(WIDTH/2,50), fontsize=60, shadow=(1,1), color=(255,255,255), scolor="#202020")
        screen.draw.text('Score '+str(score), fontsize=60, center=(WIDTH-130,50), shadow=(1,1), color=(255,255,255), scolor="#202020")
        screen.draw.text('Time: '+str(math.floor(timer)), fontsize=60, center=(100,50), shadow=(1,1), color=(255,255,255), scolor="#202020")
        player.draw()
    
def update(time_interval):
    # Need to be able to update global variable direction
    global direction, game_state, target_direction, score, timer_start, timer_decrement, timer

    
    # If state is not running then we give option to start or quit
    if (game_state == '' or game_state == 'end'):
        # Display instructions (in draw() rather than here)
        # If space key then start game
        if (keyboard.space):
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
        # Update timer - subtracting timer decrement for each point scored
        timer = timer_start + 1.5 - (timer_start * (score/ (score + 10)))

        
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