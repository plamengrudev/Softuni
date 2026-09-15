from project.customer import Customer
from project.dvd import DVD

class MovieWorld:

    def __init__(self,name: str):
        self.name=name
        self.customers: list[Customer]=[]
        self.dvds: list[DVD]=[]

    @staticmethod
    def dvd_capacity() -> int:
        return 15
    
    @staticmethod
    def customer_capacity() -> int:
        return 10
    
    def add_customer(self,customer: Customer):
        if len(self.customers)<self.customer_capacity():
            self.customers.append(customer)
    
    def add_dvd(self,dvd: DVD):
        if len(self.dvds)<self.dvd_capacity():
            self.dvds.append(dvd)
    
    def rent_dvd(self, customer_id: int, dvd_id: int):
        cust=next((c for c in self.customers if c.id==customer_id),None)
        dvd=next((d for d in self.dvds if dvd_id==d.id),None)
        if cust:
            if dvd in cust.rented_dvds:
                return f'{cust.name} has already rented {dvd.name}'
            elif dvd.is_rented:
                return f'DVD is already rented'
            elif cust.age<dvd.age_restriction:
                return f'{cust.name} should be at least {dvd.age_restriction} to rent this movie'
            dvd.is_rented=True
            cust.rented_dvds.append(dvd)
            return f'{cust.name} has successfully rented {dvd.name}'
    
    def return_dvd(self,customer_id: int, dvd_id: int):
        cust=next((c for c in self.customers if c.id==customer_id),None)
        dvd=next((d for d in self.dvds if dvd_id==d.id),None)
        if dvd in cust.rented_dvds:
            cust.rented_dvds.remove(dvd)
            dvd.is_rented=False
            return f'{cust.name} has successfully returned {dvd.name}'
        return f'{cust.name} does not have that DVD'
    
    def __repr__(self):
        result=[]
        [result.append(c.__repr__()) for c in self.customers]
        [result.append(d.__repr__()) for d in self.dvds]

        return '\n'.join(result)
        


