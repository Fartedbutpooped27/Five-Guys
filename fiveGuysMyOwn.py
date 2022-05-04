import random
import re



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

FACES = [
    "Spades",
    "Clubs",
    "Diamonds",
    "Hearts"
]

draw_pile = []
discard = []
human_hand = []
computer_hand = []

#fill draw_pile
for f in FACES:
    for c in CARDS:
        letterName = CARDS.keys()
        #print(letterName)
        #draw_pile.append(f"{letterName} of {f}")

#print(draw_pile)
        

   
        


#init human hand
#count = 4
#card_list = list(self.draw_pile.items())
#while count > 0:
            #keys = list(self.draw_pile.keys())
            #values = list(self.draw_pile.values())
            #card_num = random.choice(keys)
            #suit = random.choice(values)
            #self.human_hand[card_num] = suit
            #delete from draw_pile
            #random_card = random.choice(card_list)
            #self.human_hand[random_card[0]] = random_card[1]
            #card_list.remove(random_card)
            #count -= 1
            #possible pop method
    #keys = list(draw_pile.keys())
    #key = random.choice(keys)
    #new_value = draw_pile.pop(key)
    #human_hand[key] = new_value
    #count -= 1
            
#print(human_hand)
         