"""An implementation of the game mancala."""

from argparse import ArgumentParser
from blessed import Terminal
import sys
from time import sleep

#####
# Board setup
#####

TERM = Terminal()

NEUT = TERM.gray33      # 33% gray
P0DK = TERM.cyan4       # dark color for player 0
P0LT = TERM.cyan3       # light color for player 0
P1DK = TERM.violetred4  # dark color for player 1
P1LT = TERM.violetred1  # light color for player 1

# this template gets populated in Mancala.print_board
SLOT = "{:>2}"
TEMPLATE = f"""{TERM.home+TERM.clear}\
<SP>  {P0DK}\u2193  f  e  d  c  b  a  \u2190  <NAME0>
<SP> {P0LT}{SLOT} {SLOT} {SLOT} {SLOT} {SLOT} {SLOT} {SLOT}
<SP> {NEUT}------------------------
<SP> {P1LT}   {SLOT} {SLOT} {SLOT} {SLOT} {SLOT} {SLOT} {SLOT}
{P1DK}<NAME1>  \u2192  g  h  i  j  k  l  \u2191{TERM.normal}"""

PAUSE = 0.3             # used to help animate moves

PITS = "abcdef.ghijkl"  # helps convert between pit indexes and letters in UI
STORES = [6, 13]        # indexes of the stores

#####
# Helper function
#####

def get_move(game, player):
    """Get player's selection of a pit to play from.
    
    The player will select a letter corresponding to one of their pits. This
    function will translate their selection into an index of game.board. The
    function will ask repeatedly until the user provides valid input.
    
    Args:
        game (Mancala): the current game.
        player (int): index of the player (0 or 1).
    
    Returns:
        int: the pit selected by the user, expressed as an index of game.board.
    
    Side effects:
        Displays information in the terminal.
        May cause the program to exit.
    """
    while True:
        print()
        selection = (input(f"{game.names[player]}, select one of your pits that"
                          " is not empty (or enter q to quit): ")
                     .lower()
                     .strip())
        if selection == "q":
            sys.exit(0)
        try:
            if len(selection) != 1 or not selection.isalpha():
                raise ValueError("Please enter a single letter.")
            pit = PITS.find(selection)
            if pit == -1:
                raise ValueError("Please enter a letter corresponding to one of"
                                 " your non-empty pits.")
            game.validate_move(pit, player)
        except ValueError as e:
            print(e)
        else:
            return pit

#####
# Mancala class
#####

class Mancala:
    """A class to play the game Mancala
    
    Attributes:
            player0 (str): name of player 0
            player1 (str): name of player 1
            func0 (int, optional): the turn function to call on player 0’s turn.
                Defaults to get_move.
            func1 (int, optional): the turn function to call on player 1’s turn.
                Defaults to get_move.
    """
    def __init__(self, player0, player1, func0 = get_move, func1 = get_move):
        """Initiates a Mancala methods

        Args:
            player0 (str): name of player 0
            player1 (str): name of player 1
            func0 (int, optional): the turn function to call on player 0’s turn.
                Defaults to get_move.
            func1 (int, optional): the turn function to call on player 1’s turn.
                Defaults to get_move.
        
        Side effects: 
            Initalizes names, turn_funces, and board attributes
        """
        self.names = [player0, player1]
        self.turn_funcs = [func0, func1]
        self.board = []
    
    def validate_move(self, pit, player):
        """Checks whether a player is allowed to play from a particular pit. 
        
        Args:
            pit (int): the index of a pit
            player (int): the index of the player

        Raises:
            ValueError: the pit is a store
            ValueError: the pit index doesn't belong to the player
            ValueError: the pit is empty
        
        Side effects:
            Prints the reason why the move is invalid
        """
        int(pit)
        if pit == STORES:
            print("Sorry, you can't select the store.")
            raise ValueError
        elif self.is_own_pit(pit,player) == False:
            print("Sorry, you don't control that pit.")
            raise ValueError
        elif self.board[pit] == 0:
            print("Sorry, that pit is empty.")
            raise ValueError
        
    def check_capture(self, pit, player):
        """Determines if a player has qualified to capture seeds and carries out
        the capture if the conditions have been met

        Args:
            pit (int): the index of the pit in which a player has placed the 
                last seed from a seed distribution action
            player (int): index of the player
        
        Side effects:
            Prints the player has captured the contents of the pit
            Displays information in the terminal.
        """
        if self.is_own_pit(pit,player) == True and pit not in STORES and \
        self.board[pit] == 1:
            opposite = 12 - pit 
            self.board[STORES[player]] += self.board[pit] + self.board[opposite]
            self.board[pit] = 0
            self.board[opposite] = 0
            self.print_board()
            print(f'{self.names[player]} captured the contents of pits \
                  {PITS[pit]} and {PITS[opposite]}.')
            
    def distribute_seeds(self, index, player):
        """Distributes seeds that were in a specified pit to the subsequent pits
        and the player’s store

        Args:
            index (int): the index of a non-empty pit belonging to the player
            player (int): the index of the player

        Returns:
            int: the index of the last pit or the store into which a seed 
                was placed
                
        Side effects:
            Displays information in the terminal.
        """
        if player == 0:
            opponent_stores = STORES[1]
        else:
            opponent_stores = STORES[0]
        seeds = self.board[index]
        self.board[index] = 0
        self.print_board()
        while seeds > 0:
            index = (index + 1) % 14
            if index == opponent_stores:
                pass
            else:
                self.board[index] += 1
                seeds -= 1
                self.print_board()
        return index
            
    
    def play_round(self):
        """Manages one round of game play
        
        Side effects:
            Prints the player gets an extra turn
            Displays information in the terminal.
        """
        self.board = ([4] * 6 + [0]) * 2
        self.print_board()
        player = 0
        while self.game_over() == False:
            i_pit = self.turn_funcs[player](self,player)
            last_placed = self.distribute_seeds(i_pit, player)
            self.check_capture(last_placed, player)
            if last_placed in STORES:
                print(f"{self.names[player]} gets an extra turn!")
            else:
                player = 1 - player
        self.print_winner()
            
    def game_over(self):
        """Determine whether a round is over.
        
        A round is considered over when one player's pits are all empty.
        
        Returns:
            bool: True if the game is over, otherwise False.
        """
        return sum(self.board[0:6]) == 0 or sum(self.board[7:13]) == 0
    
    def score(self, player):
        """Calculate a player's score.
        
        Args:
            player (int): player's index (0 or 1).
        
        Returns:
            int: the requested player's score.
        """
        start = 0 if player == 0 else 7
        end = start + 7
        return sum(self.board[start:end])
    
    def is_own_pit(self, pit, player):
        """Determine if pit belongs to player.
        
        Args:
            pit (int): index into self.board.
            player (int): player's index (0 or 1).
        
        Returns:
            bool: True if pit belongs to player.
        """
        first_pit = 0 if player == 0 else 7
        store = first_pit + 6
        return first_pit <= pit <= store
    
    def play(self):
        """Manage game play.
        
        After each round, ask players if they would like to play again.
        
        Side effects:
            Displays information in the terminal.
            Calls methods that modify self.board.
        """
        with TERM.fullscreen():
            while True:
                try:
                    self.play_round()
                    if not self.play_again():
                        sys.exit(0)
                except SystemExit:
                    print("Thanks for playing!")
                    sleep(PAUSE*3)
                    raise
        
    def play_again(self):
        """Ask players if they would like to play another round.

        Returns:
            bool: True if players choose to keep playing, otherwise False.
        
        Side effects:
            Displays information in the terminal.
        """
        print()
        while True:
            response = (input("Would you like to play again (y/n)? ")
                        .strip()
                        .lower()[0])
            if response not in "ny":
                print("Please type 'y' or 'n'.")
                continue
            return response == "y"
    
    def print_board(self, pause=PAUSE):
        """Displays the board in the terminal and pauses momentarily.

        Args:
            pause (float, optional): duration to pause before allowing the
                program to continue. Expressed in seconds. Defaults to PAUSE.
        
        Side effects:
            Displays information in the terminal.
            Delays program execution for a brief amount of time.
        """
        template = (TEMPLATE
                    .replace("<NAME0>", self.names[0])
                    .replace("<NAME1>", self.names[1])
                    .replace("<SP>", " "*len(self.names[1])))
        print(template.format(*(self.board[6::-1]+self.board[7:])))
        sleep(pause)

    def print_winner(self):
        """Display information about the winner of a round.
        
        Side effects:
            Displays information in the terminal.
        """
        self.print_board()
        print()
        score0 = self.score(0)
        score1 = self.score(1)
        if score0 == score1:
            print("Tie game!")
        else:
            winner = 0 if score0 > score1 else 1
            winner_score = max(score0, score1)
            loser_score = min(score0, score1)
            print(f"{self.names[winner]} wins {winner_score} to {loser_score}.")


#####
# Code to run the program
#####

def parse_args(arglist):
    """Parse command-line arguments.
    
    Expect two required arguments (the names of two players).
    
    Returns:
        namespace: a namespace with two attributes: name0 and name1, both
        strings.
    """
    parser = ArgumentParser()
    parser.add_argument("name0", help="the first player's name")
    parser.add_argument("name1", help="the second player's name")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    game = Mancala(args.name0, args.name1)
    game.play()
