from concurrent.futures import ThreadPoolExecutor
import time
import datetime
import random

# defensive key value
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
        self.critical_rate: float = 10
        self.critical_damage: float = 1.5

    def attacked(self, damage_value):
        global defensive_
        self.health -= damage_value * (defensive_ / (defensive_ + self.defensive)) * (1 - 0.01 * random.random())
        if self.health < 0:
            self.living = False

    def __repr__(self):
        # return self.__getattribute__('name') + ':' + str(self.__getattribute__('health')) + '\n'
        return self.__dict__.__str__()


class Fighting:
    def __init__(self):
        self.start_time = datetime.datetime.now()
        self.rounds = 3
        self.enemy_roles: list = []
        self.roles: list = []
        self.state_code = True

    def fight_start(self):
        print('fight started')
        with ThreadPoolExecutor(max_workers=10) as pool:
            pool.submit(self.__end_the_turn)

    def role_add(self, roles: Role):
        self.enemy_roles.append(roles)
        self.enemy_roles.sort(key=lambda x: x.__getattribute__('speed'))

    def __act(self):
        the_length = max(x.__getattribute__('speed') for x in self.enemy_roles + self.roles)

        for x in self.enemy_roles + self.roles:
            x.location = x.__getattribute__('speed')

    def __end_the_turn(self):
        while True:

            # judge if this fight should to be end per 0.2 second
            time.sleep(0.2)
            # show the details of all role
            [print(x) for x in self.enemy_roles + self.roles]

            if not self.enemy_roles:
                time_cost: datetime.timedelta = datetime.datetime.now() - self.start_time
                print('win in %s second' % time_cost.seconds)
                self.state_code = False
                break
            elif not self.roles:
                print('failed !')
                self.state_code = False
                break
            elif self.enemy_roles and self.roles:
                continue


def main():
    round_fight = Fighting()
    snake = Role('snake', 199999, 5000, 2000, 135)
    gui_qie_one = Role('gui_qie', 28000, 3000, 700, 156)
    gui_qie_two = Role('gui_qie', 28000, 3000, 700, 156)
    round_fight.role_add(snake)
    round_fight.role_add(gui_qie_two)
    round_fight.role_add(gui_qie_one)
    round_fight.fight_start()


if __name__ == '__main__':
    main()
