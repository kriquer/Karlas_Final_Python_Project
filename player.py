import decks

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return str(self)

    def exchange_card(self, dealt_card, position, graveyard_deck):
        # exchanges a dealt card with another card in player's hand and adds discarded card into graveyard deck
        if type(dealt_card) == 'list':
            dealt_card = dealt_card[0]
        card = self.hand.pop(position)
        graveyard_deck.insert(0, card)
        self.hand.insert(position, dealt_card)

    def get_card_values(self):
        #returns values of all cards in a list
        values = []
        for card in self.hand:
            values.append(decks.Card.card_points(card))
        return values

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

    def cards_789(self, opponent, dealt_card, graveyard_deck):
        if type(dealt_card) == 'list':
            dealt_card = dealt_card[0]
        graveyard_deck.insert(0, dealt_card)#discard card
        points = decks.Deck.points_dealt_card(self, dealt_card)
        if points == 7:
            pos = int(input("You got a 7 card. You can look at a card in your hand. Which one would you want to see? Card 1, 2, 3 or 4? "))
            print(f"The card in this position is a {self.hand[pos - 1]}. ")
        elif points == 8:
            pos = int(input("You got an 8 card. You can look at a card in the computer's hand. Which one would you want to see? Card 1, 2, 3 or 4? "))
            print(f"The card in this position is a {opponent.hand[pos - 1]}. ")
        elif points == 9:
            pos1 = int(input("You got a 9 card. You can exchange a card from your hand with one in the computer's hand. "
                                "Which one from your hand would you want to exchange? Card 1, 2, 3 or 4? "))
            pos2 = int(input("And which card in the computer's hand would you want to exchange? Card 1, 2, 3 or 4? "))
            card_from_player = self.hand.pop(pos1 - 1)
            card_from_opponent = opponent.hand.pop(pos2 - 1)
            self.hand.insert(pos1 - 1, card_from_opponent)
            opponent.hand.insert(pos2 - 1, card_from_player)

# Future add on Computer Class
# class Computer_Player(Player):
#     def __init__(self,name, hand):
#         self.name = "Computer"
#         self.hand = hand
#
#     def __str__(self):
#         return f"{self.name}"
#
#     def __repr__(self):
#         return str(self)
