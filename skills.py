from role import Role
from fight import Fighting


class RoleSkill:
    def __init__(self, name, target_type, fire_cost, target_count):
        self.name = name
        self.target_type = target_type
        self.fire_cost = fire_cost
        self.target_count = target_count

    def target_get(self, self_role: Role, fight: Fighting, auto: bool):
        if auto:
            pass
        else:
            if self.target_type == 0 and self_role.__getattribute__('camp') == 'left':
                targets: int = int(input(f'选择目标:{fight.left_roles}'))
                return fight.left_roles[targets - 1]
            elif self.target_type == 0 and self_role.__getattribute__('camp') == 'right':
                targets: int = int(input(f'选择目标:{fight.right_roles}'))
                return fight.right_roles[targets - 1]
            elif self.target_type == 1 and self_role.__getattribute__('camp') == 'left':
                targets: int = int(input(f'选择目标:{fight.right_roles}'))
                return fight.right_roles[targets - 1]
            elif self.target_type == 1 and self_role.__getattribute__('camp') == 'right':
                targets: int = int(input(f'选择目标:{fight.left_roles}'))
                return fight.left_roles[targets - 1]
            else:
                pass

    def skill_effect(self):
        pass
