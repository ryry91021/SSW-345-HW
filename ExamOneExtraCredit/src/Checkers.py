from .PairGame import PairGame
from .Student import Student
from .Teacher import Teacher

class Checkers(PairGame):
    def __init__(self, p1, p2):
        super().__init__("Checkers", p1, p2)

    def play(self):
        if isinstance(self.p1, Student):
            p1_profession = "the student"
        elif isinstance(self.p1, Teacher):
            p1_profession = "the teacher"
        else:
            raise TypeError("Player one must be a Student or a Teacher.")

        if isinstance(self.p2, Student):
            p2_profession = "the student"
        elif isinstance(self.p2, Teacher):
            p2_profession = "the teacher"
        else:
            raise TypeError("Player two must be a Student or a Teacher.")
        
        print(f"{p1_profession} {self.p1.name} is playing Checkers against {p2_profession} {self.p2.name}")
