#The start to my project
from random import randint
import decks
import player
import functions_error_handling

if __name__ == "__main__":
    #hello
    print("Hello World")

    #makes a deck of spanish cards
    spanish_deck = decks.Deck()
    spanish_deck.shuffle()

    #makes a graveyard deck
    graveyard_deck = []

    #p1 means Player 1
    p1_name = input("What do you want to be called? ")
    p1_hand = spanish_deck.deal(4) #deals 4 cards to player
    p1 = player.Human_Player(p1_name, p1_hand)

    cpu_hand = spanish_deck.deal(4) #deals 4 cards to computer
    cpu = player.Computer_Player("Computer", cpu_hand)

    ##Test to see computer's hand
    #print(f"Test for computer's hand {cpu.hand}")
    ##Test to see player1's hand
    #print(f"Test for player {p1}'s hand {p1.hand}")

    print(f"Nice. Now let's play some Pedrito {p1}! Don't forget to call Pedrito "
          f"when you think you have less points than the other players.")
    print(f"Your last two cards are {p1.hand[2:]}")

    for i in range(1000):
        #Player1 goes first
        p1_choice = functions_error_handling.get_choice("Your turn! Want to call Pedrito or take a card? Choose A for calling Pedrito or B for taking a card. ", ["A", "B"])
        if p1_choice.upper() == "A":
            p1.points_hand(p1.hand)
            cpu.points_hand(cpu.hand)
            print(f"{p1} calls Pedrito! {p1} has {p1.points_hand(p1.hand)} points and the computer player has {cpu.points_hand(cpu.hand)} points. ")
            if p1.points_hand(p1.hand) < cpu.points_hand(cpu.hand):
                print("Congrats! You won Pedrito! ")
            else:
                print(f"Sorry {p1} you lost. ")#Future add on: if lost add loop to restart game if player wants
            break
        if p1_choice.upper() == "B":
            #deal a card to player 1
            dealt_card = spanish_deck.deal(1)
            dealt_card = dealt_card[0]  # first take card out of list
            print(f"You drew a {dealt_card}")
            if spanish_deck.points_dealt_card(dealt_card) == 7 or spanish_deck.points_dealt_card(dealt_card) == 8 or spanish_deck.points_dealt_card(dealt_card) == 9:
                p1.cards_789(cpu, dealt_card, graveyard_deck)
            else:
                p1_card_choice = functions_error_handling.get_choice(
                "What do you want with your card? A: Discard the card to the graveyard deck? B: Exchange card with one of your cards? ",
                ["A", "B"]
                )
                if p1_card_choice.upper() == "A":
                    #take card from Player's hand and discard into top(first position in list) of graveyard deck
                    graveyard_deck.insert(0, dealt_card)
                elif p1_card_choice.upper() == "B":
                  #switch card in Player's hand
                    pos = functions_error_handling.get_int_input("Which card do you want to switch, card in position 1, 2 ,3 or 4? ", 1, 4)
                    #switches card with chosen card by player
                    if pos == 1:
                        p1.exchange_card(dealt_card, 0,  graveyard_deck)
                    elif pos == 2:
                        p1.exchange_card(dealt_card, 1, graveyard_deck)
                    elif pos == 3:
                        p1.exchange_card(dealt_card, 2, graveyard_deck)
                    else:
                        p1.exchange_card(dealt_card, 3, graveyard_deck)

        #print(f"Test to check player's {p1}'s hand {p1.hand}")

        print(f"Graveyard deck so far has {graveyard_deck}")

        #start of computer's turn
        print("Now it is my turn!")
        #computer chooses to call Pedrito or not depending on total points with some randomization
        cpu.points_2cards(cpu.hand)
        p1.points_hand(p1.hand)

        #test to get points of front cards in computer's hand
        #print(f"Test for sum of computer's lower cards {cpu.points_2cards(cpu.hand)}")

        #randomize if computer calls Pedrito if cards are low
        random_choice = randint(1, 10)
        if cpu.points_2cards(cpu.hand) <= 4 and random_choice <= 7:
            print(f"{cpu} calls Pedrito! {p1} has {p1.points_hand(p1.hand)} points and the computer player has {cpu.points_hand(cpu.hand)} points. ")
            if p1.points_hand(p1.hand) <= cpu.points_hand(cpu.hand):
                print("Computer lost!" )
            elif cpu.points_hand(cpu.hand) < p1.points_hand(p1.hand) :
                print("Computer won!")
            break

        #if computer does not call Pedrito deal a card to computer
        dealt_card = spanish_deck.deal(1)
        print(f"The computer drew a {dealt_card}")
        dealt_card = dealt_card[0] #makes card not a list variable
        points_dealt_card = decks.Card.card_points(dealt_card) #gets point value of the dealt card

        #test to get point value of 1 card
        #print(points_dealt_card)

        '''Computer's choices for it's dealt card are:
            Discard card to graveyard deck
            Exchange card with one of it's own cards
            With 7 or 8 cards it does nothing
            With 9 cards it randomly changes a card in it's own hand with one from another player's hand'''
        random_choice = randint(1, 10)
        if points_dealt_card >= 10:
            #discards card into graveyard deck
            graveyard_deck.insert(0, dealt_card)
        elif spanish_deck.points_dealt_card(dealt_card) == 7 or spanish_deck.points_dealt_card(dealt_card) == 8 or spanish_deck.points_dealt_card(dealt_card) == 9:
                cpu.cards_789(p1, dealt_card, graveyard_deck)
        elif random_choice < 7: #this means computer remembers cards 2 and 3
            #puts dealt card in position 2 or 3 of computer's hand
            #first have to return value of cards in computer's hand
            values = cpu.get_card_values()
            #print("Test for card values list", values)
            points_card2 = values[2]
            points_card3 = values[3]
            if points_dealt_card < points_card2 and points_card2 >= points_card3:
               #exchange the card in position 2 and add discarded card into graveyard deck
                cpu.exchange_card(dealt_card, 2,  graveyard_deck)
            elif points_dealt_card < points_card3 and points_card3 >= points_card2:
               #exchange the card in position 3 and add discarded card into graveyard deck
                cpu.exchange_card(dealt_card, 3,  graveyard_deck)
            else: #computer knows cards 2 and 3 are low so wants to exchange with unknown cards 0 and 1
                if points_dealt_card <= 4:
                    position = randint(0, 1)
                    cpu.exchange_card(dealt_card, position,  graveyard_deck)
                else:
                    graveyard_deck.insert(0, dealt_card)
        elif points_dealt_card <= 4: #computer does not remember any cards so wants to exchange with any card
            position = randint(0, 3)
            cpu.exchange_card(dealt_card, position,  graveyard_deck)
        else: #discard dealt card into graveyard deck
            graveyard_deck.insert(0, dealt_card)

        #print(f"Test to check computer's's hand {c.hand} ")
        print(f"Graveyard deck so far has {graveyard_deck}")

