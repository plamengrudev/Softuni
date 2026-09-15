from project.customer import Customer
from project.trainer import Trainer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription


class Gym:

    def __init__(self):
        self.customers: list[Customer]=[]
        self.trainers: list[Trainer]=[]
        self.equipment: list[Equipment]=[]
        self.plans: list[ExercisePlan]=[]
        self.subscriptions: list[Subscription]=[]
    
    def add_customer(self,customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)
    
    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)
    
    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)
    
    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)
    
    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)
    
    def subscription_info(self, subscription_id: int):
        sub=next((s for s in self.subscriptions if s.id==subscription_id))
        cust=next((c for c in self.customers if c.id==subscription_id))
        trainer=next((t for t in self.trainers if t.id==subscription_id))
        exer=next((e for e in self.plans if e.id==subscription_id))
        equip=next((eq for eq in self.equipment if eq.id==subscription_id))

        return f'{sub}\n{cust}\n{trainer}\n{equip}\n{exer}\n'
        