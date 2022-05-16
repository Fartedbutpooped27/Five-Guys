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

deck = []
discard = []
hand = []
letterName = list(CARDS.keys())

#fill draw_pile
for f in FACES:
    for i in letterName:
        deck.append(f"{i} {f}")


#regex that match group suits and card values
#this should go in the deal_hand() method
expr = r"(?P<cardValue>^\S*)\s(?P<suitValue>\S*)"
for element in deck:
    match = re.search(expr, element)
    cardValue = match.group(0)
    suitValue = match.group(1)
    
class GameState:
    def __init__(self, deck):
        self.top_suit = ""
        self.high_card = ""
        
        self.stock = []
        #for i in deck:
        #  self.stock.append(i)
        
        self.stock = [i for i in deck] #LIST COMPREHENSION

    def draw_card(self, hand):      
        test_deck = []
        suit = []
        
        for i in self.stock:
          test_deck.append(i)

       

        new_card = random.choice(test_deck)
        valid = False
        while valid == False:
          #print(f"new card 1 {new_card}")
          if self.top_suit not in new_card:
            new_card = random.choice(test_deck)
            #print(f"new card 2 {new_card}")
            hand.append(new_card)
            test_deck.remove(new_card)
          else:
            hand.remove(new_card)
            valid = True
        print(f"you played {new_card}\n")
        return hand
    
    def Current_top_card(self, chosenCard):
        self.top_suit = chosenCard
        
        
        
        
        
    def roundWinner(self, player1, player2):
        cards = [player1, player2]
        winner = max (cards, key= lambda x: CARDS[x])
        if winner == player1:
            return 0
        else:
            return 1
        
        
       
    def game_winner():
        pass  
  
        
    def isCardValid(self, card):
      if card == self.topSuit:  
        return True
      else:
        return False
    
    
class Player:
    def __init__(self, deck, player_name="no_name"):
        #init player name
        self.player_name = player_name
        self.stock = []
        self.hand = []
        self.top_card = ""
        self.chosenCard = ""
        
        for i in deck:
            self.stock.append(i)
        
        self.starting_hand = []
        count = 4
        while count > 0:
            new_card = random.choice(self.stock)
            self.hand.append(new_card)
            self.stock.remove(new_card)
            count -= 1
        
        
    
class Human(Player):
    def take_turn(self):
        #get gamestate
        #check player's hand for playable cards
        #if none, draw till playable card
        #else, let player play a card
        #call isCardValid and return error till player plays valid card
        #remove played card from hand
        #pass new attributes into a current_gamestate variable (current top card, current stock, current trick, current high card, current winner)
        #print player's hand
        print(f"Top Suit: {self.topSuit}\n")
        print(f"start turn hand: {self.hand}\n")
        
        #create match groups for future use
        self.suits = []
        self.nums = []
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
    def take_turn(self):
        print(f"Top Suit: {self.topSuit}\n")
        print(f"start turn hand: {self.hand}\n")
        
        #create match groups for future use
        self.suits = []
        self.nums = []
        expr = r"(?P<cardValue>^\S*)\s(?P<suitValue>\S*)"
        for element in self.hand:
            match = re.search(expr, element)
            cardValue = match.group("cardValue")
            suitValue = match.group("suitValue")
            self.suits.append(suitValue)
            self.nums.append(cardValue)
            
def main():
    stock = []
    for i in deck:
        stock.append(i)
    
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
        
main()   
    