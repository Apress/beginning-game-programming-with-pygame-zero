# State is tracked as a number, but to make the code readable constants are used
STATE_NEW = 0               # Game ready to start, but not running
STATE_PLAYER1_START = 1     # Player 1 to turn over card
STATE_PLAYER1_CARDS_1 = 2   # Card 1 turned over
STATE_PLAYER1_CARDS_2 = 30  # Card 2 turned over
STATE_END = 50

# Number of seconds to display high score before allowing click to continue
TIME_DISPLAY_SCORE = 3

class GamePlay:
	
    def __init__ (self):
        # These are what we need to track
        self.score = 0
        self.state = STATE_NEW
        # These are the cards that have been turned up.
        self.cards_selected = [None, None]

    # If game has not yet started
    def is_new_game(self):
        if self.state == STATE_NEW:
            return True
        return False

    def is_game_over(self):
        if self.state == STATE_END:
            return True
        return False

    def set_game_over(self):
        # player gets to see high score
        self.state = STATE_END

    def is_game_running(self):
        if (self.state >= STATE_PLAYER1_START and self.state < STATE_END):
            return True
        return False

    def start_game(self):
        self.score = 0
        self.state = STATE_PLAYER1_START

    def set_new_game(self):
        self.state = STATE_NEW

    def is_pair_turned_over(self):
        if (self.state == STATE_PLAYER1_CARDS_2):
            return True
        return False

    # Return the index position of the specified card
    def get_card(self, card_number):
        return self.cards_selected[card_number]

    # Point scored, so add score and update state
    def score_point(self):
        self.score += 1
        self.state = STATE_PLAYER1_START

    # Not a pair - just update state
    def not_pair(self):
        self.state = STATE_PLAYER1_START

    # If a card is clicked then update the state accordingly
    def card_clicked(self, card_index):
        if (self.state == STATE_PLAYER1_START):
            self.cards_selected[0] = card_index
            self.state = STATE_PLAYER1_CARDS_1
        elif (self.state == STATE_PLAYER1_CARDS_1):
            self.cards_selected[1] = card_index
            self.state = STATE_PLAYER1_CARDS_2