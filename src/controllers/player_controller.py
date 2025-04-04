from src.models.player import Player


class PlayerController:
    """ Controller for players """

    def get_az_list(self) -> list[Player]:
        """ Get all players sorted by last name """
        players: list[Player] = Player.get_all()
        return self.sort_by_last_name(players)

    def sort_by_last_name(self, players: list[Player]) -> list[Player]:
        """ Sort players by last name """
        return sorted(players, key=lambda x: x.last_name)
