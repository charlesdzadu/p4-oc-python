from src.models.player import Player
from src.models.tournament import Tournament


class TournamentController:
    """ Controller for tournaments """

    def get_all_tournaments():
        """ Get all tournaments """
        return Tournament.get_all()

    def get_tournament_by_id(id: str):
        """ Get a tournament by id """
        return Tournament.get_by_id(id)

    def get_single_player_total_score(self, player: Player, tournament: Tournament) -> int:
        """ Get the total score of this player in this tournament """
        score = 0
        rounds = tournament.rounds
        for round in rounds:
            matches = round.matches
            for match in matches:
                if match.player_1 == player:
                    score += match.score_player_1
                if match.player_2 == player:
                    score += match.score_player_2
        return score
