from dataclasses import dataclass

from model.movie import Movie


@dataclass
class Arco:
    m1 : Movie
    m2 : Movie
    peso : int