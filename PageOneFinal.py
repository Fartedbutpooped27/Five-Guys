import random
import re
 
  
CARDS = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace": 14
}
 
FACES = [
    "Spades",
    "Clubs",
    "Diamonds",
    "Hearts"]

#CREAT DECK FUNCTION
def createdeck():
    """Function to create the entire deck.
    
    Side effects:
        append cards from the file to the deck
    
    Returns:
        deck (str): returns a deck as a string with all of the cards from the file
    """
    deck = []
    file = "deck.txt"
    with open(file, 'r', encoding = 'utf-8-sig') as f:
        lines = f.read().splitlines()
        for line in lines:
            line.strip('\n')
            line.strip('ufeff')
            deck.append(line)
    return deck
   
class GameState:
    """A class for representing the state of the game
    
    Attributes:
        deck (str) : a deck with all the cards as a string
            
    Methods:
        repr (self): returns the current top card as a string
        dealcard (path): deals a card to the hand until the count equals 0
        draw_card (hand): draws a card to the hand 
        Current_top_card (card_suit): shows the current top card
        roundWinner (player1): displays the winner of the current round
        roundWinner (player2): displays the winner of the current round
        restock (self): changes the value of a class attribute 
        game_winner (p1hand): displays the winner of the game
        game_winner (p2hand): displays the winner of the game
        isCardValid (card): returns true if the card is the top suit and false if it is not
    """  
    def __init__(self):
        """Constructs all the necessary attributes for the gamestate object

        Args:
            top_suit (str): the top suit
            high_card (str): the highest card
            trick (list): the discard pile
            stock (list): the draw pile
        
        Side effects:
            initializes the top_suit, high_card, trick, and stock variables
        """
        self.top_suit = ""
        self.high_card = ""
        self.trick = []
        self.stock = []
        #for i in deck:
        #  self.stock.append(i)
        deck = createdeck()
        self.stock = [i for i in deck] #LIST COMPREHENSION
        
    def __repr__(self):
        """Return a formal representation of the gamestate object."""
        return (f"The current top card is: {self.top_card}")

    def deal_hand(self):
        """Draws a card to the hand
        
        Side effects:
            append cards from the deck to the hand
            removes the drawn card from the draw pile

        Returns:
            Returns the hand which contains the cards which have been dealed
        """
        hand = []
        count = 4
        while count > 0:
            new_card = random.choice(self.stock)
            hand.append(new_card)
            self.stock.remove(new_card)
            count -= 1
        return hand
            
    def draw_card(self, hand):     
        """Draws a card to the hand 
        
        Args:
        hand (list): a list which contains all the cards that the player has
        
        Side effects:
            append cards from the deck to the hand if the new card is not the top suit
            removes the drawn card from the draw pile if the new card is not the top suit
            removes the drawn card from the hand if the new card is the top suit

        Returns:
            Returns the hand which contains new card that has been drawn
        """
        #suit = []
        hand = []
        new_card = random.choice(self.stock)
        self.stock.remove(new_card)
        valid = False
        while valid == False:
          #print(f"new card 1 {new_card}")
          hand.append(new_card)
          if self.top_suit not in new_card:
            #hand.append(new_card)
            new_card = random.choice(self.stock)
            #print(f"new card 2 {new_card}")
            self.stock.remove(new_card)
          else:
            #hand.remove(new_card)
            #hand.append(new_card)
            valid = True
        print(f"Player played {new_card}\n")
        #print(f"HAND: {hand}")
        return hand, new_card
   
    def current_top_card(self, card_suit, card_num):
        """Shows the current top card
        
        Args:
        card_suit (str): a string which shows the suit of the current card

        Side effects:
            initializes the top_suit variable
            
        """
        self.top_suit = card_suit
        self.high_card = card_num
        self.top_card = (f"{self.high_card} {self.top_suit}")
    
    def round_winner(self, player1, player2):
        """Displays the winner of the current round
        
        Args:
        player1 (str): the first player displayed as a string
        player2 (str): the second player displayed as a string

        Returns:
            Returns 0 if the winner is player1 and returns 1 if the winner is player2
        """ 
        cards = [player1, player2]
        winner = max (cards, key= lambda x: CARDS[x]) #Lambda
        if winner == player1:
            return 0
        else:
            return 1
     
    def restock(self):
        """Changes the value of a class attribute 

        Returns:
            Returns none
        """
        for card in self.trick:
            self.stock.append(card)
            self.trick.remove(card)
           
    def game_winner(self, p1hand, p2hand):
        """Displays the winner of the game
        
        Args:
        p1hand (str): a string which contains the cards in the player 1's hand
        p2hand (str): a string which contains the cards in the player 2's hand 

        Returns:
            Returns the winner of the game 
        """ 
        winner = "Player 1" if p1hand == [] else "Player 2" if p2hand == [] else None
        return winner
  
    def isCardValid(self, card):
        """Determines whether the card is the top suit
        
        Args:
        card (str): the current card

        Returns:
            Returns true if the card is the top suit and false if it is not
        """ 
        if card == self.top_suit:  
            return True
        else:
            return False
   
   
class Player:
    """A class for representing the player 
    
    Attributes:
        deck (str) : a deck with all the cards as a string
        player_name (str) : the player name represented as a string
    """  
    def __init__(self, player_name="no_name"):
        """Constructs all the necessary attributes for the player object

        Args:
            player_name (str): the player name 
            hand (list): a list which contains all the cards that the player has
            top_card (str): the top card
            chosenCard (str): the card that is chosen 
            suits (list): a list of suits of each card in current hand
            nums (list): a list of the face values of each card in current hand
            playablecards (list): a list of all the cards that are playable
            play_card (str): the card that is played represented as a string
            card_index (int): the index of the card which has a default value of 0 
            
        
        Side effects:
            initializes the player_name, hand, top_card, chosenCard, suits, nums, playablecards, play_card, and card_index variables
        """  
        self.player_name = player_name
        self.hand = []
        self.top_card = ""
        self.chosenCard = ""
        self.suits = []
        self.nums = []
        self.playablecards = []
        self.play_card = ""
        self.card_index = 0

    def playable_cards(self, game):
        """takes gamestate (initialized in main statement) and returns
        a list of any playable cards
            
        Args:
            game (GameState) : current gamestate
        """
        #check for playable cards
        print(f"TOP SUIT: {game.top_suit}\n")
        count = 0
        for item in self.suits:
            if item == game.top_suit:
                self.playablecards.append(f"{self.nums[count]} {item}")
            count += 1
    
    def nums_and_suits(self, hand):
        """uses regex to separate the suits and faces of the cards into two lists
        
        Args:
            hand (list) : the list to use for regex
            
        Side effects:
            appends to self.nums list and self.suits lists
        """
        expr = r"(?P<cardValue>^\S*)\s(?P<suitValue>\S*)"
        for element in hand:
            match = re.search(expr, element)
            cardValue = match.group("cardValue")
            suitValue = match.group("suitValue")
            self.suits.append(suitValue)
            self.nums.append(cardValue)    
   
class Human(Player):
    """A class for representing the human player
            
    Methods:
        take_turn (self): engages in a full turn of the game
    """ 
    def take_turn(self, gamestate):
        """Engages in a full turn of the game

        Side effects:
            appends the value of the suit to suits
            appends the value of the  card to nums
            appends the card to playable cards if it is playable
            removes the played card from the hand if the played card is valid
        """ 
        #get gamestate
        #check player's hand for playable cards
        #if none, draw till playable card
        #else, let player play a card
        #call isCardValid and return error till player plays valid card
        #remove played card from hand
        #pass new attributes into a current_gamestate variable (current top card, current stock, current trick, current high card, current winner)
        #print player's hand
        #print(f"Top Suit: {gamestate.top_suit}\n") THIS NEEDS TO BE IN THE MAIN NOT IN THE PLAYER CLASS
        print(f"start turn hand: {self.hand}\n")
        
        #set up self.nums, self.suits, and self.playablecards
        self.suits = []
        self.nums = []
        self.nums_and_suits(self.hand)
        self.playable_cards(gamestate)
        
        if self.playablecards == [] and gamestate.top_suit != "":
            print("you must draw until playable card appears\n")
            lyst, new_card = gamestate.draw_card(self.hand)
            print(new_card)
            for i in lyst:
                self.hand.append(i)
            gamestate.trick.append(new_card)
            gamestate.current_top_card(self.card_suit, self.card_num)
            self.hand.remove(new_card)
        else:
            #play card
            self.play_card = int(input("please enter the index of a card to play: \n"))
            self.card_suit = self.suits[self.play_card]
            self.card_num = self.nums[self.play_card]
            val = False
            while val == False:
                if gamestate.isCardValid(self.suits[self.play_card]) or gamestate.top_suit == "":
                    gamestate.current_top_card(self.card_suit, self.card_num)
                    gamestate.trick.append(self.hand[self.play_card])
                    self.hand.remove(self.hand[self.play_card])
                    val = True
                else:
                    self.play_card = int(input("invalid entry, try another card: \n"))
               
class Computer(Player):
    """A class for representing the computer player
            
    Methods:
        take_turn (self): engages in a full turn of the game
    """  
    def take_turn(self, gamestate):
        """Engages in a full turn of the game

        Side effects:
            appends the value of the suit to suits
            appends the value of the  card to nums
            appends the card to playable cards if it is playable
            removes the played card from the hand if the played card is valid
        """ 
        print(f"start turn hand COMPUTER: {self.hand}\n")
            
        #set up self.nums, self.suits, and self.playablecards
        self.suits = []
        self.nums = []
        self.nums_and_suits(self.hand)
        self.playable_cards(gamestate)   
           
        if self.playablecards == []: # and gamestate.top_suit != "":
            print("Computer must draw until playable card appears\n")
            lyst, new_card = gamestate.draw_card(self.hand)
            for i in lyst:
                self.hand.append(i)
            self.play_card = new_card
            self.nums_and_suits(lyst)
            gamestate.trick.append(self.play_card)
            self.card_suit = self.suits[self.hand.index(self.play_card)]
            self.card_num = self.nums[self.hand.index(self.play_card)]
            gamestate.current_top_card(self.card_suit, self.card_num)
            self.hand.remove(self.play_card)
        else:
            #play card
            self.play_card = self.playablecards.index(random.choice(self.playablecards))
            self.card_suit = self.suits[self.play_card]
            self.card_num = self.nums[self.play_card]
            val = False
            while val == False:
                if gamestate.isCardValid(self.card_suit) or gamestate.top_suit == "":
                    gamestate.current_top_card(self.card_suit, self.card_num)
                    gamestate.trick.append(self.hand[self.play_card]) #gamestate.trick.append(self.hand[self.play_card])
                    self.hand.remove(self.hand[self.play_card]) #self.hand.remove(self.hand[self.play_card])
                    val = True
                else:
                    self.play_card = self.playablecards.index(random.choice(self.playablecards))
                    self.card_suit = self.suits[self.play_card]
                    self.card_num = self.nums[self.play_card]
 
if __name__ == "__main__":
    print("Welcome to Page One!\n")
    
    #create GameState object
    gamestate = GameState()
    
    #get player 1 name and create human player class
    lyst = [input("Enter the name of player 1 (Human Player): \n"), 
    input("Enter the name of player 2 (Computer Player): \n")]
    player1name, player2name = lyst
    human = Human(player1name)
    computer = Computer(player2name)

    #deal hands
    players = (human, computer)
    for item in players:
        new_hand = gamestate.deal_hand()
        for card in new_hand:
            item.hand.append(card)

    #BIG LOOP RUNNING THE GAME
    ##########################
    #begin loop, set play = False later to end game/while loop
    play = True
    player = 0 #sets game to have player 1 go first
    print(f"{player1name} goes first!\n") #tells player to go first
    while play:
        #reset top_suit
        gamestate.top_suit = ""
        #run each player's turn
        if player == 0:
            #print(f"Top Suit: {gamestate.top_suit}\n")
            print(f"NEW ROUND: {player1name}'S TURN\n")
            human.take_turn(gamestate)
            print(f"New Top Card: {gamestate.top_card}\n")
            computer.take_turn(gamestate)
        elif player == 1:
            #print(f"Top Suit: {gamestate.top_suit}\n")
            print(f"NEW ROUND: {player2name}'S TURN\n")
            computer.take_turn(gamestate)
            print(f"New Top Card: {gamestate.top_card}\n")
            human.take_turn(gamestate)
        #see if either player won the game (empty hand)
        player = gamestate.round_winner(human.nums[human.play_card], computer.nums[-1])
        winner = gamestate.game_winner(human.hand, computer.hand)
        #UPDATE TOP CARD
        if winner == None:
            pass
        elif winner == "Player 1":
            print(f"Congrats {player1name}!! You hsve won this game of Page One! See you next time!")
            play = False
        elif winner == "Player 2":
            print(f"Congrats {player2name}!! You hsve won this game of Page One! See you next time!")
            play = False    

    #END GAME STATEMENT
    print("Thank you for playing Page One!\n")