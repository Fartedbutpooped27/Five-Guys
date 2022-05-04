#python code for page one
import random

CARDS = {
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace": 14,
    "Joker": 15
}

FACES = {
    "Spades",
    "Clubs",
    "Diamonds",
    "Hearts"
}

class Pageone():
    """Class that initializes the Page One game

    Attributes:
        player (str): the player
        stockDeck (list): list which contains all of the cards which has been randomized

    Methods:
        stock(stockDeck): randomizes all the cards in the deck 
        dealCard(playerHand): deals the card out to the player and then puts the cards in an empty list
    """
    def init(self, player):
        """Method that initializes the player variable

        Attributes:
            player (str): the player represented as a string

        Returns:
            Returns a value of None
        """
        return None
    def stock(self, stockDeck):
        """Method randomizes all the cards in the deck

        Attributes:
            stockDeck (list): list which contains all of the cards which has been randomized

        Side Effects:
            A list containing all of the cards which has been randomized 
        """
        allCards = ["""all cards in deck"""]
        random.allCards
    def dealCard(self, playerHand):
        """Method which deals cards to the player hand

        Attributes:
            playerHand (list): list which contains the cards that has been dealed to them

        Side Effects:
            A list containing all of the cards which has been dealed to them
        """
        self.playerHand = []
    def playround(self):
        """Manages one round of gameplay
    
        Side effects:
            prints the card with the highest value   
        """
    def gameover(self):
        """Determine whether the game is over
        
        The game is over when one player's hand is empty
        
        Returns:
            bool: True if the game is over, otherwise false.
        """
    def play(self):
        """manage game play.
            
        After each round, ask players if they would like to play again
            
        Side effects:
        Displays information in the terminal.
        resets player's hands
        """
    def play_again(self):
        """Ask players if they would like to play another round.

        Returns:
            bool: True if players choose to keep playing, otherwise False.
    
        Side effects:
        Displays information in the terminal.
            """

class gameplay():
    """class that manages the gameeplay of pageone"""
    def __init__(self):
        """initalizes the gameplay class"""
        self.card = []
        for c in CARDS:
            for f in FACES:
                self.card.append(c,f)
    
    def isCardValid(self, card, currentCard):
        """validates whether a card is playable at a given moment
        
        Args:
            card (str) : a given card a player wants to lay down for their turn
            currentCard (str) : The most current card on the trick
        Raises:
            ValueError: the face of the card does not match
        Side effects:
            prints the reason why the card can not be placed
        """
        if card[1] != currentCard[1]:
            print("The face does not match the other cards")
            raise ValueError 
        
    def draw(self, playerHand):
        """draws a card from the stock
        
        Args:
            playerHand (dict) : the player's current hand
            
        Returns:
            None
        """
        drawn = random.choice(self.card)
        playerHand += drawn
        
    def winRound(self, gameplay):
        """Determines who wins the round
        
        Args:
            gameplay (object) : the current state of the game
        
        Returns:
            round_winner (str) : the winning player
        """
        
    def winner(self, gameplay):
        """Determines who wins entire game
        
        Args:
            gameplay (object) : current state of game
            
        Returns:
            winner (str) : winner of whole game
        """
        
class Player():
    """Abstract base class for a Page One player.
    
    Attributes:
        player_name (str): the player's name.
    """
    def __init__(self, player_name):
        self.player_name = player_name   
    
class Human(Player):
    """Class for the human player 
    
    Attributes:
        name (str): the player's name
    """
    
    def take_turn(self, gameplay, playerHand):
        """Player takes their turn
        
        Args:
            gameplay (object): the current state of the game
            
        Returns:
            str: a string of what happened in the turn
            
        """
       #print player's hand
       #if no playable cards, make player draw until playable card drawn
       #else player tries to play a card
       #check if card is playable
       #if not, tell player to try again
       #remove card from player's hand
       #make card played into the new top of deck
       #change player turn to computer player
        for card in playerHand:
            if gameplay.isCardValid(card, gameplay.top_card)
            
        
        
class Computer(Player):
    """Instance of Player which controls computer player"""
    
    def numPlayer(self, players):
        """ """
    def take_turn(self, gameplay):
        """Takes turn for computer player
        
        Args:
            gameplay (object) : current state of game
            
        Returns:
            turn (str) : explanation of the player's turn
        """