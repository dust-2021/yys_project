import random

from typing import List

defensive_ = 300


class Role:
    def __init__(self, name: str, health: float, attack: float, defensive: float, speed: float):
        self.name = name
        self.health = health
        self.attack = attack
        self.defensive = defensive
        self.speed = speed
        self.living: bool = True
        self.target_num: int = 0
        self.critical_rate: float = 0.1
        self.critical_damage: float = 1.5

        self.skills = [object]
        self.buff = {
            "buff_name": [],
            "buff": {
                "yu_hun_combine": {"four": None, "two": None}
            },
            "debuff": {}
        }

    def skill_select(self):
        tar_get = int(input(f"选择:{self.skills.__str__()}"))
        var = self.skills[tar_get - 1]

    def attacked_by_role(self, damage_value):
        self.health -= damage_value * (defensive_ / (defensive_ + self.defensive)) * (1 - 0.01 * random.random())
        if self.health <= 0:
            self.living = False

    def __repr__(self):
        # return self.__getattribute__('name') + ':' + str(self.__getattribute__('health')) + '\n'
        if self.living:
            return f"camp:{self.__getattribute__('camp')},{self.name.__str__()}:HP:{self.health.__str__()}," \
                   f"buff:{self.buff['buff_name']}."
        else:
            return f"{self.name}已阵亡!"

