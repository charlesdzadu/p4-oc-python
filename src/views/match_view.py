from typing import Callable
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
        print(f"{match.player_1.first_name} {match.player_1.last_name} - vs {match.player_2.first_name} {match.player_2.last_name}")
        print("\n1. Modifier le score")
        print("2. Retour")
        choice = input("Entrez votre choix : ")
        if choice == "1":
            # TODO: Implement score modification
            pass
        else:
            self.back()
        
        
