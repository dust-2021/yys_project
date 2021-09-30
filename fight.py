import threading
from concurrent.futures import ThreadPoolExecutor
import time
import datetime
from role import Role
import _thread


def fire_yield():
    num = 3
    while True:
        yield num if num <= 5 else 5


class Fighting:
    def __init__(self):
        self.start_time = datetime.datetime.now()
        self.round_num = 0
        self.right_roles: list = []
        self.left_roles: list = []
        self.state_code = True

        self.left_fire_count = 4
        self.left_fire_act = 0
        self.right_fire_count = 4
        self.right_fire_act = 0
        self.left_fire_yield = fire_yield()
        self.right_fire_yield = fire_yield()
        self.auto_ = False

    def fight_start(self):
        """
        the fight start
        :return: None
        """
        print('fight started')
        with ThreadPoolExecutor(max_workers=10) as pool:
            pool.submit(self.__act)

    def role_add(self, roles: Role, role_type: int = 1):
        """
        add role into the fight before start
        :param roles:
        :param role_type:
        :return:
        """
        if role_type:
            self.left_roles.append(roles)
            roles.camp = 'left'
        else:
            self.right_roles.append(roles)
            roles.camp = 'right'

    def __act(self):
        """
        calculate which role is going to act
        :return: None
        """
        self.the_length = max(x.__getattribute__('speed') for x in self.right_roles + self.left_roles)
        for x in self.right_roles + self.left_roles:
            x.location = x.__getattribute__('speed')

        while self.state_code:
            if max([x.__getattribute__('location') for x in self.right_roles + self.left_roles]) >= self.the_length:
                self.__the_act(
                    max([x for x in self.right_roles + self.left_roles], key=lambda x: x.__getattribute__('location')))
            else:
                min_time_cost = min(
                    [(self.the_length - x.__getattribute__('location')) / x.__getattribute__('speed') for x in
                     self.right_roles + self.left_roles])
                for x in self.right_roles + self.left_roles:
                    x.location += x.speed * min_time_cost
                del min_time_cost

    def __the_act(self, role: Role):
        """
        the real act for a role
        :param role: the act role
        :return: None
        """
        print(self)
        camps = role.__getattribute__('camp')
        if camps == 'left':
            self.left_fire_act += 1
        else:
            self.right_fire_act += 1

        if self.left_fire_act == 5:
            self.left_fire_count += (next(self.left_fire_yield) if self.left_fire_count + next(
                self.left_fire_yield) <= 8 else 8 - self.left_fire_count)
            self.left_fire_act = 0
        elif self.right_fire_act == 5:
            self.right_fire_count += (next(self.right_fire_yield) if self.right_fire_count + next(
                self.right_fire_yield) <= 8 else 8 - self.right_fire_count)
            self.right_fire_act = 0
        else:
            pass

        print(
            f'阵营：{role.__getattribute__("camp")}\n'
            f'鬼火：{self.__getattribute__(f"{camps}_fire_count")}\n'
            f'鬼火条：{self.__getattribute__(f"{camps}_fire_act")}\n'
            f'{role.name}行动\n'
            f'行动条{[f"{x.name}:{round(x.location / self.the_length * 100, 1)}%" for x in self.right_roles + self.left_roles]}')

        role.skill_select([self.left_roles, self.right_roles])
        print('err')

        # calculate if the fight should to be done
        if not self.right_roles:
            time_cost: datetime.timedelta = datetime.datetime.now() - self.start_time
            print('win in %s second' % time_cost.seconds)
            self.state_code = False
        elif not self.left_roles:
            print('failed !')
            self.state_code = False
        elif self.right_roles and self.left_roles:
            pass

        role.location = 0

    def __repr__(self):
        str_s = ""
        for x in self.right_roles + self.left_roles:
            str_s += x.__repr__() + '\n'
        return str_s
