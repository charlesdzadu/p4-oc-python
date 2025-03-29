from datetime import datetime
from src.models.match import Match
from src.helpers.id_generator import generate_id


class Round:
    def __init__(
        self,
        name: str,
        matches: list[Match],
        id: str = None,
    ):
        self.id = id if id else generate_id()
        self.name = name
        self.matches = matches
        self.started_at = None
        self.finished_at = None

    def start(self):
        self.started_at = datetime.now()

    def finish(self):
        self.finished_at = datetime.now()

    def __str__(self):
        return f"{self.name} - {self.matches}"
