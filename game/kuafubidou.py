import time
from game.common import Common
from system.transform import TransForm
from system.keyboard import KeyBoard
from system.screen import Screen
from system.mouse import Mouse


class KuaFuBiDou():
    def __init__(self):
        self.transform = TransForm()
        self.common = Common()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.mouse = Mouse()
    def operate(self,type):
        if type is 0:
            self.keyboard.press_shortcut_key('alt', 'a')
        elif type is 1:
            self.keyboard.press_shortcut_key('alt', 'w')
            time.sleep(0.5)
            self.mouse.click_element(317, 178,times=0.5)
            time.sleep(0.5)
            self.mouse.click_element(289, 383,times=0.5)
    def task_start(self,team):
        print("任务开始")
        self.common.get_focus()
        for i in range(6):
            self.mouse.click_element(772, 194, times=0.5)
            self.common.change_teamer(0.5)

        for j in range(15):
            for index,z in enumerate(team):
                if index is 0 or index is 2 or index is 4:
                    self.mouse.click_element(377, 477, times=0.5)
                    self.screen.find_ele_picture('game\\bidou\\begin2')
                    self.mouse.click_element(488, 504, times=0.5)
                self.mouse.click_element(309, 489, times=0.5)
                self.common.change_teamer(0.5)
            for z in range(6):
                if z is 0 or z is 2 or z is 4:
                    result_ = self.screen.find_ele_picture_time('game\\system\\zidong')
                    if result_ is True:
                        self.keyboard.press_shortcut_key('alt', 'a')
                        self.keyboard.press_shortcut_key('alt', 'a')
                        self.keyboard.press_shortcut_key('alt', '8')
                        self.common.change_teamer(0.5)
                        self.keyboard.press_shortcut_key('alt', 'a')
                        self.keyboard.press_shortcut_key('alt', 'a')
                        self.keyboard.press_shortcut_key('alt', '8')
                        self.common.change_teamer(0.5)
                    else:
                        self.common.change_teamer(0.5)
                        self.common.change_teamer(0.5)
            time.sleep(10)




if __name__ == '__main__':
#     # 0攻击 1法术
    list = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    KuaFuBiDou().task_start(list,True)
