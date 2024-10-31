from .Human import Human

class Student(Human):
    def __init__(self, name):
        super().__init__(name)
        self._setProfession()

    def _setProfession(self):
        self._profession = "Student"

    @property
    def profession(self):
        return self._profession
