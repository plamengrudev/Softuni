from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def drive(self,distance:int):
        pass

    @abstractmethod
    def refuel(self,fuel: int):
        pass

class Car(Vehicle):
    VEHICLE_SPECIFIC=0.9
    FUEL_MULTIPLIER=1
    def __init__(self,fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity=fuel_quantity
        self.fuel_consumption=fuel_consumption

    def drive(self,distance: int):
        if distance*(self.VEHICLE_SPECIFIC+self.fuel_consumption)<=self.fuel_quantity:
            self.fuel_quantity-=distance*(self.VEHICLE_SPECIFIC+self.fuel_consumption)

    def refuel(self,fuel: int):
        self.fuel_quantity+=fuel*self.FUEL_MULTIPLIER

class Truck(Vehicle):
    VEHICLE_SPECIFIC=1.6
    FUEL_MULTIPLIER=0.95
    def __init__(self,fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity=fuel_quantity
        self.fuel_consumption=fuel_consumption

    def drive(self,distance: int):
        if distance*(self.VEHICLE_SPECIFIC+self.fuel_consumption)<=self.fuel_quantity:
            self.fuel_quantity-=distance*(self.VEHICLE_SPECIFIC+self.fuel_consumption)

    def refuel(self,fuel: int):
        self.fuel_quantity+=fuel*self.FUEL_MULTIPLIER


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)