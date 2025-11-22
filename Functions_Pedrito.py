'''Functions for Pedrito game moves'''

def exchange_card_player(hand, position, dealt_card, graveyard_deck):
    #exchanges a card with another card in player's hand and adds discarded card into graveyard deck
    card = hand.pop(position)
    graveyard_deck.insert(0, card)
    hand.insert(position, dealt_card)


# def discard_card(hand, position):
#     #discards card from a player's hand into the graveyard
#     card = hand.pop(position)
#     graveyard_deck.insert(0, card)