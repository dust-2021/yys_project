import random
from functools import reduce
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

        # 增减伤
        self.out_damage_effect = [1, 1, 1, 1, 1]
        self.get_damage_effect = [1 - self.defensive / (self.defensive + defensive_), 1, 1, 1]

    def round_start(self):
        pass

    def round_end(self):
        pass

    def skill_select(self, all_target=None):
        """
        选择技能影响对象
        :param all_target: 所有对局中角色，由fight实例传入
        :return: 无
        """
        if all_target is None:
            all_target = [[], []]
        tar_get = int(input(f"选择:{self.skills.__str__()}\n"))
        skill = self.skills[tar_get - 1]

        tar_get_list = skill.target_get(self, all_target)
        skill.effect(self, tar_get_list)

    def attacked_by_role(self, role, damage_value):
        """
        角色受到攻击
        :param role: 发起攻击的角色
        :param damage_value: 受到攻击的原始伤害
        :return: 无
        """
        final_damage = damage_value * reduce(lambda x, y: x * y, self.get_damage_effect)
        self.health -= final_damage
        print(f"{self.name}受到{role.name}{final_damage}点伤害")
        if self.health <= 0:
            self.living = False

    def __repr__(self):
        # return self.__getattribute__('name') + ':' + str(self.__getattribute__('health')) + '\n'
        if self.living:
            return f"camp:{self.__getattribute__('camp')},{self.name.__str__()}:" \
                   f"HP:{self.health / self.or_health * 100}%," \
                   f"buff:{self.buff.__str__()}."
        else:
            return f"{self.name}已阵亡!"
