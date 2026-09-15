class Player:

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int):
        if skill_name in self.skills:
            return "Skill already added"

        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        base_info = f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}"

        if not self.skills:
            return base_info

        skills_info = "\n".join(f"==={skill} - {mana_cost}" for skill, mana_cost in self.skills.items())
        return f"{base_info}\n{skills_info}"