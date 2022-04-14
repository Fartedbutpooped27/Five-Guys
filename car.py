import math

class Car:
    """ A class for turinging and driving a car forward.
    
    Attributes:
        x (float, optional): a x coordinate
        y (float, optional): a y coordinate
        heading (float, optional): the direction the car will drive
    """
    def __init__(self, x = 0, y = 0, heading = 0):
        """
        Constructs all the necessary attributes for the car object
        
        Args:
            x (float, optional): a x coordinate
            y (float, optional): a y coordinate
            heading (float, optional): the direction the car will drive
        """
        self.x = x
        self.y = y
        self.heading = heading
   
    def turn(self, degrees):
        """
        Turn the car by the specified degrees.
        
         the car will turn clockwise if positive and counter clockwise if
         negative 
         
         Args:
            degrees (float): the change in heading, expressed in degrees. 
                
        side effects:
            changes the value of self.heading
        """
        float(degrees)
        self.heading = (self.heading + degrees) % 360
    
    def drive(self, distance):
        """
        Calculates the distance the car will moves forward using the distance 
            argument.
        
        Args:
            distance (float): the distance the car will move forward 
        """
        float(distance)
        self.x += distance * math.sin(math.radians(self.heading)) 
        self.y -= distance * math.cos(math.radians(self.heading))

def sanity_check():
    """Creates an instance of the Car class and steps for it to follow
    
    Side effects:
        Prints the new location and heading of the car
    
    Returns:
        The final location of the car
    """
    test_car = Car()
    test_car.turn(90)
    test_car.drive(10)
    test_car.turn(30)
    test_car.drive(20)
    print(f'Location: {test_car.x}, {test_car.y}')
    print(f'Heading: {test_car.heading}')
    return test_car

if __name__ == "__main__":
    sanity_check()