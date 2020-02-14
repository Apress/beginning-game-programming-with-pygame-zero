import random
from card import Card

class CardTable:

    def __init__ (self, card_back, cards_available):
        self.cards = []
        # Create individual card objects, two per image
        for key in cards_available.keys():
            # Add to list of cards
            self.cards.append(Card(key, card_back, cards_available[key]))
            # Add again (to have 2 cards for each img)
            self.cards.append(Card(key, card_back, cards_available[key]))

    def draw_cards(self):
        for this_card in self.cards:
            this_card.draw()

    # Set the table settings
    def setup_table(self, card_start_x, card_start_y, num_cards_per_row, x_distance_between_cards, y_distance_between_cards):
        self.card_start_x = card_start_x
        self.card_start_y = card_start_y
        self.num_cards_per_row = num_cards_per_row
        self.x_distance_between_cards = x_distance_between_cards
        self.y_distance_between_cards = y_distance_between_cards


    # Returns all cards that are face down as Card objects
    def cards_face_down(self):
        selected_cards = []
        for this_card in self.cards:
            if (this_card.is_facedown()):
                selected_cards.append(this_card)
        return selected_cards

    # Shuffle the cards and update their positions
    def deal_cards(self):
        # Create a temporary list of card indexes that is then shuffled
        keys = []
        for i in range (len(self.cards)):
            keys.append(i)
        random.shuffle(keys)

        # Setup card positions
        xpos = self.card_start_x
        ypos = self.card_start_y
        cards_on_row = 0
        # Give each card number based on position
        # count left to right, top to bottom
        card_number = 0
        for key in keys:
            # Reset (ie. unhide if hidden and display back)
            self.cards[key].reset()
            self.cards[key].number = card_number
            self.cards[key].set_position(xpos,ypos)
            xpos += self.x_distance_between_cards

            cards_on_row += 1
            # If reached end of row - move to next
            if (cards_on_row >= self.num_cards_per_row):
                cards_on_row = 0
                xpos = self.card_start_x
                ypos += self.y_distance_between_cards
            card_number += 1

    # If reach end of level
    def end_level_reached(self):
        for card in self.cards:
            if (not card.is_hidden()):
                return False
        return True

    def check_card_clicked (self, pos):
        for this_card in self.cards:
            # If not facedown then skip
            if (not this_card.is_facedown()):
                continue
            if (this_card.collidepoint(pos)):
                return this_card
        return None