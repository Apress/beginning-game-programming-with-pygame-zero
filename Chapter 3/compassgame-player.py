WIDTH = 800
HEIGHT = 600

BACKGROUND_IMG = "compassgame_background_01"

#Player character
player = Actor('compassgame_person_down_1', (WIDTH/2,HEIGHT/2))

def draw():
    screen.blit(BACKGROUND_IMG, (0,0))
    player.draw()