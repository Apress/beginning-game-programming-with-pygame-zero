# State is tracked as a number, but to make the code readable constants are used
STATE_NEW = 0               # Game ready to start, but not running
STATE_PLAYER1_START = 10    # Player 1 to turn over card
STATE_PLAYER1_CARDS_1 = 11  # Card 1 turned over
STATE_PLAYER1_CARDS_2 = 12  # Card 2 turned over
STATE_PLAYER2_START = 20    # Player 2 starts go
STATE_PLAYER2_WAIT = 21     # Delay before Card 1 turned over
STATE_PLAYER2_CARDS_1 = 22  # Card 1 turned over
STATE_PLAYER2_CARDS_2 = 23  # Card 2 turned over
STATE_END = 50

# Number of seconds to display high score before allowing click to continue
TIME_DISPLAY_SCORE = 3

class GamePlay:

    def __init__ (self):
        self.state = STATE_NEW

    # If game has not yet started
    def is_new_game(self):
        if self.state == STATE_NEW:
            return True
        return False

    def is_game_over(self):
        if self.state == STATE_END:
            return True
        return False

    def is_player_1(self):
        if (self.state >= STATE_PLAYER1_START and self.state <= STATE_PLAYER1_CARDS_2):
            return True
        return False

    def is_player_2(self):
        if (self.state >= STATE_PLAYER2_START and self.state <= STATE_PLAYER2_CARDS_2):
            return True
        return False

    def is_player_2_start(self):
        if (self.state == STATE_PLAYER2_START):
            return True
        return False

    def is_player_2_wait(self):
        if (self.state == STATE_PLAYER2_WAIT):
            return True
        return False

    def is_player_2_card1(self):
        if (self.state == STATE_PLAYER2_CARDS_1):
            return True
        return False

    def is_player_2_card2(self):
        if (self.state == STATE_PLAYER2_CARDS_2):
            return True
        return False

    def set_player_2_wait(self):
        self.state = STATE_PLAYER2_WAIT

    def set_player_2_card1(self):
        self.state = STATE_PLAYER2_CARDS_1

    def set_player_2_card2(self):
        self.state = STATE_PLAYER2_CARDS_2

    def start_game(self):
        self.state = STATE_PLAYER1_START

    def set_game_over(self):
        # player gets to see high score
        self.state = STATE_END

    def is_game_running(self):
        if (self.state >= STATE_PLAYER1_START and self.state < STATE_END):
            return True
        return False

    # Contine with current player (matched correctly)
    def continue_player (self):
        if self.state <= STATE_PLAYER1_CARDS_2:
            self.state = STATE_PLAYER1_START
        else:
            self.state = STATE_PLAYER2_START

    # Switch to next player (not matched)
    def next_player (self):
        if self.state <= STATE_PLAYER1_CARDS_2:
            self.state = STATE_PLAYER2_START
        else:
            self.state = STATE_PLAYER1_START

    def set_new_game(self):
        self.state = STATE_NEW

    def is_pair_turned_over(self):
        if (self.state == STATE_PLAYER1_CARDS_2):
            return True
        return False

    # If a card is clicked then update the state accordingly
    def card_clicked(self):
        if (self.state == STATE_PLAYER1_START):
            self.state = STATE_PLAYER1_CARDS_1
        elif (self.state == STATE_PLAYER1_CARDS_1):
            self.state = STATE_PLAYER1_CARDS_2