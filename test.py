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
