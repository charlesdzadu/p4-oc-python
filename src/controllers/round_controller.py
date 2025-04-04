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
    def start_round(self):
        """ 
        Start a new round for a tournament.
        
        Args:
            tournament (Tournament): The tournament to start the round for.
            
        Returns:
            None
        """
        
        
        #1. Check if current is 0
        #2. If yes, create a new round
        #3. If no check if all the matches are played
        #4. If yes, create a new round
        #5. To create a new round. 
        #5.1. Name it "Round X" and X is the current round + 1
        #5.2. Set the current round to the new round
        #5.3. Si c'est le premier tour on va melanger les joueurs de façon aléatoire.
        #5.4. Sinon le tour est gérer dynamique de cette façon :
        #5.4.1. Triez tous les joueurs en fonction de leur nombre total de points dans le tournoi.
        #5.4.2. Associez les joueurs dans l'ordre (le joueur 1 avec le joueur 2, le joueur 3 avec le joueur 4 et ainsi de suite.)
        #5.4.3. Si plusieurs joueurs ont le même nombre de points, vous pouvez les choisir de façon aléatoire.
        #5.4.4. Lors de la génération des paires, évitez de créer des matchs identiques
        #5.4.5. Un tirage au sort des joueurs définira qui joue en blanc et qui joue en noir 
        
        
        
        current_round = self.tournament.current_round
        if current_round == 0:
            # Create a new round
            res = self.create_new_round(is_first_round=True)
            
        elif current_round > self.tournament.rounds_count:
            # Return error message
            pass
        else:
            # Check if all the matches are played
            # If yes, create a new round
            # If no, return error message
            pass
        
    
    
    
    def create_matches(self, players_with_score: list[tuple[Player, int]]) -> list[Match]:
        """ Create matches for a round """
        matches = []
        for i in range(0, len(players_with_score), 2):
            if i + 1 < len(players_with_score):
                player1 = players_with_score[i][0]
                player2 = players_with_score[i + 1][0]
                player1_color = random.choice(["white", "black"]) 
                player2_color = "black" if player1_color == "white" else "white"
                match = Match(player1, player2, player_1_color=player1_color, player_2_color=player2_color)
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
            
        round = Round(name=f"Round {self.tournament.current_round + 1}", matches=matches)
        round.save()
        
        self.tournament.current_round += 1
        self.tournament.save()
        
        return round
        
        
        
        
            
            
            