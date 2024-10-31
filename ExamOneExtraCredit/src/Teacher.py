from .Human import Human

class Teacher(Human):
    def __init__(self, name):
        super().__init__(name)
        self._setProfession()  # Initialize profession

    def _setProfession(self):
        self._profession = "Teacher"

    @property
    def profession(self):
        return self._profession
