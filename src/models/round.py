from datetime import datetime
import json
import os
from src.helpers.constants import ROUNDS_DB_FILE
from src.models.match import Match
from src.helpers.id_generator import generate_id


class Round:
    def __init__(
        self,
        name: str,
        matches: list[Match],
        id: str = None,
        started_at: datetime = None,
        finished_at: datetime = None,
    ):
        self.id = id if id else generate_id()
        self.name = name
        self.matches = matches
        self.started_at = started_at
        self.finished_at = finished_at

    def start(self):
        self.started_at = datetime.now()

    def finish(self):
        self.finished_at = datetime.now()

    def __str__(self):
        return f"{self.name} - {self.matches}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "matches": [match.id for match in self.matches],
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "finished_at": self.finished_at.isoformat() if self.finished_at else None,
        }
    
    def save(self):
        os.makedirs(os.path.dirname(ROUNDS_DB_FILE), exist_ok=True)
        rounds = []
        
        if os.path.exists(ROUNDS_DB_FILE) and os.path.getsize(ROUNDS_DB_FILE) > 0:
            try:
                with open(ROUNDS_DB_FILE, "r") as f:
                    rounds = json.load(f)
            except json.JSONDecodeError:
                rounds = []
        
        # Check if round with same ID exists
        round_updated = False
        for i, round in enumerate(rounds):
            if round["id"] == self.id:
                rounds[i] = self.to_dict()
                round_updated = True
                break
        
        # If round wasn't found, append new one
        if not round_updated:
            rounds.append(self.to_dict())
        
        with open(ROUNDS_DB_FILE, "w") as f:
            json.dump(rounds, f, indent=4)
            
        return self
    
    @staticmethod
    def get_all() -> list["Round"]:
        rounds: list[Round] = []
        if os.path.exists(ROUNDS_DB_FILE) and os.path.getsize(ROUNDS_DB_FILE) > 0:
            try:
                with open(ROUNDS_DB_FILE, "r") as f:
                    rounds_dicts = json.load(f)
                    for round_dict in rounds_dicts:
                        matches_ids = round_dict["matches"]
                        matches = [Match.get(match_id) for match_id in matches_ids]
                        round = Round(
                            name=round_dict["name"],
                            matches=matches,
                            id=round_dict["id"],
                            started_at=datetime.fromisoformat(round_dict["started_at"]) if round_dict["started_at"] else None,
                            finished_at=datetime.fromisoformat(round_dict["finished_at"]) if round_dict["finished_at"] else None,
                        )
                        rounds.append(round)
            except json.JSONDecodeError:
                rounds: list[Round] = []
                
        return rounds
    
    
    @staticmethod
    def get(id: str) -> "Round":
        rounds = Round.get_all()
        for round in rounds:
            if round.id == id:
                return round
        return None
            
            
