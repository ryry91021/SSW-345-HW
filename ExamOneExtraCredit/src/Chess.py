# Chess.py
from .PairGame import PairGame
from .Student import Student
from .Teacher import Teacher

class Chess(PairGame):
    def __init__(self, p1, p2):
        super().__init__("Chess", p1, p2)

    def play(self):
        player_one = "the student" if isinstance(self.p1, Student) else "the teacher"
        player_two = "the student" if isinstance(self.p2, Student) else "the teacher"

        print(f"{player_one} {self.p1.name} is playing Chess against {player_two} {self.p2.name}")
