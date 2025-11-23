#The start to my project
from random import randint
import deck_of_cards
import functions_Pedrito

#hello
print("Hello World")
#p1 means Player 1
p1 = input("What do you want to be called? ")

print(f"Nice. Now let's play some Pedrito {p1}! Don't forget to call Pedrito "
      f"when you think you have the least amount of points.")

#First we deal out the cards
spanish_deck = deck_of_cards.Deck()
spanish_deck.shuffle()
graveyard_deck = []

#computer is c
c_hand = []
#Add Cards to Computer's hand
c_hand = spanish_deck.deal(4)

#Test to see computer's hand
print(f"Computer's hand is {c_hand}")

p1_hand = []
p1_hand = spanish_deck.deal(4)

#Test to see player1's hand
print(f"{p1}'s hand is {p1_hand}")

for i in range(1000):
    #Player1 goes first
    p1_choice = input("Your turn! Want to call Pedrito or take a card? Choose A for calling Pedrito or B for taking a card. ")
    # use try block for checking A or B
    if p1_choice.upper() == "A":
        print(f"{p1} calls Pedrito! ")
        sum_p1_hand = spanish_deck.points_hand(p1_hand)
        sum_c_hand = spanish_deck.points_hand(c_hand)
        print(sum_c_hand)
        if sum_p1_hand < sum_c_hand:
            print("Congrats! You won Pedrito! ")
        else:
            print(f"Sorry {p1} you lost. Try again? ")
        break
    if p1_choice.upper() == "B":
        #deal a card to player 1
        dealt_card = spanish_deck.deal(1)
        dealt_card = dealt_card[0]  # makes card not a list variable
        print(f"You drew a {dealt_card}")
        points_dealt_card = deck_of_cards.Card.card_points(dealt_card)
        if points_dealt_card == 7 or points_dealt_card == 8 or points_dealt_card == 9:
            functions_Pedrito.cards_789(dealt_card, points_dealt_card, graveyard_deck, p1_hand, c_hand)
        else:
            p1_card_choice = input(
            "What do you want with your card? "
            "A: Discard the card to the graveyard deck? "
            "B: Exchange card with one of your cards? "
            )
            if p1_card_choice.upper() == "A":
                #take card from Player's hand and discard into top(first position in list) of graveyard deck
                graveyard_deck.insert(0, dealt_card)
            if p1_card_choice.upper() == "B":
              #switch card in Player's hand
                card_switch = input("Which card do you want to switch, card in position 1, 2 ,3 or 4? ")
                #switches card with chosen card by player
                if card_switch == "1":
                    functions_Pedrito.exchange_card_player(p1_hand, 0, dealt_card, graveyard_deck)
                elif card_switch == "2":
                    functions_Pedrito.exchange_card_player(p1_hand, 1, dealt_card, graveyard_deck)
                elif card_switch == "3":
                    functions_Pedrito.exchange_card_player(p1_hand, 2, dealt_card, graveyard_deck)
                else:
                    functions_Pedrito.exchange_card_player(p1_hand, 3, dealt_card, graveyard_deck)

    print(f"{p1}'s hand is {p1_hand}")
    print(f"graveyard has {graveyard_deck}")

    #start of computer's turn
    print("Now it is my turn!")
    #computer chooses if to call Pedrito or not depending on total points with some randomization
    sum_c_hand_2cards = spanish_deck.points_2cards(c_hand)

    #test to get points of front cards in computer's hand
    print(f"Sum of computer's lower cards is {sum_c_hand_2cards}")

    #randomize if computer calls Pedrito if cards are low
    random_choice = randint(1, 10)
    if sum_c_hand_2cards <= 4 and random_choice <= 7:
        print("Pedrito! ")
        break

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
    random_choice = randint(1, 10)
    if points_dealt_card >= 10:
        #discards card into graveyard deck
        graveyard_deck.insert(0, dealt_card)
    elif random_choice < 7: #this means computer remembers cards 2 and 3
        #puts dealt card in position 2 or 3 of computer's hand
        #first have to return value of top cards in computer's hand
        card0 = c_hand[0]
        points_card0 = deck_of_cards.Card.card_points(card0)
        card1 = c_hand[1]
        points_card1 = deck_of_cards.Card.card_points(card1)
        card2 = c_hand[2]
        points_card2 = deck_of_cards.Card.card_points(card2)
        card3 = c_hand[3]
        points_card3 = deck_of_cards.Card.card_points(card3)
        if points_dealt_card < points_card2 and points_card2 >= points_card3:
           #exchange the card in position 2 and add discarded card into graveyard deck
            functions_Pedrito.exchange_card_player(c_hand, 2, dealt_card, graveyard_deck)
        elif points_dealt_card < points_card3 and points_card3 >= points_card2:
           #exchange the card in position 3 and add discarded card into graveyard deck
            functions_Pedrito.exchange_card_player(c_hand, 3, dealt_card, graveyard_deck)
        else: #computer knows cards 2 and 3 are low so wants to exchange with unknown cards 0 and 1
            if points_dealt_card <= 4:
                position = randint(1, 2)
                functions_Pedrito.exchange_card_player(c_hand, position, dealt_card, graveyard_deck)
    elif points_dealt_card <= 4: #computer does not remember any cards so wants to exchange with any card
        position = randint(0, 3)
        functions_Pedrito.exchange_card_player(c_hand, position, dealt_card, graveyard_deck)
    else: #discard dealt card into graveyard deck
        graveyard_deck.insert(0, dealt_card)

    print(f"Computer's's hand is now {c_hand} ")
    #test to see if returned card is in the graveyard deck
    print(f"Graveyard deck so far is {graveyard_deck}")

