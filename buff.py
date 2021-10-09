from fight import Fighting
from role import Role
from skills import RoleSkill


class Buff:
    def __init__(self, role: Role, name, round_last):
        self.name = name
        self.round_last = round_last

    def buff_effect(self):
        pass

    def buff_calculate(self):
        self.round_last -= 1
        if self.round_last == 0:
            del self

    def __repr__(self):
        return f"{self.name}:{self.round_last}回合"
