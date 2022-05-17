• An explanation of the purpose of each file in your repository
• Clear instructions on how to run your program from the command line
• Clear instructions on how to use your program and/or interpret the output of the program, as applicable
• Attribution: in order to evaluate whether each member has made a substantial, original contribution to the project, please clearly and unambiguously indicate who is the primary author of each major function/method. You do not need to attribute minor program components, such as an if name == "main": statement.
• An annotated bibliography of all sources you used to develop your project. For each source, explain how you used the source.

REPOSITORY FILES
The first file, "PageOneFinal", contains our methods and classes required to run the game/program. The second file, "deck", is a text file containing the deck of cards that we imported into "PageOneFinal". 

RUNNING THE GAME AND INTERPRETING THE OUTPUT
When beginning to run the program you will be met with the "Welcome to Page One!" and then "Enter the name of player 1 (Human Player):", here you will enter your name. Then you will be met with "Enter the name of player 2 (Computer Player):", here you will enter the name of the computer player. The human player will always go first, so the next output will be the human player's hand, then an input for what card to play. For this, you will need to input the index (an integer) of the card you would like to play from your hand. If the card is invalid, you will have to try again till you enter a valid card to play. Next, the computer will automatically take its turn and the program will show you its hand and what it played, as well as the new top card. This will go on till one player empties their hand and wins the game.

ATTRIBUTIONS:
Before listing attributions, we must our troubles with GitHub. As Ben met with you and discussed, some of the code was written in separate files before being pasted to thee program. We know this was poor practice and have since corrected ourselves. To make up for this pasted code, each group member will have at least one commit which lists the methods they wrote. Otherwise, each important commit will explain the changes made
Logan: Player.playable_cards
       Player.nums_and_suits

Alex: GameState.isCardValid
      GameState.__repr__
      GameState.__init__

Jay: createdeck
     GameState.draw_card
     GameState.restock
     Player.__init__

Jon: GameState.round_winner
     GameState.game_winner

Ben: GameState.current_top_card
     GameState.deal_hand
     Human.take_turn
     Computer.take_turn


ANNOTATED BIBLIOGRAPHY


McLeod, John. “Page One.” Card Game Rules, 8 May 2009, 
https://www.pagat.com/inflation/page_one.html.

We used this website to gain a better understanding of how the card game Page One is played. Using information provided by author John McLeod, we were able to write out all aspects of our code smoothly and efficiently. 