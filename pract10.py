"""
Exercise 1:
Most shapes from the graphics library (for example, Circle or Rectangle) have an outline colour as well as a fill colour.
Create a new instance variable outlineColour for the Square class and set it to black by default in the constructor. 
Now, add a mutator method for this instance variable in the Square class. 
The method needs to check that the outline colour is valid, similar to setFillColour. 
Finally, in testSquare change the outline colour of the square to a valid and then an invalid colour. 
Test your method by printing the change in the outline colour.
"""

from graphics import *

class MyPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f"MyPoint({self.x}, {self.y})"

class Square:
    def __init__(self, p1, side, fill_colour='black', outline_colour='black'):
        self.p1 = p1
        self.side = side
        self.p2 = MyPoint(p1.getX() + side, p1.getY() + side)
        self.fill_colour = fill_colour
        self.outline_colour = outline_colour

    def getP1(self):
        return self.p1

    def getP2(self):
        return self.p2

    def getSide(self):
        return self.side

    def move(self, dx, dy):
        self.p1.move(dx, dy)
        self.p2.move(dx, dy)

    def __str__(self):
        return f"Square({self.p1}, {self.p2})"

    def setFillColour(self, colour):
        colours = ["red", "green", "blue", "yellow", "purple"]
        if colour in colours:
            self.fill_colour = colour

    def setOutlineColour(self, colour):
        colours = ["black", "white", "red", "green", "blue"]  
        if colour in colours:
            self.outline_colour = colour
            print(f"Outline colour set to: {self.outline_colour}")
        else:
            print(f"Invalid outline colour: {colour}. Keeping the current outline colour.")
    """
 Exercise two:
 Write two new methods for your Square class called getPerimeter and getArea that return the perimeter and the area of the square instance. 
 Test these methods in the testSquare function.
    """           
    def getPerimeter(self):
        return 4 * self.side

    def getArea(self):
        return self.side ** 2

def testSquare():
    p1 = MyPoint(100, 50)
    square = Square(p1, 50)
    print("square's side length is", square.getSide())  # 50
    print("square's p1 is", square.getP1())  # MyPoint(100, 50)
    print("square's p2 is", square.getP2())  # MyPoint(150, 100)

    square.move(10, -20)
    print("After the move ...")
    print("square's side length is", square.getSide())  # 50
    print("square's p1 is", square.getP1())  # MyPoint(110, 30)
    print("square's p2 is", square.getP2())  # MyPoint(160, 80)

    print(square)  # Square(MyPoint(110, 30), MyPoint(160, 80))

    print("Changing square's fill colour to red")
    square.setFillColour("red")
    print("square's fill colour is", square.fill_colour)  # red

    print("Changing square's outline colour to blue")
    square.setOutlineColour("blue")
    print("square's outline colour is", square.outline_colour)  # blue

    print("Changing square's outline colour to leopard print!")
    square.setOutlineColour("leopard print")
    print("square's outline colour is", square.outline_colour)  # blue (keeping the current outline colour)

testSquare()

"""
Exercise three:
The Rectangle class from the graphics module has a getCenter method which returns a Point object. 
Try it by running the following lines in the shell:

from graphics import *
rect = Rectangle(Point(50, 50), Point(100, 100))
print(rect.getCenter())

Your task is to write and test a similar method for the Square class. 
Note that your method needs to return a MyPoint object instead of a Point.
"""

from graphics import *

class MyPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return f"MyPoint({self.x}, {self.y})"

class Square:
    def __init__(self, p1, side, fill_colour='black', outline_colour='black'):
        self.p1 = p1
        self.side = side
        self.p2 = MyPoint(p1.getX() + side, p1.getY() + side)
        self.fill_colour = fill_colour
        self.outline_colour = outline_colour

    def getP1(self):
        return self.p1

    def getP2(self):
        return self.p2

    def getSide(self):
        return self.side

    def move(self, dx, dy):
        self.p1.move(dx, dy)
        self.p2.move(dx, dy)

    def __str__(self):
        return f"Square({self.p1}, {self.p2})"

    def setFillColour(self, colour):
        colours = ["red", "green", "blue", "yellow", "purple"]
        if colour in colours:
            self.fill_colour = colour

    def setOutlineColour(self, colour):
        colours = ["black", "white", "red", "green", "blue"]  
        if colour in colours:
            self.outline_colour = colour
            print(f"Outline colour set to: {self.outline_colour}")
        else:
            print(f"Invalid outline colour: {colour}. Keeping the current outline colour.")

    def getCenter(self):
        center_x = (self.p1.getX() + self.p2.getX()) / 2
        center_y = (self.p1.getY() + self.p2.getY()) / 2
        return MyPoint(center_x, center_y)

square = Square(MyPoint(110, 30), 50)
print(f"The centre of the square is {square.getCenter()}")  # Output: MyPoint(135.0, 55.0)

"""
Exercise four:
Define a MyCircle class that can be used similarly to the Circle class from the graphics library. 
Test your circle using a testCircle function.  
The class diagram below shows what you need to write:

centre: MyPoint
radius: float

__init__(centre: MyPoint, radius: float)
getCentre(): MyPoint
getRadius(): float
move(dx: float, dy: float)
__str__(): str


"""
from graphics import *

class MyPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f"MyPoint({self.x}, {self.y})"

class MyCircle:
    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius

    def getCentre(self):
        return self.centre

    def getRadius(self):
        return self.radius

    def move(self, dx, dy):
        self.centre.move(dx, dy)

    def __str__(self):
        return f"MyCircle(centre: {self.centre}, radius: {self.radius})"

def testCircle():
    center_point = MyPoint(50, 50)
    circle = MyCircle(center_point, 30)

    print("Circle center:", circle.getCentre())  # Output: MyPoint(50, 50)
    print("Circle radius:", circle.getRadius())  # Output: 30

    circle.move(10, -20)
    print("After the move ...")
    print("Circle center:", circle.getCentre())  # Output: MyPoint(60, 30)

    print(circle)  # Output: MyCircle(centre: MyPoint(60, 30), radius: 30)

testCircle()

"""
Exercise five:
Your task is to write and test a class representing a bank account. 
Begin by looking at our test case below. Your bank account class must be able to perform the tasks shown below. 
However, you may wish to add extra attributes (instance variables) or behaviours (methods) in your class. 

testAccount()
The name of the account holder is Matthew Poole
The initial balance of the account is £0.00
After depositing £100, the balance is £100.00
After withdrawing £50, the balance is £50.00
After trying to withdraw £100, the balance is £50.00
Account name: Matthew Poole
Balance: £50

As an extra feature, add a percentage interest rate to the parameters of the constructor. 
This percentage can then be later used in a method that applies interest to the current balance.
"""

class BankAccount:
    def __init__(self, account_holder, initial_balance=0.00, interest_rate=5):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount
        print(f"After depositing £{amount:.2f}, the balance is £{self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal failed.")
        else:
            self.balance -= amount
            print(f"After withdrawing £{amount:.2f}, the balance is £{self.balance:.2f}")

    def apply_interest(self):
        interest_amount = (self.balance * self.interest_rate) / 100
        self.balance += interest_amount
        print(f"Interest applied. New balance is £{self.balance:.2f}")

    def display_account_info(self):
        print(f"Account name: {self.account_holder}")
        print(f"Balance: £{self.balance:.2f}")


def testAccount():
    account = BankAccount("Severus Snape")

    print(f"The name of the account holder is {account.account_holder}")
    print(f"The initial balance of the account is £{account.balance:.2f}")

    account.deposit(100)
    account.withdraw(50)
    account.withdraw(100) # This should fail due to insufficient funds
    account.apply_interest()

    print("Account information after transactions:")
    account.display_account_info()


# Run the test
testAccount()

"""
Exercise six:
Write a scale method for the Square class which takes an integer as its parameter and scales the square by that factor. 
Note that the centre of the square must remain fixed. 
You'll need to update the coordinates of p1 and p2 based on the scale factor and the current side length of the square.
"""

from graphics import *

class Square:
    def __init__(self, sideLength, center, fillColour="white", outlineColour="black"):
        self.sideLength = sideLength
        self.center = center
        self.fillColour = fillColour
        self.outlineColour = outlineColour

    def draw(self, win):
        square = Rectangle(Point(self.center.getX() - self.sideLength / 2, self.center.getY() - self.sideLength / 2),
                           Point(self.center.getX() + self.sideLength / 2, self.center.getY() + self.sideLength / 2))
        square.setFill(self.fillColour)
        square.setOutline(self.outlineColour)
        square.draw(win)

    def setOutlineColour(self, newColour):
        validColours = ["black", "white", "red", "green", "blue", "yellow"]  
        if newColour.lower() in validColours:
            self.outlineColour = newColour.lower()
            print(f"Changing square's outline colour to {newColour}")
        else:
            print(f"Invalid colour: {newColour}! Outline colour unchanged.")

    def scale(self, factor):
        if factor > 0:
            # Calculate the new side length based on the scale factor
            new_side_length = self.sideLength * factor

            # Update the side length and redraw the square
            self.sideLength = new_side_length

def testSquare():
        win = GraphWin("Test Square", 600, 600)
        square = Square(200, Point(300, 300), fillColour="red")

        square.scale(2)  # Scale up by a factor of 2
        square.draw(win)

        square.scale(0.5)  # Scale down by a factor of 0.5
        square.draw(win)

        win.getMouse()
        win.close()

if __name__ == "__main__":
    testSquare()

"""
Exercise seven:
Add a class representing an aeroplane to the pract10.py file. Use the class diagram below as your starting point:

fuel: int
altitude: int
departure: str
destination: str

__init__(departure: str, destination: str)
setfFuel(fuel: int)
increaseAltitude()
decreaseAltitude()
setDeparture(departure: str)
setDestination(destination: str)
getDeparture(): str
getDestination(): str
getAltitude(): int
__str__: str

Assume that all flights use a maximum amount of 150000 litres of fuel (so make sure enough fuel is added in the setFuel method). 
Additionally, assume that all flights are direct, so the departure of the flight becomes its destination once it is landed.
Lastly, test your Aeroplane class in a function that asks the user to select a departure and destination. 
Then, create an Aeroplane object, fuel it up, and set its departure and destination. 
After each change, remember to print your Aeroplane object too (this should display all the attributes of your object).

"""

class Aeroplane:
    MAX_FUEL = 150000

    def __init__(self, departure, destination):
        self.fuel = 0
        self.altitude = 0
        self.departure = departure
        self.destination = destination

    def setFuel(self, fuel):
        if fuel > Aeroplane.MAX_FUEL:
            self.fuel = Aeroplane.MAX_FUEL
        else:
            self.fuel = fuel

    def increaseAltitude(self):
        self.altitude += 1000

    def decreaseAltitude(self):
        if self.altitude >= 1000:
            self.altitude -= 1000

    def setDeparture(self, departure):
        self.departure = departure

    def setDestination(self, destination):
        self.destination = destination

    def getDeparture(self):
        return self.departure

    def getDestination(self):
        return self.destination

    def getAltitude(self):
        return self.altitude

    def __str__(self):
        return f"Aeroplane - Departure: {self.departure}, Destination: {self.destination}, Altitude: {self.altitude}, Fuel: {self.fuel}"

def testAeroplane():
    departure = input("Enter departure city: ")
    destination = input("Enter destination city: ")

    airplane = Aeroplane(departure, destination)

    fuel_amount = int(input("Enter fuel amount (in litres): "))
    airplane.setFuel(fuel_amount)
    print(airplane)

    airplane.increaseAltitude()
    print(airplane)

    airplane.decreaseAltitude()
    print(airplane)

    new_departure = input("Enter new departure city: ")
    airplane.setDeparture(new_departure)
    print(airplane)

    new_destination = input("Enter new destination city: ")
    airplane.setDestination(new_destination)
    print(airplane)

if __name__ == "__main__":
    testAeroplane()
