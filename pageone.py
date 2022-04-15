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

class gameplay():
    def __init__(self, card):
        """"""
    
    def isCardValid(self, playerHand):
        
    def draw(self):
        
    def winRound(self):
        
    def winner(self):
        
        
      
        
    
    
        
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
    
    def take_turn(self, gameplay):
        """Player takes their turn
        
        Args:
            gameplay (object): the current state of the game
            
        Return:
            str: a string of what happened in the turn
            
        """
        
class Computer(Player):
    """ """
    
    def numPlayer(self, players):
        """ """
    def take_turn(self, gameplay):
        """ """