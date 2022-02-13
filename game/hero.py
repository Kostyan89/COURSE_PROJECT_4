from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Type, Optional

from game.equipment import Weapon, Armor
from game.personages import Personage


class Hero(ABC):
    def __init__(self, class_: Type[Personage], weapon: Weapon, armor: Armor, name: str):
        self.class_ = class_
        self.weapon = weapon
        self.armor = armor
        self._stamina = self.class_.max_stamina
        self._hp = self.class_.max_health
        self.skill_user: bool = False
        self.name = name

    @property
    def hp(self):
        return round(self._hp, 1)

    @hp.setter
    def hp(self, value):
        self._hp = value

    @property
    def stamina(self):
        return round(self._stamina, 1)

    @stamina.setter
    def stamina(self, value):
        self._stamina = value

    @abstractmethod
    def hit(self, target: Hero) -> Optional[float]:
        ...


class Enemy(Hero):
    ...


class Player(Hero):
    ...

