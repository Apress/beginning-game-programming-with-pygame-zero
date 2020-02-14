WIDTH = 800
HEIGHT = 600

BACKGROUND_IMG = "compassgame_background_01"

#Player character
player = Actor('compassgame_person_down_1', (WIDTH/2,HEIGHT/2))
# Direction that player is facing
direction = 'down'

def draw():
    screen.blit(BACKGROUND_IMG, (0,0))
    player.draw()
    
def update():
    # Need to be able to update global variable direction
    global direction
    
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
        player.image = "compassgame_person_"+new_direction+"_1"
        direction = new_direction
    
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
