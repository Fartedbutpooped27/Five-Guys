"""Perform fixed-rate mortgage calculations."""

from argparse import ArgumentParser
import math
import sys

def get_min_payment(P, annual_rate, term = 30, number_payments = 12):
    """ Computes the minimum mortgage payment 
    
    Args:
        P (float): total amount of the mortgage 
            (assume this is a positive number)
        annual_rate (float): annual interest rate (between 0 and 1)
        term (int, optional): The term of the mortgage in years 
            (assume this is a positive integer)
        number_payments (int, optional): The number of payments per year
            (assume this is a positive integer)
            
    Returns:
        int: minimum mortgage payment
    """
    r = annual_rate / number_payments
    n = term * number_payments
    A = (P * r * (1 + r)**n) / ((1+r)**n - 1)
    return math.ceil(A)

def interest_due(b, annual_rate, number_payments = 12):
    """ Computes the amount of interest due in the next payment 

    Args:
        b (float): balance of the mortgage (assume this is a positive number)
        annual_rate (float): annual interest rate (between 0 and 1)
        number_payments (int, optional): number of payments per year 
            (assume this is a positive integer)
    
    Returns:
        float: the amount of interest due in the next payment
    """
    r = annual_rate / number_payments
    i = b * r
    return i
    
def remaining_payments(b, annual_rate, target, number_payments = 12):
    """ Computes the the number of payments required to pay off the mortgage
    
    Args:
        b (float): balance of the mortgage (assume this is a positive number)
        annual_rate (float): annual interest rate (between 0 and 1)
        target (float): target payment (assume this is a positive number)
        number_payments (int, optional): number of payments per year 
            (assume this is a positive integer)
    
    Returns:
        int: the number of payments required to pay off the mortgage
    """
    payments_made = 0
    while b > 0:
        total = target - interest_due(b, annual_rate, number_payments)
        b = b - total
        payments_made +=1
    else:
        return payments_made
        
def main(P, annual_rate, term = 30, number_payments = 12, target = None):
    """ Displays the user's minimum mortgage payment and computes whether the 
    user's target payment satisfies the minimum mortgage payment.
    
    Args:
        P (float): Total amount of the mortgage 
            (assume this is a positive number)
        annual_rate (float): annual interest rate (between 0 and 1)
        term (int, optional): term of the mortgage in years 
            (assume this is a positive integer)
        number_payments (int, optional): number of payments per year 
            (assume this is a positive integer)
        target (float, optional): The user's target payment 
            (assume this is a positive number)
        
    Returns:
        float: minimum mortgage payment 
    
    Side effects:
        string: a statement depending on 
            the user's target payment in comparison to the 
            minimum mortgage payment.
    """
    minimum_payment = get_min_payment(P, annual_rate, term, number_payments)
    print(f'Your minimum payment is {minimum_payment}')
    if target == None:
        target = minimum_payment
    elif target < minimum_payment:
        print("Your target payment is less than the minimum payment for this \
            mortgage")
    else:
        total_payments = remaining_payments(P, annual_rate, target, number_payments)
        print(f"If you make payments of ${target}, you will pay off the \
            mortgage in {total_payments} payments.")

def parse_args(arglist):
    """Parse and validate command-line arguments.
    
    This function expects the following required arguments, in this order:
    
        mortgage_amount (float): total amount of a mortgage
        annual_interest_rate (float): the annual interest rate as a value
            between 0 and 1 (e.g., 0.035 == 3.5%)
        
    This function also allows the following optional arguments:
    
        -y / --years (int): the term of the mortgage in years (default is 30)
        -n / --num_annual_payments (int): the number of annual payments
            (default is 12)
        -p / --target_payment (float): the amount the user wants to pay per
            payment (default is the minimum payment)
    
    Args:
        arglist (list of str): list of command-line arguments.
    
    Returns:
        namespace: the parsed arguments (see argparse documentation for
        more information)
    
    Raises:
        ValueError: encountered an invalid argument.
    """
    # set up argument parser
    parser = ArgumentParser()
    parser.add_argument("mortgage_amount", type=float,
                        help="the total amount of the mortgage")
    parser.add_argument("annual_interest_rate", type=float,
                        help="the annual interest rate, as a float"
                             " between 0 and 1")
    parser.add_argument("-y", "--years", type=int, default=30,
                        help="the term of the mortgage in years (default: 30)")
    parser.add_argument("-n", "--num_annual_payments", type=int, default=12,
                        help="the number of payments per year (default: 12)")
    parser.add_argument("-p", "--target_payment", type=float,
                        help="the amount you want to pay per payment"
                        " (default: the minimum payment)")
    # parse and validate arguments
    args = parser.parse_args()
    if args.mortgage_amount < 0:
        raise ValueError("mortgage amount must be positive")
    if not 0 <= args.annual_interest_rate <= 1:
        raise ValueError("annual interest rate must be between 0 and 1")
    if args.years < 1:
        raise ValueError("years must be positive")
    if args.num_annual_payments < 0:
        raise ValueError("number of payments per year must be positive")
    if args.target_payment and args.target_payment < 0:
        raise ValueError("target payment must be positive")
    
    return args


if __name__ == "__main__":
    try:
        args = parse_args(sys.argv[1:])
    except ValueError as e:
        sys.exit(str(e))
    main(args.mortgage_amount, args.annual_interest_rate, args.years,
         args.num_annual_payments, args.target_payment)
