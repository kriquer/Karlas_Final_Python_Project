README Pedrito Card Game Code
1. Overview   
Pedrito is a turn-based card game based on traditional Spanish playing cards.
Each player holds 4 face-down cards, and the objective is to finish the game with the lowest total points. A player may end the game at the start of it’s turn by calling “Pedrito”.
This project was developed as a final project for a Python class.

2. Installation & Requirements
The game is written in Python.
 •	Developed using PyCharm 2025 (version 2.1.1)
 •	Required Python libraries:
    • random (standard library)  
 •	There is no graphical interface yet. The game runs entirely in the PyCharm (or terminal) console.

To play:
  1.	Open the project in PyCharm
  2.	Run Project.py
  3.	Play by following the prompts in the console

3. How the Game works
-	Spanish Deck
    The game is based on Spanish playing cards. There are 4 suits “Swords”, “Clubs”, “Cups” and “Coins” with 12 cards each with values are from 1-12. Additionally, there are 2 “0” Cards that don’t have a suit (Jokers), these cards are not used in this game for now.
-	Setting up the game:
	 • Each player is dealt 4 cards, placed in a 2x2 grid:
      •	Position 1: top left
      • Position 2: top right
      • Position 3: bottom left
      •	Position 4: bottom right
  •	At the beginning of the game, each player may look at cards 3 and 4 (their bottom row. After that the cards will stay facedown for everybody except for the actions that can occur during a turn.
-	Turns:
    At the beginning of the turn there are 3 options:
      •	“Call Pedrito”: If Pedrito is called all cards are turned face up. The points of the 4 cards of each player’s hands are summed up. If the player who called Pedrito has the lowest points they win.
      •	Take a card from the deck: The card that the player draws is seen by everyone. The player has three options: 
          •	Discard the drawn card and put it faceup on the top of the graveyard.
          •	Exchange the card with one of its own cards. The drawn card is exchanged with one of the players cards of the players choice. The card that used to be the players card is put faceup on the top of the graveyard.
            Exceptions are for the following cards:
                •	If a 7 card is drawn the player must put it faceup on the top of the graveyard. The player and only the player can look at one of its own players cards. After the card is put back in its place facedown.
                •	If an 8 card is drawn the player must put it faceup on the top of the graveyard. The player and only the player can look at one of the opponent’s cards. After the card is put back in its place facedown.
                •	If a 9 card is drawn the player must put it faceup on the top of the graveyard. The player can exchange one of its own cards with one belonging to another player.
          •	Exchange the last card in the graveyard deck with one of the players own cards (not yet implanted)

-	End of game:
The game ends when a player calls Pedrito. All cards are revealed, points are summed, and if the player who called “Pedrito” has the lowest total of points they win.

-	How to play the game on Python: 
The game is being played by responding to the prompts on the console. A player must give a name. To choose actions in a turn the letters “A” and “B” are used. To choose cards to exchange the number 1-4 are used. Read prompts carefully.

5. Known issues / limitations
  -	Only single-player vs computer supported
  -	No graphical interface
  -	Cannot adjust:
    •	Number of players
    •	Computer difficulty
    •	Language (English only)
    •	Statistics/tracking of wins
  -	Deck is not recycled — if it becomes empty, the game ends
  -	Option to take the top graveyard card is not yet implemented
    
6. Author / Acknowledgements
Created by:
Karla Riquer
Special Thanks:
  •	REDI School Munich teachers
  •	ChatGPT (assistance with debugging and code syntax)


