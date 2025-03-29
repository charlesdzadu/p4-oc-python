from datetime import date
import datetime as dt
import json
import os
from src.helpers.id_generator import generate_id
from src.helpers.constants import TOURNAMENTS_DB_FILE
from src.models.player import Player
from src.models.round import Round


class Tournament:
    def __init__(
        self,
        name: str,
        location: str,
        start_date: str,
        end_date: str,
        rounds_count: int = 4,
        current_round: int = 1,
        players: list[Player] = [],
        rounds: list[Round] = [],
        description: str = "",
        id: str = None,
    ):
        self.id: str = id if id else generate_id()
        self.name: str = name
        self.location: str = location
        self.players: list[Player] = players
        self.rounds: list[Round] = rounds
        self.description: str = description
        self.rounds_count: int = rounds_count
        self.start_date: date = dt.datetime.strptime(start_date, "%d/%m/%Y")
        self.end_date: date = dt.datetime.strptime(end_date, "%d/%m/%Y")
        self.current_round: int = current_round

    def __str__(self):
        return f"{self.name}"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "description": self.description,
            "start_date": self.start_date.strftime("%d/%m/%Y"),
            "end_date": self.end_date.strftime("%d/%m/%Y"),
            "rounds_count": self.rounds_count,
            "current_round": self.current_round,
            "players": [player.id for player in self.players],
            "rounds": [round.id for round in self.rounds],
        }

    def save(self):
        os.makedirs(os.path.dirname(TOURNAMENTS_DB_FILE), exist_ok=True)

        tournaments = []
        if os.path.exists(TOURNAMENTS_DB_FILE) and os.path.getsize(TOURNAMENTS_DB_FILE) > 0:
            try:
                with open(TOURNAMENTS_DB_FILE, "r") as f:
                    tournaments = json.load(f)
            except json.JSONDecodeError:
                tournaments = []

        tournaments.append(self.to_dict())

        with open(TOURNAMENTS_DB_FILE, "w") as f:
            json.dump(tournaments, f, indent=4)

        return self

    @staticmethod
    def get_by_id(id: str) -> "Tournament":
        """
        Get a tournament by id
        """
        tournaments = Tournament.get_all()
        return next((tournament for tournament in tournaments if tournament.id == id), None)

    @staticmethod
    def get_all() -> list["Tournament"]:
        """
        Get all tournaments from the database
        """
        tournaments = []
        if os.path.exists(TOURNAMENTS_DB_FILE) and os.path.getsize(TOURNAMENTS_DB_FILE) > 0:
            try:
                with open(TOURNAMENTS_DB_FILE, "r") as f:
                    tournaments = json.load(f)
            except json.JSONDecodeError:
                tournaments = []

        tmp = []

        # Get all players and rounds for each tournament
        for tournament in tournaments:
            t_players = []
            for player_id in tournament["players"]:
                player = Player.get(player_id)
                if player:
                    t_players.append(player)

            t_rounds = []
            for round_id in tournament["rounds"]:
                round = Round.get_by_id(round_id)
                if round:
                    t_rounds.append(round)

            tmp.append(Tournament(
                id=tournament["id"],
                name=tournament["name"],
                location=tournament["location"],
                description=tournament["description"],
                players=t_players,
                rounds=t_rounds,
                start_date=tournament["start_date"],
                end_date=tournament["end_date"],
                rounds_count=tournament["rounds_count"],
                current_round=tournament["current_round"],
            ))

        return tmp
