from fleet import Fleet
from grid import Grid
from ai import Ai

WIDTH = 1024
HEIGHT  = 768

# Start of your grid (after labels)
YOUR_GRID_START = (94,180)
# Start of enemy grid
ENEMY_GRID_START = (544,180)
GRID_SIZE = (38,38)

player = "player1"

grid_img_1 = Actor ("grid", topleft=(50,150))
grid_img_2 = Actor ("grid", topleft=(500,150))

own_fleet = Fleet(YOUR_GRID_START, GRID_SIZE)
enemy_fleet = Fleet(ENEMY_GRID_START, GRID_SIZE)

## Manually position ships position random or allow
## player to choose.
own_fleet.add_ship("destroyer",(7,0),"horizontal")
own_fleet.add_ship("cruiser",(1,1),"horizontal")
own_fleet.add_ship("submarine",(1,4),"vertical")
own_fleet.add_ship("battleship",(4,5),"horizontal")
own_fleet.add_ship("carrier",(9,3),"vertical")

enemy_fleet.add_ship("destroyer",(5,8),"horizontal", True)
enemy_fleet.add_ship("cruiser",(3,4),"vertical", True)
enemy_fleet.add_ship("submarine",(4,1),"horizontal", True)
enemy_fleet.add_ship("battleship",(8,3),"vertical", True)
enemy_fleet.add_ship("carrier",(1,1),"vertical", True)

# Don't need a player1 object
# Player 2 represents the AI player
player2=Ai()

def draw():
    screen.fill((192,192,192))
    grid_img_1.draw()
    grid_img_2.draw()
    screen.draw.text("Battleships", fontsize=60, center=(WIDTH/2,50), shadow=(1,1), color=(255,255,255), scolor=(32,32,32))
    screen.draw.text("Your fleet", fontsize=40, topleft=(100,100), color=(255,255,255))
    screen.draw.text("The enemy fleet", fontsize=40, topleft=(550,100), color=(255,255,255))
    own_fleet.draw()
    enemy_fleet.draw()
    if (player == "gameover"):
        screen.draw.text("Game Over", fontsize=60, center=(WIDTH/2,HEIGHT/2), shadow=(1,1), color=(255,255,255), scolor=(32,32,32))

def update():
    global player
    if (player == "player2"):
        grid_pos = player2.fire_shot()
        # Ai uses list position - but grid uses grid
        result = own_fleet.fire(grid_pos)
        player2.fire_result (grid_pos, result)
        # If ship sunk then inform Ai player
        if (result == True):
            if (own_fleet.is_ship_sunk_grid_pos(grid_pos)):
                player2.ship_sunk(grid_pos)
                # As a ship is sunk - check to see if all ships are sunk
                if own_fleet.all_sunk():
                    player = "gameover"
                    return

        # If reach here then not gameover, so switch back to main player
        player = "player1"

def on_mouse_down(pos, button):
    global player
    if (button != mouse.LEFT):
        return
    if (player == "player1"):
        if (enemy_fleet.grid.check_in_grid(pos)):
            grid_location = enemy_fleet.grid.get_grid_pos(pos)
            #print (Grid.grid_to_string(grid_location))
            enemy_fleet.fire(grid_location)
            if enemy_fleet.all_sunk():
                player = "gameover"
            else:
                # switch to player 2
                player = "player2"