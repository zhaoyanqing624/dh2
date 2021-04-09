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
import pyautogui

class HuaShan():

    def __init__(self):
        self.transform = TransForm()
        self.common = Common()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.mouse = Mouse()
        self.list_task = [0, 0, 0, 0, 0]

    def task_start(self, operate=None):
        print("任务开始")
        self.common.get_focus()
        # for i in range(5):
        #     self.screen.find_ele_picture(file_path='game\\huashan\\0', handle='self')
        #     self.mouse.click_element(160, 330)
        #     time.sleep(2)
        #     self.mouse.click_element(738, 205)
        #     self.common.change_teamer()

        for i in range(8):
            print("------第"+str(i+1)+"轮------")
            for j in range(5):
                self.screen.find_ele_picture(file_path='game\\huashan\\1', handle='self')
                time.sleep(5)
                self.screen.find_ele_picture('game\\system\\caozuo')
                result = self.common.find_attack('f6')
                for z in range(3):
                    if operate[z] is 0:
                        pyautogui.click()
                    else:
                        if i is 0:
                            self.keyboard.press_shortcut_key('alt', 'w')
                            self.mouse.click_element(317, 178, times=0.5, right=True)
                        self.keyboard.press_shortcut_key('alt', 's')
                        self.mouse.click_direct_element(result[0], result[1])
                self.keyboard.press_shortcut_key('alt', '8')
                self.common.change_teamer(times=0.5)

if __name__ == '__main__':
    # 0攻击 1法术
    HuaShan().task_start(operate=[0, 0, 0])