from typing import Callable

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
        print(f"Date de début : {round.started_at}")
        print(f"Date de fin : {round.finished_at}")
        
        print(f"\nMatches ({len(round.matches)}) :")
        for i, match in enumerate(round.matches):
            status = " - Terminé" if match.is_finished else " - Pas renseigné"
            print(f"{i+1}. {match.player_1.first_name} {match.player_1.last_name} {match.score_player_1} vs {match.score_player_2} {match.player_2.first_name} {match.player_2.last_name}{status}")
        
        match_index = int(input("\nEntrez l'index du match à afficher : "))
        if match_index > 0 and match_index <= len(round.matches):
            match = round.matches[match_index - 1]
            match_view = MatchView(lambda: self.display_single_round(round))
            match_view.display_single_match(match)
        else:
            print("Index invalide.")
            self.display_single_round(round)
        