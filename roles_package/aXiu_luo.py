import random

from fight import Fighting
from role import Role
from skills import RoleSkill


class AXiuLuo(Role):
    def __init__(self):
        super(AXiuLuo, self).__init__('阿修罗', 13500, 11000, 350, 159)
        self.critical_rate = 0.11
        self.critical_rate = 100
        self.critical_damage = 2.5

        self.skill_one = AXiuLuoOne()
        self.skills.append(self.skill_one)


class AXiuLuoOne(RoleSkill):
    def __init__(self):
        super(AXiuLuoOne, self).__init__("A", 1, 0, 1)

    @staticmethod
    def effect(role: Role, target: []):
        critical_damage = (role.critical_damage if random.random() <= role.critical_rate else 1)

        final_damage = critical_damage * role.attack * 1.25 * (
            role.buff["yu_hun_combine"]["four"] if role.buff["yu_hun_combine"]["four"] else 1)

        target = min(target, key=lambda x: x.__getattr__("health"))
        target.attcked_by_role(role, final_damage)