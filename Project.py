#The start to my project
from random import randint
import deck_of_cards

# #hello
# print("Hello World")
# #p1 means Player 1
# p1 = input("What do you want to be called? ")
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
print(f"computer's hand is {c_hand}")

p1_hand = []
p1_hand = spanish_deck.deal(4)

# #Test to see player1's hand
# print(f"{p1}'s hand is {p1_hand}")

# #Player1 goes first
# p1_choice = input("Want to call Pedrito or take a card? Choose A for calling Pedrito or B for taking a card. ")
# # use try block for checking A or B
# if p1_choice == "A":
#     print(f"{p1} calls Pedrito! ")
#     sum_p1_hand = spanish_deck.points_hand(p1_hand)
#     sum_c_hand = spanish_deck.points_hand(c_hand)
#     print(sum_c_hand)
#     if sum_p1_hand < sum_c_hand:
#         print("Congrats! You won Pedrito! ")
#     else:
#         print(f"Sorry {p1} you lost. Try again? ")
#
# if p1_choice == "B":
#     #deal a card to player 1
#     dealt_card = spanish_deck.deal(1)
#     print(f"You drew a {dealt_card}")
#     # print(p1_hand)
#     p1_card_choice = input(
#         "What do you want with your card? "
#         "A: Return the card to the deck? "
#         "B: Exchange card with one of your cards? "
#     )
#     if p1_card_choice == "A":
#         #take card from Player's hand and return to bottom(last position) of deck
#         returned_card = dealt_card[0]
#         spanish_deck.cards.append(returned_card)
#         #switch card in Player's hand
#     if p1_card_choice == "B":
#         card_switch = input("Which card do you want to switch, card in position 1, 2 ,3 or 4? ")
#         new_card = dealt_card[0] #makes card not a list variable
#         # switches card with chosen card by player
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
#
# print(f"{p1}'s hand is {p1_hand}")

#start of computer's turn
print("Now it is my turn!")
#computer chooses if to call Pedrito or not depending on total points with some randomization
sum_c_hand_2cards = spanish_deck.points_2cards(c_hand)
print(sum_c_hand_2cards)
#randomize if computer calls Pedrito if cards are low
if sum_c_hand_2cards < 4:
    random_choice = randint(1, 10)
    if random_choice < 7:
        print("Pedrito! ")



#     if sum_p1_hand < sum_c_hand:
#         print("I won! ")
#     else:
#         print(f"Sorry {p1} you lost. Try again? ")
#
# if p1_choice == "B":
#     #deal a card to player 1
#     dealt_card = spanish_deck.deal(1)
#     print(f"You drew a {dealt_card}")
#     # print(p1_hand)
#     p1_card_choice = input(
#         "What do you want with your card? "
#         "A: Return the card to the deck? "
#         "B: Exchange card with one of your cards? "
#     )
#     if p1_card_choice == "A":
#         #take card from Player's hand and return to bottom(last position) of deck
#         returned_card = dealt_card[0]
#         spanish_deck.cards.append(returned_card)
#         #switch card in Player's hand
#     if p1_card_choice == "B":
#         card_switch = input("Which card do you want to switch, card in position 1, 2 ,3 or 4? ")
#         new_card = dealt_card[0] #makes card not a list variable
#         # switches card with chosen card by player
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
#
# print(f"{p1}'s hand is {p1_hand}")
#
#
