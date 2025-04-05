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
        print(LOGO_TOURNOI_ECHECS)
        print("\nBienvenue dans le programme de gestion de tournois d'echecs !")
        print("1. Joueurs")
        print("2. Tournois")
        print("3. Quitter")
        choice = input("\nEntrez votre choix : ")
        if choice == "1":
            players_view = PlayersView(self.start)
            players_view.menu()
        elif choice == "2":
            tournament_view = TournamentView(self.start)
            tournament_view.menu()
        elif choice == "3":
            self.stop()

    def tournaments_menu(self):
        """
        Display the tournaments menu
        """
        print("\n1. Créer un tournoi")
        print("2. Afficher les tournois")
        print("3. Retour")
        choice = input("Entrez votre choix : ")
        if choice == "1":
            self.create_tournament()
        elif choice == "2":
            self.display_tournaments()
        elif choice == "3":
            self.start()
