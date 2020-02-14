# Memory Card Game - PyGame Zero
import random

from card import Card
from timer import Timer
from gameplay import GamePlay

# These constants are used to simplify the game
# For more flexibility these could be replaced with configurable variables
# (eg. different number of cards for different difficulty levels)
NUM_CARDS_PER_ROW = 4
X_DISTANCE_BETWEEN_CARDS = 120
Y_DISTANCE_BETWEEN_CARDS = 120
CARD_START_X = 220
CARD_START_Y = 130
TIME_LIMIT = 60

TITLE = "Lake District Memory Game"
WIDTH = 800
HEIGHT = 600

cards_available = {
    'airafalls' : 'memorycard_airafalls',
    'ambleside' : 'memorycard_ambleside',
    'bridgehouse' : 'memorycard_bridgehouse',
    'derwentwater' : 'memorycard_derwentwater',
    'ravenglassrailway' : 'memorycard_ravenglassrailway',
    'ullswater' : 'memorycard_ullswater',
    'weatherstone' : 'memorycard_weatherstone',
    'windermere' : 'memorycard_windermere'
    }

card_back = "memorycard_back"

## Setup instance variables
count_down = Timer(TIME_LIMIT)
game_state = GamePlay()
all_cards = []
# Create individual card objects, two per image
for key in cards_available.keys():
    # Add to list of cards
    all_cards.append(Card(key, card_back, cards_available[key]))
    # Add again (to have 2 cards for each img)
    all_cards.append(Card(key, card_back, cards_available[key]))

## Functions are defined here - the rest of the initialization
## is at the bottom of the file

# Shuffle the cards and update their positions
# Do not draw as this is called before the screen is properly setup
def deal_cards():
    # Create a temporary list of card indexes that is then shuffled
    keys = []
    for i in range (len(all_cards)):
        keys.append(i)
    random.shuffle(keys)

    # Setup card positions
    xpos = CARD_START_X
    ypos = CARD_START_Y
    cards_on_row = 0
    for key in keys:
        # Reset (ie. unhide if hidden and display back)
        all_cards[key].reset()
        all_cards[key].set_position(xpos,ypos)
        xpos += X_DISTANCE_BETWEEN_CARDS

        cards_on_row += 1
        # If reached end of row - move to next
        if (cards_on_row >= NUM_CARDS_PER_ROW):
            cards_on_row = 0
            xpos = CARD_START_X
            ypos += Y_DISTANCE_BETWEEN_CARDS

def update():
    if (game_state.is_new_game()):
        pass
    elif (game_state.is_game_over()):
        pass
    else:
        if (count_down.get_time_remaining()<=0):
            game_state.set_game_over()

# Mouse clicked
def on_mouse_down(pos, button):
    # Only interested in the left button
    if (not button == mouse.LEFT):
        return
    # If new game then this click is to start the game
    if (game_state.is_new_game()):
        game_state.start_game()
        # start the timer
        count_down.start_count_down(TIME_LIMIT)
        deal_cards()
        return
    # If game over then this click is to get to new game screen
    if (game_state.is_game_over()):
        # Make sure the timer has reached zero (short delay to see state)
        if (count_down.get_time_remaining()<=0):
            game_state.set_new_game()
        return

    ## Reach here then we are in game play
    # First check for both already clicked and this is a click to test
    if (game_state.is_pair_turned_over()):
        if (all_cards[game_state.get_card(0)].equals(all_cards[game_state.get_card(1)])):
            # Add points and hide the cards
            game_state.score_point()
            all_cards[game_state.get_card(0)].hide()
            all_cards[game_state.get_card(1)].hide()
            # Check if we are at the end of this level (all cards done)
            if (end_level_reached()):
                deal_cards()
        # If not match then turn both around
        else:
            all_cards[game_state.get_card(0)].turn_over()
            all_cards[game_state.get_card(1)].turn_over()
            game_state.not_pair()
        return

    ## Otherwise we just turn over the next card if clicked
    for i in range (len(all_cards)):
        if (all_cards[i].collidepoint(pos)):
            # Ignore if card hidden, or has already been turned up
            if (all_cards[i].is_hidden() or all_cards[i].is_faceup()):
                return
            all_cards[i].turn_over()
            # Update state
            game_state.card_clicked(i)

# If reach end of level ?
def end_level_reached():
    for card in all_cards:
        if (not card.is_hidden()):
            return False
    return True

def draw():
    screen.fill((220, 220, 220))
    if (game_state.is_new_game()):
        screen.draw.text("Click mouse to start", fontsize=60, center=(WIDTH/2,HEIGHT/2), shadow=(1,1), color=(255,255,255), scolor="#202020")
    if (game_state.is_game_over()):
        screen.draw.text("Game Over\nScore: "+str(game_state.score), fontsize=60, center=(WIDTH/2,HEIGHT/2), shadow=(1,1), color=(255,255,255), scolor="#202020")
    if (game_state.is_game_running()):
        for card in all_cards:
            card.draw()
        screen.draw.text("Time remaining: "+str(count_down.get_time_remaining()), fontsize=40, bottomleft=(50,50), color=(0,0,0))
        screen.draw.text("Score: "+str(game_state.score), fontsize=40, bottomleft=(600,50), color=(0,0,0))

### End of functions - start of initialization code
deal_cards()