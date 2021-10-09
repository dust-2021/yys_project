from role import Role
from fight import Fighting


class RoleSkill:
    def __init__(self, name, target_type, fire_cost, target_count):
        self.name = name
        self.target_type = target_type
        self.fire_cost = fire_cost
        self.target_count = target_count

        self.auto_skill = False

    def target_get(self, self_role: Role, all_target=None, auto: bool = False):
        if auto:
            pass
        else:
            if self.target_type == 0 and self_role.__getattribute__('camp') == 'left':
                return all_target[0]
            elif self.target_type == 0 and self_role.__getattribute__('camp') == 'right':
                return all_target[1]
            elif self.target_type == 1 and self_role.__getattribute__('camp') == 'left':
                return all_target[1]
            elif self.target_type == 1 and self_role.__getattribute__('camp') == 'right':
                return all_target[0]
            else:
                pass

    def skill_effect(self):
        pass

    def __repr__(self):
        return f"{self.name}:{self.fire_cost}"
