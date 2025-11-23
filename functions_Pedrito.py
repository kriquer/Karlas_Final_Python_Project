'''Functions for Pedrito game moves.'''

def exchange_card_player(hand, position, dealt_card, graveyard_deck):
    #exchanges a card with another card in player's hand and adds discarded card into graveyard deck
    card = hand.pop(position)
    graveyard_deck.insert(0, card)
    hand.insert(position, dealt_card)

def cards_789(dealt_card, points_dealt_card, graveyard_deck, hand, hand2):
    graveyard_deck.insert(0, dealt_card)
    if points_dealt_card == 7:
        position = int(input("You got a 7 card. You can look at a card in your hand. Which one would you want to see? Card 1, 2, 3 or 4? "))
        print(f"The card in this position is a {hand[position]}")
    if points_dealt_card == 8:
        position = int(input("You got an 8 card. You can look at a card in the computer's hand. Which one would you want to see? Card 1, 2, 3 or 4? "))
        print(f"The card in this position is a {hand[position]}")
    if points_dealt_card == 9:
        position = int(input("You got a 9 card. You can exchange a card from your hand with one in the computer's hand. "
                                   "Which one from your hand would you want to exchange? Card 1, 2, 3 or 4? "))
        position2 = int(input("And which card in the computer's hand would you want to exchange? Card 1, 2, 3 or 4? "))
        for p in range(1, 4):
            if p == position - 1:
                exchange_card = hand[position]
                hand.pop(positon)
                exchange_card2 = hand2[position]
                hand2.pop(positon)
                hand.insert(position, exchange_card2)
                hand2.insert(position2, exchange_card)