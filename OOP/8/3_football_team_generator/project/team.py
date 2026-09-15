from project.player import Player
class Team:

    def __init__(self,name: str, rating: int):
        self.__name=name
        self.__rating=rating
        self.__players=[]
    
    def add_player(self,player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        else:
            self.__players.append(player)
            return f"Player {player.name} joined team {self.__name}"
        
    def remove_player(self, player: str):
        p=next((pl for pl in self.__players if pl.name==player),None)
        if p:
            self.__players.remove(p)
            return p
        return f"Player {player} not found"
