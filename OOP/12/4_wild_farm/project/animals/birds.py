from project.animals.animal import Bird
from project.food import Food,Vegetable,Fruit,Meat,Seed

class Owl(Bird):
    @property
    def allowed_food(self)->list[type[Food]]:
        return [Meat]
    
    @property
    def weight_gain(self)->float:
        return 0.25

    @staticmethod
    def make_sound():
        return f'Hoot Hoot'

class Hen(Bird):
    @property
    def allowed_food(self)->list[type[Food]]:
        return [Vegetable,Meat,Fruit,Seed]
    
    @property
    def weight_gain(self)->float:
        return 0.35

    @staticmethod
    def make_sound():
        return f'Cluck'