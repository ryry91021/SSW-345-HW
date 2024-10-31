from .PairGame import PairGame
from .Student import Student
from .Teacher import Teacher

class Chess(PairGame):
    def __init__(self, p1, p2):
        super().__init__("Chess", p1, p2)

    def play(self):
        super().play()
        
        p1_profession = "the student" if isinstance(self.p1, Student) else "the teacher"
        p2_profession = "the student" if isinstance(self.p2, Student) else "the teacher"
        
        print(f"{p1_profession} {self.p1.name} is playing Chess against {p2_profession} {self.p2.name}")
