# Memory Card Game - PyGame Zero
import random

from card import Card
from gameplay import GamePlay
from player import Player
from playerai import PlayerAi
from timer import Timer
from cardtable import CardTable

# These constants are used to simplify the game
# For more flexibility these could be replaced with configurable variables
# (eg. different number of cards for different difficulty levels)
NUM_CARDS_PER_ROW = 4
X_DISTANCE_BETWEEN_CARDS = 120
Y_DISTANCE_BETWEEN_CARDS = 120
CARD_START_X = 220
CARD_START_Y = 130

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
game_state = GamePlay()
player1 = Player()
ai = PlayerAi()
# Timer is used for AI thinking time
timer = Timer(2)
all_cards = CardTable(card_back, cards_available)
all_cards.setup_table(CARD_START_X, CARD_START_Y, NUM_CARDS_PER_ROW, X_DISTANCE_BETWEEN_CARDS, Y_DISTANCE_BETWEEN_CARDS)
all_cards.deal_cards()

def update():
    if (game_state.is_player_2_start()):
        timer.start_count_down()
        game_state.set_player_2_wait()
    if (game_state.is_player_2_wait()):
        if (timer.get_time_remaining() <= 0):
            ai.make_guess(all_cards.cards_face_down())
            timer.start_count_down()
            game_state.set_player_2_card1()
    # card 1 turned
    elif (game_state.is_player_2_card1()):
        if (timer.get_time_remaining() <= 0):
            ai.make_guess(all_cards.cards_face_down())
            timer.start_count_down()
            game_state.set_player_2_card2()
    # Card 2 selected - wait then check if matches
    elif (game_state.is_player_2_card2()):
        if (timer.get_time_remaining() <= 0):
                if ai.get_card(0).equals(ai.get_card(1)):
                    # If match add points and hide the cards
                    ai.score_point()
                    ai.get_card(0).hide()
                    ai.get_card(1).hide()
                    ai.reset_cards()
                    # Game Over
                    if (all_cards.end_level_reached()):
                        game_state.set_game_over()
                    # If user guess correct then they get another attempt
                    else:
                        game_state.continue_player()
                # If not match then turn both around
                else:
                    ai.get_card(0).turn_over()
                    ai.get_card(1).turn_over()
                    ai.reset_cards()
                    game_state.next_player()


# Mouse clicked
def on_mouse_down(pos, button):
    # Only interested in the left button
    if (not button == mouse.LEFT):
        return
    # If new game then this click is to start the game
    if (game_state.is_new_game() or game_state.is_game_over()):
        game_state.start_game()
        all_cards.deal_cards()
        player1.score = 0
        ai.score = 0
        return

    ## Reach here then we are in game play
    # Is it player1's turn
    if (game_state.is_player_1()):
        # Check for both already clicked and this is a click to test
        if (game_state.is_pair_turned_over()):
            if (player1.get_card(0).equals(player1.get_card(1))):
                # If match add points and hide the cards
                player1.score_point()
                player1.get_card(0).hide()
                player1.get_card(1).hide()
                player1.reset_cards()
                # End of game
                if (all_cards.end_level_reached()):
                    game_state.set_game_over()
                # If user guess correct then they get another attempt
                else:
                    game_state.continue_player()
            # If not match then turn both around
            else:
                player1.get_card(0).turn_over()
                player1.get_card(1).turn_over()
                player1.reset_cards()
                game_state.next_player()
            return

        # Check if clicked on a card
        card_clicked = all_cards.check_card_clicked(pos)
        if (card_clicked != None):
            card_clicked.turn_over()
            player1.select_card(card_clicked)
            # Update state
            game_state.card_clicked()

def draw():
    screen.fill((220, 220, 220))
    if (game_state.is_new_game()):
        screen.draw.text("Click mouse to start", fontsize=60, center=(WIDTH/2,HEIGHT/2), shadow=(1,1), color=(255,255,255), scolor="#202020")
    if (game_state.is_game_over()):
        screen.draw.text("Game Over\nPlayer 1 score: "+str(player1.score)+"\nPlayer 2 (AI) score: "+str(ai.score), fontsize=60, center=(WIDTH/2,HEIGHT/2), shadow=(1,1), color=(255,255,255), scolor="#202020")
    if (game_state.is_game_running()):
        # Set colors based on which player is selected
        if (game_state.is_player_1()):
            player1_color = (0,0,0)
            player2_color = (128,128,128)
        else:
            player1_color = (128,128,128)
            player2_color = (0,0,0)
        all_cards.draw_cards()
        screen.draw.text("Player 1: "+str(player1.score), fontsize=40, bottomleft=(50,50), color=player1_color)
        screen.draw.text("Player 2 (AI): "+str(ai.score), fontsize=40, bottomleft=(550,50), color=player2_color)
        # Display computer status during ai turns
        if (game_state.is_player_2_wait() or game_state.is_player_2_card1()):
            screen.draw.text("Thinking which card to pick", fontsize=40, center=(WIDTH/2,HEIGHT/2), shadow=(1,1), color=(255,255,255), scolor="#202020")