from project.animals.animal import Mammal
from project.food import Food, Fruit, Vegetable, Meat

class Mouse(Mammal):
    @property
    def allowed_food(self)->list[type[Food]]:
        return [Vegetable, Fruit]
    
    @property
    def weight_gain(self)->float:
        return 0.10

    @staticmethod
    def make_sound():
        return f'Squeak'

class Dog(Mammal):
    @property
    def allowed_food(self)->list[type[Food]]:
        return [Meat]
    
    @property
    def weight_gain(self)->float:
        return 0.40
    
    @staticmethod
    def make_sound():
        return f'Woof!'

class Cat(Mammal):
    @property
    def allowed_food(self)->list[type[Food]]:
        return [Vegetable,Meat]
    
    @property
    def weight_gain(self)->float:
        return 0.30

    @staticmethod
    def make_sound():
        return f'Meow'

class Tiger(Mammal):
    @property
    def allowed_food(self)->list[type[Food]]:
        return [Meat]
    
    @property
    def weight_gain(self)->float:
        return 1.00

    @staticmethod
    def make_sound():
        return f'ROAR!!!'
