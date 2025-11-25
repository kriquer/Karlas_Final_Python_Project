import decks

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = []

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return str(self)

    # def add_cards(self, dealt_card):
    #     self.hand.append(self, dealt_card)

    def exchange_card(self, hand, dealt_card, position):
        # exchanges a dealt card with another card in player's hand and adds discarded card into graveyard deck
        card = hand.pop(position - 1)
        decks.graveyard_deck.insert(0, card)
        self.hand.insert(position - 1, dealt_card)

    def get_card_values(self, hand):
        card0 = hand[0]
        points_card0 = decks.Card.card_points(card0)
        card1 = hand[1]
        points_card1 = decks.Card.card_points(card1)
        card2 = hand[2]
        points_card2 = decks.Card.card_points(card2)
        card3 = hand[3]
        points_card3 = decks.Card.card_points(card3)

    def points_hand(self, hand):
        # sums the points in a player's hand
        total = 0
        for card in hand:
            total += card.card_points()
        return total

    def points_2cards(self, hand):
        # sums the points in a player's last 2 cards in his/her hand
        total = 0
        for card in hand[-2:]:
            total += card.card_points()
        return total

class Human_Player(Player):
    def __init__(self, name, hand):
        super().__init__(name, hand)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return str(self)

    def cards_789(self, opponent, dealt_card):
        graveyard_deck.insert(0, dealt_card)#discard card
        if points_dealt_card == 7:
            pos = int(input("You got a 7 card. You can look at a card in your hand. Which one would you want to see? Card 1, 2, 3 or 4? "))
            print(f"The card in this position is a {hand[pos-1]}. ")
        elif points_dealt_card == 8:
            pos = int(input("You got an 8 card. You can look at a card in the computer's hand. Which one would you want to see? Card 1, 2, 3 or 4? "))
            print(f"The card in this position is a {hand[pos-1]}.  ")
        elif points_dealt_card == 9:
            pos1 = int(input("You got a 9 card. You can exchange a card from your hand with one in the computer's hand. "
                                "Which one from your hand would you want to exchange? Card 1, 2, 3 or 4? "))
            pos2 = int(input("And which card in the computer's hand would you want to exchange? Card 1, 2, 3 or 4? "))
            card_from_player = self.hand.pop(pos1)
            card_from_opponent = opponent.hand.pop(pos2)
            self.hand.insert[pos1, card_from_opponent]
            opponent.hand.insert(pos2, card_from_player)

# class Computer_Player(Player):
#     def __init__(self,name, hand):
#         self.name = "Computer"
#         self.hand = []
#
#     def __str__(self):
#         return f"{self.name}"
#
#     def __repr__(self):
#         return str(self)
