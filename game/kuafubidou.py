import time
from game.common import Common
from system.transform import TransForm
from system.keyboard import KeyBoard
from system.screen import Screen
from system.mouse import Mouse

import pymysql
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
    def task_start(self,team,computer):
        print("任务开始")
        self.common.get_focus(computer)
        for i in range(5):
            self.mouse.click_element(772, 194, times=0.5)
            self.common.change_teamer(0.5)
        if computer is True:
            for j in range(15):
                for index,z in enumerate(team):
                    if index is 0 or index is 2 or index is 4:
                        self.mouse.click_element(477, 511, times=0.5)
                        self.screen.find_ele_picture('game\\bidou\\begin2')
                        self.mouse.click_element(488, 488, times=0.5)
                    self.mouse.click_element(309, 489, times=0.5)
                    self.common.change_teamer(0.5)
                for z in range(5):
                    if z is 0 or z is 2 or z is 4:
                        self.screen.find_ele_picture('game\\system\\zidong')
                        if z is 4:
                            self.update("1")
                    self.keyboard.press_shortcut_key('alt', 'a')
                    self.keyboard.press_shortcut_key('alt', 'a')
                    self.keyboard.press_shortcut_key('alt', '8')
                    self.common.change_teamer(0.5)
        else:
            for j in range(15):
                for index,z in enumerate(team):
                    if index is 0:
                        self.screen.find_ele_picture('game\\bidou\\tongyi')
                        self.mouse.click_element(309, 489, times=0.5)
                    elif index is 1:
                        self.screen.find_ele_picture('game\\bidou\\begin2')
                        self.mouse.click_element(488, 488, times=0.5)
                        self.mouse.click_element(309, 489, times=0.5)
                    elif index is 3:
                        self.screen.find_ele_picture('game\\bidou\\begin2')
                        self.mouse.click_element(488, 488, times=0.5)
                        self.mouse.click_element(309, 489, times=0.5)
                    else:
                        self.mouse.click_element(309, 489, times=0.5)
                    self.common.change_teamer(0.5)
                for z in range(5):
                    if z is 1 or z is 3 or z is 0:
                        self.screen.find_ele_picture('game\\system\\zidong')
                    self.keyboard.press_shortcut_key('alt', 'a')
                    self.keyboard.press_shortcut_key('alt', 'a')
                    self.keyboard.press_shortcut_key('alt', '8')
                    self.common.change_teamer(0.5)



if __name__ == '__main__':
#     # 0攻击 1法术
    list = [[0,0],[0,0],[0,0],[0,0],[0,0]]
    KuaFuBiDou().task_start(list,True)
