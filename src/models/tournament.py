from datetime import date
from models.player import Player
from models.round import Round


class Tournament:
    def __init__(
        self,
        name: str,
        location: str,
        start_date: date,
        end_date: date,
        rounds_count: int = 4,
        current_round: int = 1,
        players: list[Player] = [],
        rounds: list[Round] = [],
        description: str = "",
    ):
        self.name = name
        self.location = location
        self.players = players
        self.rounds = rounds
        self.description = description
        self.rounds_count = rounds_count
        self.start_date = start_date
        self.end_date = end_date
        self.current_round = current_round
        

        
    def __str__(self):
        return f"{self.name} - {self.location} - {self.description} - {self.rounds_count}"
    
    
        
        
        