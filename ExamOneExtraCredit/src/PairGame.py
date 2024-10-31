from abc import ABC, abstractmethod

class PairGame(ABC):
    _m_players = 0

    def __init__(self, game, p1=None, p2=None):
        self.game = game
        self.p1 = None
        self.p2 = None
        if p1:
            self.set_player_one(p1)
        if p2:
            self.set_player_two(p2)

    def set_player_one(self, player):
        if player is None:
            raise ValueError("Player one cannot be None.")
        if self.p1 is None:
            PairGame._m_players += 1
        self.p1 = player

    def set_player_two(self, player):
        if player is None:
            raise ValueError("Player two cannot be None.")
        if self.p2 is None:
            PairGame._m_players += 1
        self.p2 = player

    @abstractmethod
    def play(self):
        if PairGame._m_players != 2:
            raise ValueError("Both players must be set before playing.")
        pass
