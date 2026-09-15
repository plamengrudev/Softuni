from project.animal import Animal
from project.worker import Worker
class Zoo:

    def __init__(self,name: str,budget: int,animal_capacity: int,workers_capacity: int):
        self.name=name
        self.__budget=budget
        self.__animal_capacity=animal_capacity
        self.__workers_capacity=workers_capacity
        self.animals=[]
        self.workers=[]
    
    def add_animal(self, animal: Animal, price: float):
        if self.__budget>=price and len(self.animals)<self.__animal_capacity:
            self.animals.append(animal)
            self.__budget-=price
            return f'{animal.name} the {animal.__class__.__name__} added to the zoo'
        elif len(self.animals)<self.__animal_capacity:
            return f'Not enough budget'
        return f'Not enough space for animal'
    
    def hire_worker(self, worker: Worker):
        if len(self.workers)<self.__workers_capacity:
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'
        return f'Not enough space for worker'
    
    def fire_worker(self, worker_name: str):
        if any(w.name==worker_name for w in self.workers):
            worker=next(w for w in self.workers if w.name==worker_name)
            self.workers.remove(worker)
            return f'{worker.name} fired successfully'
        return f'There is no {worker_name} in the zoo'
    
    def pay_workers(self):
        salaries=[w.salary for w in self.workers]
        if self.__budget>=sum(salaries):
            self.__budget-=sum(salaries)
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return f'You have no budget to pay your workers. They are unhappy'
    
    def tend_animals(self):
        cost=[a.money_for_care for a in self.animals]
        if self.__budget>=sum(cost):
            self.__budget-=sum(cost)
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        return f'You have no budget to tend the animals. They are unhappy.'
    
    def profit(self, amount: float):
        self.__budget+=amount

    def animals_status(self):
        lions=[x for x in self.animals if x.__class__.__name__=='Lion']
        tigers=[x for x in self.animals if x.__class__.__name__=='Tiger']
        cheetas=[x for x in self.animals if x.__class__.__name__=='Cheetah']
        result= [f"You have {len(self.animals)} animals"]
        result.append(f"----- {len(lions)} Lions:")
        result.extend(repr(x) for x in lions)
        result.append(f"----- {len(tigers)} Tigers:")
        result.extend(repr(x) for x in tigers)
        result.append(f"----- {len(cheetas)} Cheetahs:")
        result.extend(repr(x) for x in cheetas)

        return "\n".join(result)

    def workers_status(self):
        keepers=[x for x in self.workers if x.__class__.__name__=='Keeper']
        caretakers=[x for x in self.workers if x.__class__.__name__=='Caretaker']
        vets=[x for x in self.workers if x.__class__.__name__=='Vet']

        result= [f"You have {len(self.workers)} workers"]
        result.append(f"----- {len(keepers)} Keepers:")
        result.extend(repr(x) for x in keepers)
        result.append(f"----- {len(caretakers)} Caretakers:")
        result.extend(repr(x) for x in caretakers)
        result.append(f"----- {len(vets)} Vets:")
        result.extend(repr(x) for x in vets)

        return "\n".join(result)


    
