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
def createdeck():
    deck = []
    file = "deck.txt"
    with open(file, 'r', encoding = 'utf-8-sig') as f:
        lines = f.read().splitlines()
        for line in lines:
            line.strip('\n')
            line.strip('ufeff')
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
    def __init__(self):
        """DOCSTRINGGGGG """ 
        self.top_suit = ""
        self.high_card = ""
        self.trick = []
        self.stock = []
        #for i in deck:
        #  self.stock.append(i)
        deck = createdeck()
        self.stock = [i for i in deck] #LIST COMPREHENSION
        
    def __repr__(self):
        """DOCSTRINGGGG """
        return (f"The current top card is: {self.top_card}")

    def deal_hand(self):
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
        """DOCSTRINGGGGG """ 
        self.top_suit = card_suit
        self.high_card = card_num
        self.top_card = (f"{self.high_card} {self.top_suit}")
    
    def round_winner(self, player1, player2):
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
           
    def game_winner(self, p1hand, p2hand):
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
    def __init__(self, player_name="no_name"):
        """DOCSTRINGGGGG """ 
        #init player name
        #self.stock = []
        #for i in deck:
        #    self.stock.append(i)
        # self.starting_hand = []  
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
        #current_gamestate = GameState(self.stock)
        #playableCards = []
        print(f"TOP SUIT: {game.top_suit}\n")
        count = 0
        for item in self.suits:
            if item == game.top_suit:
                self.playablecards.append(f"{self.nums[count]} {item}")
            count += 1
    
    def nums_and_suits(self, hand):
        """DOCSTRINGGG"""
        #self.suits = []
        #self.nums = []
        expr = r"(?P<cardValue>^\S*)\s(?P<suitValue>\S*)"
        for element in hand:
            match = re.search(expr, element)
            cardValue = match.group("cardValue")
            suitValue = match.group("suitValue")
            self.suits.append(suitValue)
            self.nums.append(cardValue)    
   
class Human(Player):
    """DOCSTRINGGGGG """ 
    def take_turn(self, gamestate):
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
        
        #set up self.nums, self.suits, and self.playablecards
        self.suits = []
        self.nums = []
        self.nums_and_suits(self.hand)
        self.playable_cards(gamestate)
        #print(f"NUMS LIST: {self.nums}")
        #print(f"SUITS LIST: {self.suits}")
        
        if self.playablecards == [] and gamestate.top_suit != "":
            print("you must draw until playable card appears\n")
            #self.hand = gamestate.draw_card(self.hand)
            lyst, new_card = gamestate.draw_card(self.hand)
            print(new_card)
            for i in lyst:
                self.hand.append(i)
            #print(f"your new current hand: {self.hand}\n")
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
                    #gamestate.stock.remove(self.hand[self.play_card])
                    gamestate.current_top_card(self.card_suit, self.card_num)
                    gamestate.trick.append(self.hand[self.play_card])
                    self.hand.remove(self.hand[self.play_card])
                    #print(f"PLAYER HANDDDD: {self.hand}\n")
                    val = True
                else:
                    self.play_card = int(input("invalid entry, try another card: \n"))
               
class Computer(Player):
    """DOCSTRINGGGGG """ 
    def take_turn(self, gamestate):
        """DOCSTRINGGGGG """ 
        print(f"start turn hand COMPUTER: {self.hand}\n")
       
        #create match groups for future use
        #^DONE IN Player CLASS INIT
        #self.suits = []
        #self.nums = []
            
        #set up self.nums, self.suits, and self.playablecards
        self.suits = []
        self.nums = []
        self.nums_and_suits(self.hand)
        self.playable_cards(gamestate)
        #print(f"PLAYABLE CARDS LIST: {self.playablecards} \n")
        #print(f"NUMS LIST: {self.nums}")
        #print(f"SUITS LIST: {self.suits}")   
           
        if self.playablecards == []: # and gamestate.top_suit != "":
            print("Computer must draw until playable card appears\n")
            #self.hand = gamestate.draw_card(self.hand)
            lyst, new_card = gamestate.draw_card(self.hand)
            #print(new_card)
            #print(self.hand)
            for i in lyst:
                self.hand.append(i)
            self.play_card = new_card
            #print(f"PLAY CARD: {self.play_card}\n") #{self.play_card}
            #print(f"Computer's new current hand: {self.hand}\n")
            #new_card_lyst = [new_card]
            self.nums_and_suits(lyst)
            #print(f"SUITS: {self.suits}")
            gamestate.trick.append(self.play_card)
            self.card_suit = self.suits[self.hand.index(self.play_card)]
            self.card_num = self.nums[self.hand.index(self.play_card)]
            gamestate.current_top_card(self.card_suit, self.card_num)
            #print(f"Computer played: {self.play_card}\n")
            self.hand.remove(self.play_card)
        else:
            #play card
            self.play_card = self.playablecards.index(random.choice(self.playablecards))
            #print(f"COMPUTER PLAY CAR VALUE: {self.play_card}\n")
            #print(f"COMPUTER PLAY CARD VALUE: {self.play_card}")
            #self.card_index = self.playablecards.index[self.play_card]
            self.card_suit = self.suits[self.play_card]
            self.card_num = self.nums[self.play_card]
            val = False
            while val == False:
                if gamestate.isCardValid(self.card_suit) or gamestate.top_suit == "":
            #print(f"COMPUTER CARD_NUM VALUE: {self.card_num}")
            #print(f"COMPUTER CARD_SUIT VALUE: {self.card_suit}")
            #gamestate.stock.remove(self.play_card) #gamestate.stock.remove(self.hand[self.play_card])
                    gamestate.current_top_card(self.card_suit, self.card_num)
                    gamestate.trick.append(self.hand[self.play_card]) #gamestate.trick.append(self.hand[self.play_card])
                    self.hand.remove(self.hand[self.play_card]) #self.hand.remove(self.hand[self.play_card])
                    val = True
                else:
                    self.play_card = self.playablecards.index(random.choice(self.playablecards))
                    self.card_suit = self.suits[self.play_card]
                    self.card_num = self.nums[self.play_card]
                    
            #print(f"COMP HANDDDD: {self.hand}\n")
            #print(f"Computer played: {self.hand[self.play_card]}\n")
 
if __name__ == "__main__":
    """
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
    """       
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
        #print(f"{human.play_card} | {computer.play_card}")
        #run each player's turn
        if player == 0:
            #print(f"Top Suit: {gamestate.top_suit}\n")
            print(f"NEW ROUND: {player1name}'S TURN\n")
            human.take_turn(gamestate)
            print(f"New Top Card: {gamestate.top_card}\n")
            computer.take_turn(gamestate)
            #top_card = player1.top_card
            #player = 1 - player
        elif player == 1:
            #print(f"Top Suit: {gamestate.top_suit}\n")
            print(f"NEW ROUND: {player2name}'S TURN\n")
            computer.take_turn(gamestate)
            print(f"New Top Card: {gamestate.top_card}\n")
            human.take_turn(gamestate)
            #top_card = player2.top_card
            #player = 1 - player
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