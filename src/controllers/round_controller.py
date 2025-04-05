from datetime import datetime
import random
from src.models.round import Round
from src.controllers.player_controller import PlayerController
from src.controllers.tournament_controller import TournamentController
from src.models.player import Player
from src.models.tournament import Tournament
from src.models.match import Match

class RoundController:
    def __init__(self, tournament: Tournament):
        self.tournament = tournament
        self.player_controller = PlayerController()
    
    def is_last_round_finished(self) -> bool:
        """ Check if the last round is finished """
        return self.tournament.rounds[-1].finished_at is not None
    
    def start_round(self) -> dict:
        """ 
        Start a new round for a tournament.
        
        Args:
            tournament (Tournament): The tournament to start the round for.
            
        Returns:
            None
        """
        current_round = self.tournament.current_round
        if current_round == 0:
            round = self.create_new_round(is_first_round=True)
            return {
                "success": True,
                "message": "Le premier tour est créé avec succès. ",
                "round": round,
            }

        elif current_round >= self.tournament.rounds_count:
            return {
                "success": False,
                "message": "Le nombre maximum de tours est atteint",
                "round": None,
            }
        else:
            if self.is_last_round_finished():
                round = self.create_new_round()
                return {
                    "success": True,
                    "message": f"Le tour {round.name} est créé avec succès. ",
                    "round": round,
                }
            else:
                return {
                    "success": False,
                    "message": "Le dernier tour n'est pas terminé. Veuillez terminer le tour avant de créer un nouveau tour.",
                    "round": None,
                }
        
    
    
    
    def create_matches(self, players_with_score: list[tuple[Player, int]]) -> list[Match]:
        """ Create matches for a round """
        matches = []
        for i in range(0, len(players_with_score), 2):
            if i + 1 < len(players_with_score):
                player1 = players_with_score[i][0]
                player2 = players_with_score[i + 1][0]
                player1_color = random.choice(["white", "black"]) 
                player2_color = "black" if player1_color == "white" else "white"
                match = Match(
                    player_1=player1,
                    player_2=player2,
                    player_1_color=player1_color,
                    player_2_color=player2_color,
                )
                matches.append(match)
        
        return matches
        
    def create_new_round(self, is_first_round: bool = False):
        """ """
        players = self.tournament.players
        tournament_controller = TournamentController()
        players_with_score: list[tuple[Player, int]] = []
        
        # Get total score for each player
        for player in players:
            score = tournament_controller.get_single_player_total_score(player, self.tournament)
            players_with_score.append((player, score))
        
        # Sort players with score by score
        players_with_score.sort(key=lambda x: x[1], reverse=True)
        
        if is_first_round:
            # Shuffle players with score to make the first round random
            random.shuffle(players_with_score)
        
        # Create matches
        matches = self.create_matches(players_with_score)
        
        # Create a new round
        for match in matches:
            match.save()
            
        round = Round(
            name=f"Round {self.tournament.current_round + 1}",
            matches=matches,
            started_at=datetime.now(),
        )
        round.save()
        
        self.tournament.current_round += 1
        self.tournament.rounds.append(round)
        self.tournament.save()
        
        return round
        
        
        
        
            
            
            