from src.models.player import Player
from typing import Callable

class PlayerController:
    """ Controller for players """
    
    def get_az_list(self) -> list[Player]:
        """ Get all players sorted by last name """
        players: list[Player] = Player.get_all()
        return sorted(players, key=lambda x: x.last_name)
        
        
    
    
    