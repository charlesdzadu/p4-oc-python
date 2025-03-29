from typing import Callable
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
        print("\n1. Ajouter un joueur")
        print("2. Afficher les joueurs")
        print("3. Retour")
        choice = input("Entrez votre choix : ")
        if choice == "1":
            self.add_player_from_menu(self.menu)
        elif choice == "2":
            player_controller = PlayerController()
            players: list[Player] = player_controller.get_az_list()
            self.display_players(players)
        elif choice == "3":
            self.back()
    
    def add_player_from_menu(self, back: Callable):
        """
        Add a player
        """
        print("\nAjout d'un joueur")
        id_national = input("ID national du joueur : ")
        last_name = input("Nom du joueur : ")
        first_name = input("Prénom du joueur : ")
        birth_date = input("Date de naissance (format : jj/mm/aaaa) : ")
        
        player = Player(id_national, last_name, first_name, birth_date)
        player = player.save()
        print("\nJoueur ajouté avec succès !")
        back()
        
    def display_players(self, players: list[Player]):
        """
        Display all players
        """
        index: int = 1
        print("\nListe des joueurs (de A à Z) :")
        for player in players:
            print(f"{index}. {player}")
            index += 1
            
        go_back = input("\nAppuyez sur 'Enter' pour revenir au menu précédent")
        if go_back:
            self.back()
        
        
