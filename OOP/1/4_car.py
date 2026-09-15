class Car:
    def __init__(self, name: str,model: str,engine: str):
        self.name=name
        self.model=model
        self.engine=engine

    def get_info(self):
        return f"This is {self.name} {self.model} with engine {self.engine}"

car = Car("W124", "Mercedes", "Petrol l4")
print(car.get_info())



