from dataclasses import dataclass
@dataclass
class Movie:
    id : int
    name : str
    year : int
    rank : float

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return f"{self.name}"