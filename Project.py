#The start to my project

import deck_of_cards
import random


#hello
print("Hello World")
#p1 means Player 1
p1 = input("What do you want to be called? ")
#
# print(f"Nice. Now let's play some Pedrito {p1}! Don't forget to call Pedrito "
#       f"when you think you have the least amount of points.")

#First we deal out the cards

spanish_deck = deck_of_cards.Deck()
spanish_deck.shuffle()

#computer is c
c_hand = []
#Add Cards to Computer's hand
c_hand = spanish_deck.deal(4)

#Test to see computer's hand
print(c_hand)

p1_hand = []
p1_hand = spanish_deck.deal(4)

#Test to see player1's hand
print(f"{p1}'s hand is {p1_hand}")

#Player1 goes first
p1_choice = input("Want to call Pedrito or take a card? Choose A for calling Pedrito or B for taking a card. ")
# use try block for checking A or B
if p1_choice == "A":
    print(f"{p1} calls Pedrito! ")
    sum_p1_hand = spanish_deck.points_hand(p1_hand)
    sum_c_hand = spanish_deck.points_hand(c_hand)
    print(sum_c_hand)
    if sum_p1_hand < sum_c_hand:
        print("Congrats! You won Pedrito! ")
    else:
        print(f"Sorry {p1} you lost. Try again? ")

