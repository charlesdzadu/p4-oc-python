import datetime
from typing import Callable

from src.controllers.round_controller import RoundController
from src.models.player import Player
from src.helpers.safe_input import safe_input
from src.controllers.player_controller import PlayerController
from src.models.tournament import Tournament
from src.views.players_view import PlayersView
from src.helpers.colors import bcolors
from src.views.round_view import RoundView


class TournamentView:
    def __init__(self, back: Callable):
        self.back = back

    def menu(self):
        print("\n1. Ajouter un tournoi")
        print("2. Afficher les tournois")
        print("3. Retour")
        choice = input("Entrez votre choix : ")
        if choice == "1":
            self.add_tournament_from_menu(self.menu)
        elif choice == "2":
            self.display_tournaments()
        elif choice == "3":
            self.back()

    def display_tournament_details(self, tournament: Tournament, only_menu: bool = False):
        
        
        if not only_menu:
            print(f"\nTournoi : {tournament.name}")
            print(f"Localisation : {tournament.location}")
            print(f"Date : {tournament.start_date}")
            print(f"Description : {tournament.description}")
            print(f"Nombre de tours : {tournament.rounds_count}")
            print(f"Tour actuel : {tournament.current_round}")

        print("\nMenu du tournoi :")
        print("1. Afficher les joueurs")
        print("2. Afficher les tours")
        print("3. Démarrer un tour")
        print("4. Retour")
        choice = input("Entrez votre choix : ")
        choice = int(choice)

        if choice == 1:
            players_view = PlayersView(self.back)
            sorted_player_list = PlayerController().sort_by_last_name(tournament.players)
            players_view.display_players(sorted_player_list)
            
        elif choice == 2:
            self.display_rounds(tournament)
            
        elif choice == 3:
            res = RoundController(tournament).start_round()
            if res["success"]:
                print(f"\n{bcolors.OKGREEN}{res['message']}{bcolors.ENDC}")
            else:
                print(f"\n{bcolors.FAIL}{res['message']}{bcolors.ENDC}")
                
            print("\n")
            self.display_tournament_details(tournament, only_menu=True)
            
        elif choice == 4:
            self.back()

    def display_rounds(self, tournament: Tournament):
        print("\nEntrez 0 pour revenir au menu principal")
        print("\nListe des tours :")
        index = 1
        for round in tournament.rounds:
            message = f"{index}. {round.name}"
            if not round.started_at and not round.finished_at:
                message += f" - {bcolors.OKBLUE}Pas commencé{bcolors.ENDC}"
            elif round.started_at and not round.finished_at:
                message += f" - {bcolors.WARNING}En cours{bcolors.ENDC}"
            elif round.finished_at:
                message += f" - {bcolors.OKGREEN}Terminé{bcolors.ENDC}"
            print(message)
            index += 1
            
        index = safe_input("Entrez l'index du tour à afficher : ", type=int, min_value=0, max_value=len(tournament.rounds))
        index = int(index)
        if index > 0 and index <= len(tournament.rounds):
            round = tournament.rounds[index - 1]
            round_view = RoundView(lambda: self.display_rounds(tournament))
            round_view.display_single_round(round)
        else:
            self.display_tournament_details(tournament, only_menu=True)
            

    def add_tournament_from_menu(self, back: Callable):
        """
        Add a tournament from the menu
        """
        print("\nBienvenue dans la création d'un tournoi ! ♟️\n")
        print("Veuillez fournir les informations du tournoi: ")
        name = safe_input("Nom : ")
        location = safe_input("Localisation : ")
        start_date = safe_input("Date de début (format JJ/MM/AAAA) : ", type=datetime.date, date_format="%d/%m/%Y")
        end_date = safe_input("Date de fin (format JJ/MM/AAAA) : ", type=datetime.date, date_format="%d/%m/%Y")
        description: str = safe_input("Description : ", allow_empty=True)
        rounds_count: int = safe_input("Nombre de tours (4 par défaut) : ", type=int,
                                  min_value=1, max_value=100, allow_empty=True)

        print("\nNous allons maintenant ajouter les joueurs au tournoi.")
        players = []
        while True:
            player_national_id = safe_input("ID National du joueur (ou 'q' pour terminer) : ")
            if not player_national_id:
                break
            player = Player.get_by_id_national(player_national_id)
            if player:
                # Check if the player is already in the tournament
                if player in players:
                    print(f"{bcolors.WARNING} Joueur déjà dans le tournoi.{bcolors.ENDC}")
                else:
                    print(f"{bcolors.OKGREEN} Joueur trouvé : {player.first_name} {player.last_name} (ID National : {player.id_national}){bcolors.ENDC}")
                    players.append(player)
            else:
                print(f"{bcolors.FAIL} Joueur non trouvé.{bcolors.ENDC}")

        tournament = Tournament(
            name=name,
            location=location,
            start_date=start_date,
            end_date=end_date,
            description=description,
            rounds_count=int(rounds_count) if rounds_count else 4,
            players=players
        )

        tournament.save()
        print(f"Tournoi {name} ajouté avec succès.")
        back()

    def display_tournaments(self):
        tournaments = Tournament.get_all()
        if not tournaments or len(tournaments) == 0:
            print("Aucun tournoi trouvé.")
            return
        print("\nListe des tournois (Utilisez l'index pour afficher les détails) :")
        for index, tournament in enumerate(tournaments, start=1):
            print(f"{index}. {tournament}")

        index = int(input("Entrez l'index du tournoi à afficher : "))
        if index > 0 and index <= len(tournaments):
            tournament = tournaments[index - 1]
            self.display_tournament_details(tournament)
        else:
            print("Index invalide.")
