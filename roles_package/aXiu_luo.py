import random
from functools import reduce
from fight import Fighting
from role import Role
from skills import RoleSkill
from buff import Buff


class AXiuLuo(Role):
    def __init__(self):
        super(AXiuLuo, self).__init__('阿修罗', 13500, 11000, 350, 159)
        self.critical_rate = 0.11
        self.critical_rate = 50
        self.critical_damage = 2.5

        self.skill_one = AXiuLuoOne()
        self.skills.append(self.skill_one)


class AXiuLuoOne(RoleSkill):
    def __init__(self):
        super(AXiuLuoOne, self).__init__("A", 1, 0, 1)

    @staticmethod
    def effect(role: Role, target: []):
        role.out_damage_effect[0] = (role.critical_damage if random.random() < role.critical_rate/100 else 1)
        final_damage = role.attack * reduce(lambda x, y: x * y, role.out_damage_effect)
        print(f"{'暴击！' if role.out_damage_effect[0] != 1 else ''}")
        target = min(target, key=(lambda x: x.__getattribute__("health")))
        target.attacked_by_role(role, final_damage)


class TianMoWeiYa(Buff):
    def __init__(self):
        super(TianMoWeiYa, self).__init__()


class AXiuLuoTwo(RoleSkill):
    def __init__(self):
        super(AXiuLuoTwo, self).__init__("天魔威压", 0, 0, 0)
        self.auto_skill = True
