import sys
import os
current_dir = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(current_dir)[0]
sys.path.append(rootPath)
import time
from game.common import Common
from system.transform import TransForm
from system.keyboard import KeyBoard
from system.screen import Screen
from system.mouse import Mouse
import _Tools.getFighting
class BiDou():
    def __init__(self):
        self.transform = TransForm()
        self.common = Common()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.mouse = Mouse()

    def operate(self,cicle,type):
        result = []
        if type[0] is 0:
            self.keyboard.press_shortcut_key('alt', 'a')
        else:
            self.keyboard.press_shortcut_key('alt', 'w')
            self.mouse.click_element(317, 178, times=0.5, right=True)
            result = self.common.find_attack(type='s', str='zidong', x_pos=300, y_pos=420)

        for i in range(1, 3):
            if type[i] is 0:
                self.keyboard.press_shortcut_key('alt', 'a')
            else:
                if cicle is 0:
                    self.keyboard.press_shortcut_key('alt', 'w')
                    self.mouse.click_direct_element(317, 178)
                self.mouse.click_direct_element(result[0], result[1])

        # if type is 0:
        #     self.keyboard.press_shortcut_key('alt', 'a')
        # elif type is 1:
        #     self.keyboard.press_shortcut_key('alt', 'w')
        #     self.mouse.click_element(317, 178,times=0.5)
        #     self.mouse.click_element(289, 383,times=0.5)
    def task_start(self,team):
        print("任务开始")
        self.common.get_focus()
        for j in range(10):
            for index,i in enumerate(team):
                if j is 0:
                    time.sleep(1)
                    self.keyboard.press_shortcut_key('alt', 'o')
                    self.mouse.click_element(248, 385)
                    time.sleep(1)
                    self.mouse.click_element(578, 420)
                    self.keyboard.press_shortcut_key('alt', 'o')
                else:
                    # self.mouse.click_element(417,588,right=True)
                    time.sleep(2)
                    self.screen.find_ele_picture('game\\bidou\\begin','mouse', 541, 420)
                self.screen.find_ele_picture('game\\system\\zidong','mouse', 397, 531)
                if j is 0:
                    self.operate(j,i)
                self.keyboard.press_shortcut_key('alt', '8')
                time.sleep(1)
                self.common.change_teamer(times=0.5)
            # time.sleep(1)
if __name__ == '__main__':
    # 0攻击 1法术
    list = [[1,1,0],[1,1,0],[1,1,0],[1,1,0],[1,1,0]]

    BiDou().task_start(list)