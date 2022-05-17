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

#deck = []
#discard = []
#hand = []
#letterName = list(CARDS.keys())
 
#fill draw_pile
#for f in FACES:
#   for i in letterName:
#        deck.append(f"{i} {f}")

#CREAT DECK FUNCTION
def createdeck(file):
    deck = []
    file = "deck.txt"
    with open(file, 'r', encoding = 'utf-8') as f:
        for line in f:
            deck.append(line)
    return deck

        
#regex that match group suits and card values
#this should go in the deal_hand() method
#expr = r"(?P<cardValue>^\S*)\s(?P<suitValue>\S*)"
#for element in deck:
#    match = re.search(expr, element)
#    cardValue = match.group(0)
#    suitValue = match.group(1)
   
class GameState:
    """DOCSTRINGGGGG """ 
    def __init__(self, deck):
        """DOCSTRINGGGGG """ 
        self.top_suit = ""
        self.high_card = ""
        self.top_card = (f"{self.high_card} {self.top_suit}")
        self.trick = []
        self.stock = []
        #for i in deck:
        #  self.stock.append(i)
        deck = createdeck()
        self.stock = [i for i in deck] #LIST COMPREHENSION
        
    def __repr__(self):
        """DOCSTRINGGGG """
        return (f"The current top card is: {self.top_card}")

    def dealCard(self):
        hand = []
        count = 4
        while count > 0:
            new_card = random.choice(self.stock)
            hand.append(new_card)
            self.stock.remove(new_card)
            count -= 1
        return hand
            
    def draw_card(self, hand):     
        """DOCSTRINGGGGG """
        #suit = []
        new_card = random.choice(self.stock)
        valid = False
        while valid == False:
          #print(f"new card 1 {new_card}")
          if self.top_suit not in new_card:
            new_card = random.choice(self.stock)
            #print(f"new card 2 {new_card}")
            hand.append(new_card)
            self.stock.remove(new_card)
          else:
            hand.remove(new_card)
            valid = True
        print(f"you played {new_card}\n")
        return hand
   
    def Current_top_card(self, card_suit):
        """DOCSTRINGGGGG """ 
        self.top_suit = card_suit
    
    def roundWinner(self, player1, player2):
        """DOCSTRINGGGGG """ 
        cards = [player1, player2]
        winner = max (cards, key= lambda x: CARDS[x]) #Lambda
        if winner == player1:
            return 0
        else:
            return 1
       
        
    def restock(self):
        """DOCSTRING"""
        for card in self.trick:
            self.stock.append(card)
            self.trick.remove(card)
           
    def game_winner(p1hand, p2hand):
        """DOCSTRINGGGGG """ 
        winner = "Player 1" if p1hand == [] else "Player 2" if p2hand == [] else None
        return winner
  
    def isCardValid(self, card):
        """DOCSTRINGGGGG """ 
        if card == self.top_suit:  
            return True
        else:
            return False
   
   
class Player:
    """DOCSTRINGGGGG """ 
    def __init__(self, deck, player_name="no_name"):
        """DOCSTRINGGGGG """ 
        #init player name
        self.player_name = player_name
        self.stock = []
        self.hand = []
        self.top_card = ""
        self.chosenCard = ""
        self.suits = []
        self.nums = []
       
        for i in deck:
            self.stock.append(i)
       
        # self.starting_hand = []       
   
class Human(Player):
    """DOCSTRINGGGGG """ 
    def take_turn(self):
        """DOCSTRINGGGGG """ 
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
       
        #create match groups for future use
        #^DONE IN Player CLASS INIT
        #self.suits = []
        #self.nums = []
        
        expr = r"(?P<cardValue>^\S*)\s(?P<suitValue>\S*)"
        for element in self.hand:
            match = re.search(expr, element)
            cardValue = match.group("cardValue")
            suitValue = match.group("suitValue")
            self.suits.append(suitValue)
            self.nums.append(cardValue)
       
        #check for playable cards
        current_gamestate = GameState(self.stock)
        playableCards = []
        count = 0
        for item in self.suits:
            if item == current_gamestate.topSuit:
                playableCards.append(f"{self.nums[count]} {item}\n")
            count += 1
       
        if playableCards == []:
            print("you must draw until playable card appears\n")
            self.hand = current_gamestate.draw_card(self.hand)
            print(f"your new current hand: {self.hand}\n")
        else:
          #play card
          play_card = int(input("please enter the index of a card to play: \n"))
          self.card_suit = self.suits[play_card]
          self.card_num = self.nums[play_card]
          val = False
          while val == False:
            if current_gamestate.isCardValid(self.suits[play_card]):
                  self.hand.remove(self.hand[play_card])
                  val = True
            else:
                play_card = int(input("invalid entry, try another card: \n"))
               
class Computer(Player):
    """DOCSTRINGGGGG """ 
    def take_turn(self):
        """DOCSTRINGGGGG """ 
        print(f"Top Suit: {self.topSuit}\n")
        print(f"start turn hand: {self.hand}\n")
       
        #create match groups for future use
        #^DONE IN Player CLASS INIT
        #self.suits = []
        #self.nums = []
        
        expr = r"(?P<cardValue>^\S*)\s(?P<suitValue>\S*)"
        for element in self.hand:
            match = re.search(expr, element)
            cardValue = match.group("cardValue")
            suitValue = match.group("suitValue")
            self.suits.append(suitValue)
            self.nums.append(cardValue)
           
        current_gamestate = GameState(self.stock)
        playableCards = []
        count = 0
        for item in self.suits:
            if item == current_gamestate.topSuit:
                playableCards.append(f"{self.nums[count]} {item}\n")
            count += 1
           
        if playableCards == []:
            self.hand = current_gamestate.draw_card(self.hand)
        else:
          #play card
          play_card = random.choice(playableCards)
 
if __name__ == "__main__":
    #stock = []
    #for i in deck:
    #   stock.append(i)
   
    player1_name = input("input first player's name: \n")
    player2_name = input("input first player's name: \n")
   
    player1 = Human(player1_name, stock)
    for card in player1.hand:
        stock.remove(card)
    player2 = Computer(player2_name, stock)
    for card2 in player2.hand:    
        stock.remove(card2)
   
    game = True
    player = 0
    while game:
       
        if player1.hand == [] or player2.hand == []:
            GameState.game_winner()
            game = False
               
        elif player == 0:
            player1.take_turn()
            player2.take_turn()
            #top_card = player1.top_card
            #player = 1 - player
        elif player == 1:
            player2.take_turn()
            player1.take_turn()
            #top_card = player2.top_card
            #player = 1 - player
     
       
        player = GameState.round_winner(player1.card_num, player2.card_num)
       

