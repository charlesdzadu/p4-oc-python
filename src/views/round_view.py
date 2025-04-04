from typing import Callable


class RoundView:
    def __init__(self, back: Callable):
        self.back = back
        
    def start_round(self):
        """"""
        