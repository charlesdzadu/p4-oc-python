from datetime import datetime
from typing import Callable
from src.helpers.colors import bcolors
from src.helpers.safe_input import safe_input
from src.helpers.validator import is_valid_player_national_id
from src.models.player import Player
from src.controllers.player_controller import PlayerController


class PlayersView:
    """ View for players """

    def __init__(self, back: Callable):
        self.back = back

    def menu(self):
        """
        Display the players menu
        """
        print(f"\n{bcolors.BOLD}Gestion des joueurs{bcolors.ENDC}")
        print("1. Ajouter un joueur")
        print("2. Afficher les joueurs")
        print("3. Retour")
        choice = safe_input("Entrez votre choix : ", type=int, min_value=1, max_value=3)
        if choice == 1:
            self.add_player_from_menu(lambda: self.menu())
        elif choice == 2:
            player_controller = PlayerController()
            players: list[Player] = player_controller.get_az_list()
            self.display_players(players)
        elif choice == 3:
            self.back()

    def add_player_from_menu(self, back: Callable):
        """
        Add a player
        
        Args:
            back: Callable - The function to call when the user wants to go back to the previous menu
        
        Returns:
            None
        """
        print("\nAjout d'un joueur")
        id_national = safe_input("ID national du joueur (format : AA00000) : ", type=str)
        if not is_valid_player_national_id(id_national):
            print(f"{bcolors.FAIL}Erreur : L'ID national du joueur doit contenir 7 caractères alphanumériques, avec les 2 premiers caractères en lettres et les 5 suivants en chiffres.{bcolors.ENDC}")
            back()
         
         
        # Check if the player already exists
        id_national = id_national.upper()
        player = Player.get_by_id_national(id_national)
        if player:
            print(f"{bcolors.FAIL}Erreur : Le joueur avec l'ID national {id_national} existe déjà.{bcolors.ENDC}")
            back()

        last_name = safe_input("Nom du joueur : ", type=str)
        first_name = safe_input("Prénom du joueur : ", type=str)
        birth_date = safe_input("Date de naissance (format : jj/mm/aaaa) : ", type=datetime.date)

        player = Player(id_national, last_name, first_name, birth_date)
        player = player.save()
        print("\nJoueur ajouté avec succès !")
        back()

    def display_players(self, players: list[Player], return_to_menu: Callable | None = None):
        """
        Display all players
        
        Args:
            players: list[Player] - The list of players to display
        
        Returns:
            None
        """
        index: int = 1
        print(f"\n{bcolors.BOLD}Liste des joueurs (de A à Z){bcolors.ENDC}")
        for player in players:
            print(f"{index}. {player}")
            index += 1

        go_back = safe_input("\nAppuyez sur 0 pour revenir au menu précédent ", type=int, min_value=0, max_value=0)
        if go_back == 0:
            if return_to_menu:
                return_to_menu()
            else:   
                self.back()
