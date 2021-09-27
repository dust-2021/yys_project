import random

from fight import Fighting
from role import Role
from skills import RoleSkill


class AXiuLuo(Role):
    def __init__(self):
        super(AXiuLuo, self).__init__('阿修罗', 13500, 4014, 350, 119)
        self.critical_rate = 0.11


class AXiuLuoOne(RoleSkill):
    def __init__(self):
        super(AXiuLuoOne, self).__init__("A", 1, 0, 1)

    def skill_one_effect(self, role: Role):
        critical_damage = (role.critical_damage if random.random() <= role.critical_rate else 1)
        final_damage = critical_damage * role.attack * 1.25 * (
            role.buff["yu_hun_combine"]["four"] if role.buff["yu_hun_combine"]["four"] else 1)
        for tar in self.target_get():
            tar.attacked_by_role(final_damage)
