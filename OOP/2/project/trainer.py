from project.pokemon import Pokemon

class Trainer:

    def __init__(self,name: str):
        self.name=name
        self.pokemons=[]
    def add_pokemon(self,pokemon: Pokemon):
        if any(p.name == pokemon.name for p in self.pokemons):
            return f'This pokemon is already caught'
        self.pokemons.append(pokemon)
        return f'Caught {pokemon.name} with health {pokemon.health}'
    def release_pokemon(self, pokemon_name: str):
        for pokemon in self.pokemons:
            if pokemon_name==pokemon.name:
                self.pokemons.remove(pokemon)
                return f'You have released {pokemon_name}'
        return f'Pokemon is not caught'
    def trainer_data(self):
        details = "\n- ".join([pokemon.pokemon_details() for pokemon in self.pokemons])
        return f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n- {details}"