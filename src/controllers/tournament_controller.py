from src.models.tournament import Tournament


class TournamentController:
    """ Controller for tournaments """

    def get_all_tournaments():
        """ Get all tournaments """
        return Tournament.get_all()

    def get_tournament_by_id(id: str):
        """ Get a tournament by id """
        return Tournament.get_by_id(id)
