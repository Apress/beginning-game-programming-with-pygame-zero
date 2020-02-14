from card import Card

class Player():

    # Index of cards that ai remembers
    # Stored as dictionary as cards will be missing or be forgotten
    card_memory = {}
    click_order = []

    def __init__ (self):
        # Track which cards are turned over
        self.guess = [None, None]
        self.score = 0

    @staticmethod
    def new_game():
        Player.card_memory = {}
        Player.click_order = []


    def score_point (self):
        self.score += 1

    # Returns a single card object - either 0 or 1
    def get_card (self, card_number):
        return self.guess[card_number]

    # Reset cards held in hand, but does not hide / turn_over card
    def reset_cards(self):
        self.guess[0] = None
        self.guess[1] = None

    def select_card(self, card):
        if (self.guess[0] == None):
            self.guess[0] = card
        else:
            self.guess[1] = card
        Player.card_memory[card.number] = card

    # Returns the number of cards that are selected
    def num_cards_selected(self):
        if (self.guess[0] == None):
            return 0
        elif (self.guess[1] == None):
            return 1
        else:
            return 2
