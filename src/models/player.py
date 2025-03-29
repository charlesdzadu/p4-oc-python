from datetime import datetime
import json
import os


from src.helpers.constants import PLAYERS_DB_FILE
from src.helpers.id_generator import generate_id


class Player:
    def __init__(
        self,
        id_national: str,
        first_name: str,
        last_name: str,
        date_of_birth: str,
        id: str = None,
        points: int = 0
    ):
        self.id = id if id else generate_id()
        self.id_national = id_national
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth: datetime = datetime.strptime(date_of_birth, "%d/%m/%Y")
        self.points = points

    def __str__(self):
        return f"{self.last_name.capitalize()} {self.first_name.capitalize()} - {self.id_national.upper()}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.id_national == other.id_national

    def to_dict(self):
        return {
            "id": self.id,
            "id_national": self.id_national,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth.strftime("%d/%m/%Y"),
            "points": self.points,
        }

    def save(self):
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(PLAYERS_DB_FILE), exist_ok=True)

        # Load existing players or create empty list
        players = []
        if os.path.exists(PLAYERS_DB_FILE) and os.path.getsize(PLAYERS_DB_FILE) > 0:
            try:
                with open(PLAYERS_DB_FILE, "r") as f:
                    players = json.load(f)
            except json.JSONDecodeError:
                # If the file is not proper JSON, start with an empty list
                players = []

        # Add the current player
        players.append(self.to_dict())

        # Write all players back to the file
        with open(PLAYERS_DB_FILE, "w") as f:
            json.dump(players, f, indent=4)

        return self

    @staticmethod
    def get(id: str) -> "Player":
        players = Player.get_all()
        for player in players:
            if player.id == id:
                return player
        return None

    @staticmethod
    def get_by_id_national(id_national: str) -> "Player":
        players = Player.get_all()
        for player in players:
            if player.id_national == id_national:
                return player
        return None

    @staticmethod
    def get_all() -> list["Player"]:
        players = []
        if os.path.exists(PLAYERS_DB_FILE) and os.path.getsize(PLAYERS_DB_FILE) > 0:
            try:
                with open(PLAYERS_DB_FILE, "r") as f:
                    player_dicts = json.load(f)
                    players = [Player(**player_dict) for player_dict in player_dicts]
            except json.JSONDecodeError:
                players = []

        return players
