"""Compute a team's score for a (fictitious) word game.

In this game, two players independently find words in a matrix of letters.
Each player's words are added to a text file with one word per line. Duplicates
are removed from each player's list. For each word that appears on both players'
lists, the team's score increases by the number of letters in the word minus 2
(words less than three characters long are not worth any points).
"""


from argparse import ArgumentParser
import sys


class PlayerWords:
    """A class for finding unique words found by one player
    
    Attributes:
        file(set of str): a string consisting of a path to a text file containing
            unique words found by one player
            
    Methods:
        score(playerWords): determines which words both players were able to
            find and calculates a final score
    """
    def __init__(self, file):
        """Constructs all the necessary attributes for the playerwords object
        or Initiates a PlayerWords methods

        Args:
            file(str): a string that contains the path to a text file with unique 
                words found by one player
        
        Side effects: 
            sets word attribute
        """
        with open(file, 'r', encoding = 'utf-8') as f:
            self.words = set()
            for word in f:
                word = word.strip()
                self.words.add(word)
                
    def score(self, otherPlayer):
        """Determines which words both players found and the calculates a final
        score

        Args:
            otherPlayer (PlayerWords): the partner of self
        Returns:
            int: the final calculated score
        """
        incommon = self.words & otherPlayer.words
        points = 0
        for word in incommon:
            if len(word) >= 3:
                points += len(word) - 2
        return points

def main(file1, file2):
    """Takes two text files containing words found by each player and prints out
    the finals score

    Args:
        file1 (str): a string consisting of a path to a text file containing the
            words found by player 1
        file2 (str): a string consisting of a path to a text file containing the
            words found by player 2
    
    Side effects:
        Prints the final score earned by the team
    """
    player1 = PlayerWords(file1)
    player2 = PlayerWords(file2)          
    print(f'Your team scored {player1.score(player2)} points!')
                
                
def parse_args(arglist):
    """Parse command line arguments.
    
    Expect two mandatory arguments:
        - str: path to a text file containing words found by player 1.
        - str: path to a text file containing words found by player 2.
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.

    """
    parser = ArgumentParser()
    parser.add_argument("wordfile1", help="file containing player 1's words")
    parser.add_argument("wordfile2", help="file containing player 2's words")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.wordfile1, args.wordfile2)
