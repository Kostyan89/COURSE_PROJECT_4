from abc import ABC

from game.skills import Skill


class Personage(ABC):
    name: str = NotImplemented
    max_health: float = NotImplemented
    max_stamina: float = NotImplemented
    stamina: float = NotImplemented
    attack: float = NotImplemented
    armor: float = NotImplemented
    skill: Skill = NotImplemented
