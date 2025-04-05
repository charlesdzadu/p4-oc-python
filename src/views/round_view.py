from datetime import datetime
from typing import Callable

from src.helpers.safe_input import safe_input
from src.models.round import Round
from src.helpers.colors import bcolors
from src.views.match_view import MatchView


class RoundView:
    def __init__(self, back: Callable):
        self.back = back
        
    def display_single_round(self, round: Round):
        """
        Display a single round
        """
        print(f"\n{bcolors.OKGREEN}Tour {round.name} : {bcolors.ENDC}")
        print(f"Nombre de matches : {len(round.matches)}")
        print(f"Date de début : {round.started_at}")
        print(f"Date de fin : {round.finished_at}")
        
        print("Entrez -1 pour revenir à la liste des tours")
        if not round.finished_at:
            print("Entrez 0 pour terminer le tour")
            
            
        
        print(f"\nMatches ({len(round.matches)}) :")
        for i, match in enumerate(round.matches):
            if match.is_finished:
                status = f" - {bcolors.OKGREEN}Terminé{bcolors.ENDC}"
            else:
                status = f" - {bcolors.OKBLUE}Pas renseigné{bcolors.ENDC}"
                
            print(f"{i+1}. {match.player_1.first_name} {match.player_1.last_name} {match.score_player_1} vs {match.score_player_2} {match.player_2.first_name} {match.player_2.last_name}{status}")
        
        match_index = safe_input("\nEntrez l'index du match à afficher : ", type=int, min_value=-1, max_value=len(round.matches) + 1)
        match_index = int(match_index)
        if match_index > 0 and match_index <= len(round.matches):
            match = round.matches[match_index - 1]
            match_view = MatchView(lambda: self.display_single_round(round))
            match_view.display_single_match(match)
        else:
            if match_index == -1:
                self.back()
                return
            elif match_index == 0:
                round.finished_at = datetime.now()
                round.save()
               
            self.display_single_round(round)
        