from fight import Fighting
from role import Role
import roles_package

if __name__ == '__main__':
    round_fight = Fighting()
    snake = Role('大蛇', 199999, 5000, 2000, 135)
    gui_qie_one = Role('鬼切', 28000, 3000, 700, 156)
    gui_qie_two = Role('鬼切', 28000, 3000, 700, 156)
    aXiu_luo = roles_package.aXiu_luo.AXiuLuo()
    qing_ming = Role('晴明', 15000, 6000, 1300, 128)
    round_fight.role_add(snake)
    round_fight.role_add(gui_qie_two)
    round_fight.role_add(gui_qie_one)
    round_fight.role_add(aXiu_luo, role_type=0)
    round_fight.role_add(qing_ming, role_type=0)
    round_fight.fight_start()
