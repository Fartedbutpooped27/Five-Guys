from argparse import ArgumentParser
import sys

def evaluate(line):
    """ Computes a math expression in postfix notation
    
    Args: 
        line (string): a math expression in postfix notation
    
    Returns:
        float: answer to the math expression
    """
    stack = []
    line = line.split()
    for char in line:
        if char == "+":
            y = stack.pop()
            x = stack.pop()
            result = x + y
            stack.append(result)
        elif char == "-":
            y = stack.pop()
            x = stack.pop()
            result = x - y
            stack.append(result)
        elif char == "*":
            y = stack.pop()
            x = stack.pop()
            result = x * y
            stack.append(result)
        elif char == "/":
            y = stack.pop()
            x = stack.pop()
            result = x / y
            stack.append(result)
        else:
            number = float(char)
            stack.append(number)
    return stack[0]
        
def main(filepath):   
    """ Opens and reads a file, then computes the math expressions in postfix 
    notation line by line
    
    Args:
        filepath (.txt): imports a text file which includes expressions in 
            postfix notation
    
    Side effects: 
        print: the math expressions in postfix notation and the answer to the 
            expressions
    """
    with open(filepath, "r", encoding = "utf-8") as f:
        for statement in f:
            string = statement.strip()
            answer = evaluate(string)
            print(f'{string} = {answer}')
            
def parse_args(arglist):
    """ Process command line arguments.
    
    Expect one mandatory argument (a file containing postfix expressions).
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file containing reverse polish notation")
    args = parser.parse_args(arglist)
    return args


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)
