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
graveyard_deck = []

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
#         #take card from Player's hand and discard into top(first position in list) of graveyard deck
#         returned_card = dealt_card[0]
#         graveyard_deck.insert(0, returned_card)
#     if p1_card_choice == "B":
#       #switch card in Player's hand
#         card_switch = input("Which card do you want to switch, card in position 1, 2 ,3 or 4? ")
#         new_card = dealt_card[0] #makes card not a list variable
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
#
# print(f"{p1}'s hand is {p1_hand}")

#start of computer's turn
print("Now it is my turn!")
#computer chooses if to call Pedrito or not depending on total points with some randomization
sum_c_hand_2cards = spanish_deck.points_2cards(c_hand)

#test to get points of front cards in computer's hand
print(f"Sum of my 2 lower cards is {sum_c_hand_2cards}")

#randomize if computer calls Pedrito if cards are low
random_choice = randint(1, 10)
if sum_c_hand_2cards <= 4 and random_choice < 7:
    print("Pedrito! ")

#if computer does not call Pedrito deal a card to computer
dealt_card = spanish_deck.deal(1)
print(f"The computer drew a {dealt_card}")
dealt_card = dealt_card[0] #makes card not a list variable
points_dealt_card = deck_of_cards.Card.card_points(dealt_card) #gets point value of the dealt card

#test to get point value of 1 card
#print(points_dealt_card)

'''Computer's choices for it's dealt card are:
    Discard card to graveyard deck
    Exchange card with one of it's own cards'''

if points_dealt_card >= 10:
    #discards card into graveyard deck
    graveyard_deck.insert(0, dealt_card)

#test to see if returned card is in the graveyard deck
print(f"Graveyard deck so far is {graveyard_deck}")

#first have to return value of top cards in computer's hand
card0 = c_hand[0]
points_card0 = deck_of_cards.Card.card_points(card0)
card1 = c_hand[1]
points_card1 = deck_of_cards.Card.card_points(card1)
card2 = c_hand[2]
points_card2 = deck_of_cards.Card.card_points(card2)
card3 = c_hand[3]
points_card3 = deck_of_cards.Card.card_points(card3)

random_choice = randint(1, 10)
if random_choice < 7: #this means computer remembers cards 2 and 3
    #puts dealt card in position 2 or 3 of computer's hand
    if points_dealt_card < points_card2 and points_card2 >= points_card3:
       pass#exchange the card and add discarded card into graveyard deck
    elif points_dealt_card < points_card3 and points_card3 >= points_card2:
       pass#exchange the card and add discarded card into graveyard deck
    else: #computer knows cards 2 and 3 are low so wants to exchange with unknown cards 0 and 1
        if points_dealt_card <= 4:
            position = randint(1, 2)
            Functions_Pedrito.exchange_card(dealt_card, position)
elif points_dealt_card <= 4: #computer does not remember any cards so wants to exchange with any card
    position = randint(1, 4)
    Functions_Pedrito.exchange_card(dealt_card, position)
else: #discard card into graveyard deck
    returned_card = dealt_card[0]
    graveyard_deck.insert(0, returned_card)

# print(f"Computer's's hand is now {c_hand} ")

