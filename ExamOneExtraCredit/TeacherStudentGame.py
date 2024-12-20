#!/usr/bin/env python3


from src.Chess import Chess
from src.Checkers import Checkers
from src.Student import Student
from src.Teacher import Teacher

def main():
    player1 = Student("Alice")
    player2 = Teacher("Bob")
    chess_game = Chess(player1, player2)
    chess_game.play()
    player1 = Student("Ryan")
    player2 = Teacher("Ethan")
    checkers_game = Checkers(player1, player2)
    checkers_game.play()

if __name__ == "__main__":
    main()
