from project.dough import Dough
from project.topping import Topping

class Pizza:

    def __init__(self,name: str, dough: Dough,max_number_of_toppings: int):
        self.name=name
        self.dough=dough
        self.max_number_of_toppings=max_number_of_toppings
        self.toppings: [Topping.topping_type,Topping.weight] = {}
    
    @property
    def name(self):
        return self.__name
    
    @property
    def dough(self):
        return self.__dough
    
    @property
    def max_number_of_toppings(self):
        return self.__max_number_of_toppings

    
    @name.setter
    def name(self,value):
        if value=='':
            raise ValueError('The name cannot be an empty string')
        else:
            self.__name=value
    
    @dough.setter
    def dough(self,value):
        if value==None:
            raise ValueError('You should add dough to the pizza')
        else:
            self.__dough=value
    
    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value):
        if value<=0:
            raise ValueError('The maximum number of toppings cannot be less or equal to zero')
        else:
            self.__max_number_of_toppings=value
    
    def add_topping(self, topping: Topping):
        if len(self.toppings)>=self.max_number_of_toppings:
            raise ValueError('Not enough space for another topping')
        elif topping.topping_type in self.toppings:
            self.toppings[topping.topping_type]+=topping.weight
        else:
            self.toppings[topping.topping_type] = topping.weight
    
    def calculate_total_weight(self):
        return self.dough.weight + sum(self.toppings.values())
            
        

    


