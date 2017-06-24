# Parking Lot: learning and using Python basics 

class Vechile:

    numberOfVechiles = 0

    def __init__(self, model, color, year, isVIP):
        self.model = model
        self.color = color
        self.year = year
        self.isVIP = isVIP
        Vechile.numberOfVechiles += 1
    
    def entreanceTime(self, time):
        pass
    
    def exitTime(self, time):
        pass

    def determinePrice(self, timeIn, timeOut):
        pass

class Car(Vechile):
    pass
    numberOfCars = 0

class Motorcyle(Vechile):
    numberOfMotos = 0
    pass

class Bus(Vechile):
    numberOfBus = 0
    pass