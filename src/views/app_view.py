from src.helpers.safe_input import safe_input
from src.helpers.colors import bcolors
from src.helpers.constants import LOGO_TOURNOI_ECHECS
from src.views.players_view import PlayersView
from src.views.tournament_view import TournamentView


class AppView:

    def stop(self):
        """
        Stop the application
        """
        print("Merci pour votre utilisation !")
        exit()

    def start(self):
        """
        Start the application
        """
  
        print("1. Joueurs")
        print("2. Tournois")
        print("3. Quitter")
        choice = safe_input("\nEntrez votre choix : ", type=int, min_value=1, max_value=3)
        if choice == 1:
            players_view = PlayersView(lambda: self.start())
            players_view.menu()
        elif choice == 2:
            tournament_view = TournamentView(lambda: self.start())
            tournament_view.menu()
        elif choice == 3:
            self.stop()
