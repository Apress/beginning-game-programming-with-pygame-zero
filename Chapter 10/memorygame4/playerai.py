import random
from player import Player


class PlayerAi (Player):

    def __init__(self):
        Player.__init__(self)
        self.difficulty = "easy"

    def make_guess(self, available_cards):
        if self.difficulty == "easy":
            self.guess_random(available_cards)
        elif self.difficulty == "difficult":
            self.guess_remember_sometimes(available_cards)
        else:
            self.guess_remember_all(available_cards)

    def guess_random (self, available_cards):
        this_guess = random.choice(available_cards)
        this_guess.turn_over()
        self.select_card(this_guess)

    def guess_remember_all (self, available_cards):
        # If first guess then use random
        if (self.guess[0] == None):
           self.guess_random(available_cards)
           return
        # Search to see if we have seen a matching card
        for search_card in Player.card_memory.values():
            # ignore if current card - or card has been hidden since
            if (search_card == self.guess[0] or search_card.is_hidden()):
                continue
            # Check to see if the card matches
            if (search_card.equals(self.guess[0])):
                search_card.turn_over()
                self.select_card(search_card)
                return
        # If not found the matching card then use random
        self.guess_random(available_cards)

    def guess_remember_sometimes (self, available_cards):
        # If first guess then use random
        if (self.guess[0] == None):
           self.guess_random(available_cards)
           return
        # Random whether make a proper guess or random guess
        if (random.randint(1,10) < 4):
            self.guess_random(available_cards)
            return
        # Search to see if we have seen a matching card
        for search_card in Player.card_memory.values():
            # ignore if current card - or card has been hidden since
            if (search_card == self.guess[0] or search_card.is_hidden()):
                continue
            # Check to see if the card matches
            if (search_card.equals(self.guess[0])):
                search_card.turn_over()
                self.select_card(search_card)
                return
        # If not found the matching card then use random
        self.guess_random(available_cards)

    def guess_remember_recent (self, available_cards):
        # If first guess then use random
        if (self.guess[0] == None):
           self.guess_random(available_cards)
           return
        # Get last 4 cards that were clicked
        # These are just card numbers
        recent_cards = Player.click_order[:-4]
        # Search to see if one of those is a matching card
        for search_card in Player.card_memory.values():
            # ignore if current card - or card has been hidden since
            if (search_card == self.guess[0] or search_card.is_hidden()):
                continue
            # ignore if not a recent card
            if (search_card.number not in recent_cards):
               continue
            # Check to see if the card matches
            if (search_card.equals(self.guess[0])):
                search_card.turn_over()
                self.select_card(search_card)
                return
        # If not found the matching card then use random
        self.guess_random(available_cards)

    def get_card (self, card_number):
        return self.guess[card_number]