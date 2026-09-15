from project.guild_halls.base_guild_hall import BaseGuildHall

class MagicTower(BaseGuildHall):

    MAX_MEMBER_COUNT=4
    GOLD_INCREASE_AMOUNT=50

    def __init__(self, alias):
        super().__init__(alias)
    
    @property
    def max_member_count(self) -> int:
        return self.MAX_MEMBER_COUNT
    
    @property
    def gold_increase_amount(self) -> int:
        return self.GOLD_INCREASE_AMOUNT
    
    def increase_gold(self, min_skill_level_value: int):
        for member in self.members:
            if member.role == "Mage" and member.skill_level >= min_skill_level_value:
                member.gold *= 2



