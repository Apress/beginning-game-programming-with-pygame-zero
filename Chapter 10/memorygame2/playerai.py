import random
from player import Player


class PlayerAi (Player):

    def __init__(self):
        Player.__init__(self)

    def make_guess(self, available_cards):
        self.guess_random(available_cards)

    def guess_random (self, available_cards):
        this_guess = random.choice(available_cards)
        this_guess.turn_over()
        self.select_card(this_guess)

    def get_card (self, card_number):
        return self.guess[card_number]
