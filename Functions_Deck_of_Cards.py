import random

def get_suit():
    """Returns a random playing spanish card suit."""
    choice = random.randint(1, 4)

    if choice == 1:
        return "Clubs"
    elif choice == 2:
        return "Cups"
    elif choice == 3:
        return "Coins"
    else:
        return "Clubs"

def get_rank(include_face_cards):
    """Returns a random playing
    card rank."""
    if include_face_cards:
        num = random.randint(1, 13)
    else:
        num = random.randint(2, 10)

    if num == 1:
        return "Ace"
    elif num == 11:
        return "Jack"
    elif num == 12:
        return "Queen"
    elif num == 13:
        return "King"

    return str(num)

def draw_card(include_face_cards):
    """Returns a random playing card in string format."""
    return get_rank(include_face_cards) + " of " + get_suit()

def draw_hand(num_cards, include_face_cards):
    """Returns a random hand of cards of the given size."""
    hand = ""
    for card in range(num_cards):
        hand += draw_card(include_face_cards) + "\n"

    return hand


print(draw_hand(5, False))
print(draw_hand(7, True))
