import random

class Card:
    #makes a single card
    def __init__(self, suit, number):
        self.suit = suit
        self.number= number

    def __str__(self):
        return f"{self.number} of {self.suit}"

    def __repr__(self):
        return str(self)

# #test for Card Class
# print(Card("Cups", 2))

class Deck:
    # makes the deck of cards, 4 suits "Cups, Clubs, Coins and Swords" with numbers 1-12
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

    def remove(self):
        #Remove cards from deck
        return self.cards.remove


# #test for Deck Class
# spanish_deck= Deck()
# print(spanish_deck)

# #Test for deal method
# spanish_deck.deal(4)
# print (spanish_deck.deal(4))


