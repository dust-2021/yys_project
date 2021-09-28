import random
from functools import reduce

from typing import List

defensive_ = 300


class Role:
    def __init__(self, name: str, health: float, attack: float, defensive: float, speed: float):
        self.name = name
        self.health, self.or_health = health, health
        self.attack, self.or_attack = attack, attack
        self.defensive, self.or_defensive = defensive, defensive
        self.speed, self.or_speed = speed, speed
        self.living: bool = True
        self.target_num: int = 0
        self.critical_rate, self.or_critical_rate = 0.1, 0.1
        self.critical_damage, self.or_critical_damage = 1.5, 1.5
        self.skills = []
        self.buff = []

    def skill_select(self, all_target=None):
        """
        player select a skill
        :param all_target: all the role in the round
        :return: None
        """
        if all_target is None:
            all_target = [[], []]
        tar_get = int(input(f"选择:{self.skills.__str__()}\n"))
        skill = self.skills[tar_get - 1]

        tar_get_list = skill.target_get(self, all_target)

        skill.effect(self, tar_get_list)

    def attacked_by_role(self, role, damage_value):
        """
        role be damage attack
        :param role: the role attack
        :param damage_value: the original damage
        :return: None
        """
        self.health -= damage_value * (defensive_ / (defensive_ + self.defensive)) * (1 - 0.01 * random.random())
        if self.health <= 0:
            self.living = False

    def __repr__(self):
        # return self.__getattribute__('name') + ':' + str(self.__getattribute__('health')) + '\n'
        if self.living:
            return f"camp:{self.__getattribute__('camp')},{self.name.__str__()}:HP:{self.health.__str__()}," \
                   f"buff:{self.buff.__str__()}."
        else:
            return f"{self.name}已阵亡!"
