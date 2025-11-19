#The start to my project

import deck_of_cards
import random


#hello
print("Hello World")
# player1 = input("What do you want to be called? ")
#
# print(f"Nice. Now let's play some Pedrito {player1}! Don't forget to call Pedrito "
#       f"when you think you have the least amount of points.")

#First we deal out the cards

spanish_deck = deck_of_cards.Deck()
spanish_deck.shuffle()

computers_hand = []
#Add Cards to Computer's hand
computers_hand = spanish_deck.deal(4)

#Test to see computer's hand
print(computers_hand)

player1_hand = []
player1_hand = spanish_deck.deal(4)

#Test to see player's hand
print(player1_hand)

#Player goes first

