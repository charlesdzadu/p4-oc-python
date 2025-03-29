from models.player import Player


class Match:
    def __init__(self, player_1: Player, player_2: Player):
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_player_1 = 0
        self.score_player_2 = 0
        
    def __str__(self):
        return f"{self.player_1} {self.score_player_1} - {self.score_player_2} {self.player_2}"
    
    def __repr__(self):
        return self.__str__()
    
    def to_dict(self):
        return {
            "player_1": self.player_1.to_dict(),
            "player_2": self.player_2.to_dict(),
            "score_player_1": self.score_player_1,
            "score_player_2": self.score_player_2,
        }
        
        
        
