from abc import ABC, abstractmethod

class Human(ABC):
    def __init__(self, name):
        self.name = name
        self._profession = None  # Initialize with None or a default value

    @abstractmethod
    def _setProfession(self):
        pass

    @property
    def getProfession(self):
        return self._profession
