"""Classes for card and a deck"""

import random

class Card:
    #makes a single card
    def __init__(self, suit, number):
        self.suit = suit
        self.number= number

    def card_points(self):
        #how to get point value of card
        if isinstance(self.number, int):
            return self.number
        #Future add on: jokers, need this if implementing jokers
        else:
            return 0

    def __str__(self):
        return f"{self.number} of {self.suit}"

    def __repr__(self):
        return str(self)

##test for Card Class
#print(Card("Cups", 2))

class Deck:    #makes the deck of cards, 4 suits "Cups, Clubs, Coins and Swords" with numbers 1-12, future addon would be to add 2 jokers
    def __init__(self):
        suits = ["Cups", "Clubs", "Coins", "Swords"]
        numbers = []
        for n in range(1, 13):
            numbers.append(n)
        #Creates list of cards in deck
        self.cards = [Card(suit, number) for suit in suits for number in numbers]

    def __str__(self):
        return f"A Spanish Deck with {len(self.cards)} cards remaining."

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards):
        if num_cards > len(self.cards):
            print("There aren't sufficient cards")
            return None
        #Deals cards
        dealt_cards = self.cards[:num_cards]
        #Remove cards from deck
        self.cards = self.cards[num_cards:]
        return dealt_cards

    def points_dealt_card(self, dealt_card):
        return dealt_card.card_points()

# #test for Deck Class
# spanish_deck= Deck()
# print(spanish_deck)
#
# #Test for deal method
# hand = spanish_deck.deal(4)
# print(hand)
#
# #Test for dealt card points
# dealt_card = spanish_deck.deal(1)
# print(spanish_deck.points_dealt_card(dealt_card))

