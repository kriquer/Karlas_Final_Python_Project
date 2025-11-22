'''Functions for Pedrito game moves'''

def exchange_card_player(player, deck, graveyard):
    #exchanges a card with another card in player's hand and adds discarded card into graveyard deck
#         card_switch = input("Which card do you want to switch, card in position 1, 2 ,3 or 4? ")
#   new_card = dealt_card[0] #makes card not a list variable
#         #switches card with chosen card by player
#         if card_switch == "1":
#             p1_hand.pop(0)
#             p1_hand.insert(0, new_card)
#         elif card_switch == "2":
#             p1_hand.pop(1)
#             p1_hand.insert(1, new_card)
#         elif card_switch == "3":
#             p1_hand.pop(2)
#             p1_hand.insert(2, new_card)
#         else:
#             p1_hand.pop(3)
#             p1_hand.insert(3, new_card)

def exchange_card(card, position):
    c_hand.pop(position)
    c_hand.insert(position, new_card)