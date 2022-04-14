from argparse import ArgumentParser
import re
import sys


class Address:
    def __init__(self, address, house_number, street, city, state, zip):
        expr = r"""(?xm)
^
(?P<house_number>\S+)
\s
(?P<street_name>[^,]+)
,\s
(?P<city>.+)
\s
(?P<state>[A-Z]+)
\s
(?P<zip_code>\d{5})
"""
        self.house_number = house_number
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        match = re.search(expr, address)
        if re.search(expr, address) == None:
            raise ValueError
        else:
            self.house_number = match.group(0)
            self.street = match.group(1)
            self.city = match.group(2)
            self.state = match.group(3)
            self.zip = match.group(4)

    def __repr__(self):
        """Return a formal representation of the Address object."""
        return (
            f"address:      {self.address}\n"
            f"house number: {self.house_number}\n"
            f"street:       {self.street}\n"
            f"city:         {self.city}\n"
            f"state:        {self.state}\n"
            f"zip:          {self.zip}"
        )

def read_addresses(path):
    with open(path , 'r', encoding = 'utf-8') as f:
        list = [ for addr in f]
        return list

def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect one mandatory argument, the path to a file of addresses.
    
    Args:
        arglist (list of str): command-line arguments.
    
    Returns:
        namespace: an object with one attribute, file, containing a string.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file containing one address per line")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    for address in read_addresses(args.file):
        # the !r tells the f-string to use the __repr__() method to generate
        # a string version of the address object
        print(f"{address!r}\n")
