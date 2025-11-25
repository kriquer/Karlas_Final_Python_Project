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
        #needed if implementing jokers
        else:
            return 0

    def __str__(self):
        return f"{self.number} of {self.suit}"

    def __repr__(self):
        return str(self)

# #test for Card Class
# print(Card("Cups", 2))

class Deck:    # makes the deck of cards, 4 suits "Cups, Clubs, Coins and Swords" with numbers 1-12
    def __init__(self):
        suits = ["Cups", "Clubs", "Coins", "Swords"]
        numbers = []
        for n in range(1, 13):
            numbers.append(n)
        #Creates list of cards in deck
        self.cards = [Card(suit, number) for suit in suits for number in numbers]

        #Test to show the deck
        # print(self.cards)

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
        dealt_card = dealt_card[0]
        return dealt_card.card_points()

    # def points_hand(self, hand):
    #     #sums the points in a player's hand
    #     total = 0
    #     for card in hand:
    #         total += card.card_points()
    #     return total
    #
    # def points_2cards(self, hand):
    #     #sums the points in a player's last 2 cards in his/her hand
    #     total = 0
    #     for card in hand[-2:]:
    #         total += card.card_points()
    #     return total

class Graveyard_Deck:
    def __init__(self):
        self.graveyard_deck = []

    def __str__(self):
        return f"{self.graveyard_deck}"

    def shuffle(self):
        random.shuffle(self.graveyard_deck)

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
#

# #Test for function points_2cards
# print(spanish_deck.points_2cards(hand))
