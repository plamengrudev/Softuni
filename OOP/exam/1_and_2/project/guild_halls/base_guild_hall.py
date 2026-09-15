from abc import ABC, abstractmethod

class BaseGuildHall(ABC):

    def __init__(self, alias: str):
        self.alias = alias
        self.members = []

    @property
    def alias(self):
        return self._alias
    
    @alias.setter
    def alias(self, value):
        if len(value.strip()) < 2 or not all(character.isalpha() or character.isspace() for character in value):
            raise ValueError('Guild hall alias is invalid!')
        self._alias = value
    
    @property
    @abstractmethod
    def max_member_count(self) -> int:
        pass

    def calculate_total_gold(self):
        if not self.members:
            return 0
        return sum(member.gold for member in self.members)
    
    def status(self):
        members_info = ' *'.join(sorted(member.tag for member in self.members)) or 'N/A'
        return (
            f"Guild hall: {self.alias}; Members: {members_info}; "
            f"Total gold: {self.calculate_total_gold()}"
        )
    
    @property
    @abstractmethod
    def gold_increase_amount(self) -> int:
        pass

    def increase_gold(self, min_skill_level_value: int):
        for member in self.members:
            if member.skill_level >= min_skill_level_value:
                member.gold+=self.gold_increase_amount

