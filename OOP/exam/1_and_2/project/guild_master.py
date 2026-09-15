from project.guild_members.mage import Mage
from project.guild_members.warrior import Warrior
from project.guild_halls.combat_hall import CombatHall
from project.guild_halls.magic_tower import MagicTower
from project.guild_halls.base_guild_hall import BaseGuildHall

class GuildMaster:

    def __init__(self):
        self.members = []
        self.guild_halls = []
    
    def add_member(self,member_type: str, member_tag: str, member_gold: int):
        member_types={
            "Mage": Mage,
            "Warrior": Warrior
        }
        if member_type not in member_types:
            raise ValueError('Invalid member type!')

        if any(member.tag == member_tag for member in self.members):
            raise ValueError(f'{member_tag} has already been added!')
        
        member_class = member_types[member_type]
        new_member = member_class(member_tag, member_gold)
        self.members.append(new_member)
        return f"{member_tag} is successfully added as {member_type}."
    
    def add_guild_hall(self,guild_hall_type: str, guild_hall_alias: str):
        hall_types={
            "CombatHall": CombatHall,
            "MagicTower": MagicTower
        }

        if guild_hall_type not in hall_types:
            raise ValueError('Invalid guild hall type!')
        
        if any(hall.alias == guild_hall_alias for hall in self.guild_halls):
            raise ValueError(f'{guild_hall_alias} has already been added!')
        
        hall_class = hall_types[guild_hall_type]
        new_hall = hall_class(guild_hall_alias)
        self.guild_halls.append(new_hall)
        return f"{guild_hall_alias} is successfully added as a {guild_hall_type}."

    
    def assign_member(self,guild_hall_alias: str, member_type: str):
        guild_hall = next(
            (hall for hall in self.guild_halls if hall.alias == guild_hall_alias),
            None,
        )
        if guild_hall is None:
            raise ValueError(f'Guild hall {guild_hall_alias} does not exist!')
        if not any(member.role == member_type for member in self.members):
            raise ValueError('No available members of the type!')
        if len(guild_hall.members) >= guild_hall.max_member_count:
            return 'Maximum member count reached. Assignment is impossible.'
        member = next(
            member for member in self.members
            if member.role == member_type
        )

        guild_hall.members.append(member)
        self.members.remove(member)
        return f"{member.tag} was assigned to {guild_hall_alias}."
    
    def practice_members(self, guild_hall: BaseGuildHall, sessions_number: int):
        for _ in range(sessions_number):
            for member in guild_hall.members:
                member.practice()

        total_skill_level = sum(
            member.skill_level for member in guild_hall.members
        )

        return (
            f"{guild_hall.alias} members have {total_skill_level} "
            f"total skill level after {sessions_number} practice session/s."
        )

    def unassign_member(self, guild_hall: BaseGuildHall, member_tag: str):
        member = next(
            (member for member in guild_hall.members if member.tag == member_tag),
            None
        )

        if member is None or member.skill_level == 10:
            return "The unassignment process was canceled."

        guild_hall.members.remove(member)
        self.members.append(member)

        return f"Unassigned member {member_tag}."
    
    def guild_update(self, min_skill_level_value: int):
        for guild_hall in self.guild_halls:
            guild_hall.increase_gold(min_skill_level_value)

        sorted_halls = sorted(
            self.guild_halls,
            key=lambda hall: (-len(hall.members), hall.alias)
        )

        result = [
            "<<<Guild Updated Status>>>",
            f"Unassigned members count: {len(self.members)}",
            f"Guild halls count: {len(self.guild_halls)}",
        ]

        result.extend(f">>>{hall.status()}" for hall in sorted_halls)

        return "\n".join(result)
            
            
