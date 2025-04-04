import json
import os
from typing import Literal
from src.helpers.constants import MATCHES_DB_FILE
from src.helpers.id_generator import generate_id
from src.models.player import Player


class Match:
    def __init__(
        self,
        player_1: Player,
        player_2: Player,
        score_player_1: int = 0,
        score_player_2: int = 0,
        player_1_color: Literal["white", "black"] = "white",
        player_2_color: Literal["white", "black"] = "black",
        id: str = None,
        is_finished: bool = False,
    ):
        self.id = id if id else generate_id()
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_player_1 = score_player_1
        self.score_player_2 = score_player_2
        self.player_1_color = player_1_color
        self.player_2_color = player_2_color
        self.is_finished = is_finished

    def __str__(self):
        return f"{self.player_1} {self.score_player_1} - {self.score_player_2} {self.player_2}"

    def __repr__(self):
        return self.__str__()

    def to_dict(self):
        return {
            "id": self.id,
            "player_1": self.player_1.id,
            "player_2": self.player_2.id,
            "score_player_1": self.score_player_1,
            "score_player_2": self.score_player_2,
            "player_1_color": self.player_1_color,
            "player_2_color": self.player_2_color,
            "is_finished": self.is_finished,
        }

    def save(self):
        os.makedirs(os.path.dirname(MATCHES_DB_FILE), exist_ok=True)

        matches = []
        if os.path.exists(MATCHES_DB_FILE) and os.path.getsize(MATCHES_DB_FILE) > 0:
            try:
                with open(MATCHES_DB_FILE, "r") as f:
                    matches = json.load(f)
            except json.JSONDecodeError:
                matches = []

        # Check if match with same ID exists
        match_updated = False
        for i, match in enumerate(matches):
            if match["id"] == self.id:
                matches[i] = self.to_dict()
                match_updated = True
                break
        
        # If match wasn't found, append new one
        if not match_updated:
            matches.append(self.to_dict())

        with open(MATCHES_DB_FILE, "w") as f:
            json.dump(matches, f, indent=4)

        return self

    @staticmethod
    def get_all() -> list["Match"]:
        matches: list[Match] = []
        if os.path.exists(MATCHES_DB_FILE) and os.path.getsize(MATCHES_DB_FILE) > 0:
            try:
                with open(MATCHES_DB_FILE, "r") as f:
                    matches_dicts = json.load(f)
                    for match_dict in matches_dicts:
                        match = Match(
                            id=match_dict["id"],
                            player_1=Player.get(match_dict["player_1"]),
                            player_2=Player.get(match_dict["player_2"]),
                            score_player_1=match_dict["score_player_1"],
                            score_player_2=match_dict["score_player_2"],
                            player_1_color=match_dict["player_1_color"],
                            player_2_color=match_dict["player_2_color"],
                            is_finished=match_dict["is_finished"],
                        )
                        matches.append(match)
            except json.JSONDecodeError:
                matches: list[Match] = []

        return matches

    @staticmethod
    def get(id: str) -> "Match":
        matches = Match.get_all()
        for match in matches:
            if match.id == id:
                return match
        return None
