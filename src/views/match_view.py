from typing import Callable
from src.helpers.safe_input import safe_input
from src.helpers.constants import DRAW_SCORE, LOSER_SCORE, WINNER_SCORE
from src.helpers.colors import bcolors
from src.models.match import Match


class MatchView:
    def __init__(self, back: Callable):
        self.back = back
        
    def display_single_match(self, match: Match):
        """
        Display a single match
        """
        print(f"\n{bcolors.OKGREEN}Match {match.id} : {bcolors.ENDC}")
        print(f"{match.player_1.first_name} {match.player_1.last_name} - {match.score_player_1} vs {match.score_player_2} {match.player_2.first_name} {match.player_2.last_name}")
        
        print("\n1. Modifier le score")
        print("2. Retour")
        choice = safe_input("Entrez votre choix : ", type=int, min_value=1, max_value=2)
        choice = int(choice)
        if choice == 1:
            self.update_single_match_menu(match)
        else:
            self.back()
            
    def update_single_match_menu(self, match: Match):
        """
        Display the update match menu
        """
        print(f"\n{bcolors.OKGREEN}Match {match.id} : {bcolors.ENDC}")
        print(f"{match.player_1.first_name} {match.player_1.last_name} - vs {match.player_2.first_name} {match.player_2.last_name}")
        
        print("\nQui a gagné le match ?")
        print(f"1. {match.player_1.first_name} {match.player_1.last_name}")
        print(f"2. {match.player_2.first_name} {match.player_2.last_name}")
        print(f"3. Match nul")
        choice = safe_input("Entrez votre choix : ", type=int, min_value=1, max_value=3)
        choice = int(choice)
        if choice == 1:
            match.score_player_1 = WINNER_SCORE
            match.score_player_2 = LOSER_SCORE
        elif choice == 2:
            match.score_player_1 = LOSER_SCORE
            match.score_player_2 = WINNER_SCORE
        else:
            match.score_player_1 = DRAW_SCORE
            match.score_player_2 = DRAW_SCORE
            
        message = f"\nLe match {match.id} a été mis à jour avec le score {match.score_player_1} - {match.score_player_2}"
        print(f"{bcolors.OKGREEN}{message}{bcolors.ENDC}")
            
        match.is_finished = True
        match.save()
        
        self.display_single_match(match)
        
