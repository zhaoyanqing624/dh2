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

class TianTi():
    def __init__(self):
        self.transform = TransForm()
        self.common = Common()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.mouse = Mouse()
    def chong_operate(self,type):
        if type is 0:
            self.keyboard.press_shortcut_key('alt', 'a')
        elif type is 1:
            self.keyboard.press_shortcut_key('alt', 'w')
            time.sleep(0.5)
            self.mouse.click_element(317, 178)
            time.sleep(0.5)
            self.mouse.click_element(289, 383)

    def task_start(self):
        print("任务开始")
        self.common.get_focus()
        time.sleep(1)
        # 切换宝宝
        # for i in range(5):
        #     self.common.change_dog(2)
        #     time.sleep(1)
        #     self.common.change_teamer(times=0.3)
        # 组队
        # self.keyboard.press_shortcut_key('alt', '5')
        # self.keyboard.press_shortcut_key('alt', 't')
        # self.mouse.click_element(415, 306, times=0.5)
        # self.keyboard.press_shortcut_key('alt', 'f')
        # self.mouse.click_element(701, 312, times=0.5)
        # self.mouse.click_element(715, 338, times=0.5, right=True)
        # self.screen.find_ele_picture('game\\bidou\\2', 'mouse', 387, 504)
        # self.mouse.click_element(414, 531, times=0.5, right=True)
        #
        # self.mouse.click_element(701, 290, times=0.5)
        # for i in range(3):
        #     self.mouse.click_element(715, 320+25*i, times=0.5, right=True)
        #     self.screen.find_ele_picture('game\\bidou\\2', 'mouse', 387, 504)
        #     self.mouse.click_element(414, 531, times=0.5, right=True)
        # self.keyboard.press_shortcut_key('alt', 'f')
        #
        # for i in range(5):
        #     self.mouse.click_element(347, 415, times=0.5)
        #     time.sleep(1)
        #     self.common.change_teamer(times=0.3)

        time.sleep(1)
        self.mouse.click_element(757, 566)
        time.sleep(1)
        self.mouse.click_element(161, 327)
        time.sleep(3)
        # 开始点击天梯
        self.mouse.click_element(770, 193)
        time.sleep(1)
        for i in range(10):
            time.sleep(5)
            self.screen.find_ele_picture('game\\tianti\\begin')
            for z in range(5):
                self.mouse.click_element(422, 144, right=True)
                self.common.change_teamer(times=0.5)
            if i is not 0:
                time.sleep(3)
            self.mouse.click_element(470, 444)
            for z in range(5):
                if z is 0:
                    self.mouse.click_element(312, 490)
                else:
                    pyautogui.click()
                self.common.change_teamer(times=0.5)
            # flag = 0
            self.screen.find_ele_picture('system\\zidong')
            self.common.find_attack('f7')
            pyautogui.click()
            self.keyboard.press_shortcut_key('alt', '8', times=0.3)
            self.common.change_teamer(times=0.5)
            for j in range(4):
                self.keyboard.press_key('f7')
                pyautogui.click()
                pyautogui.rightClick()
                pyautogui.click()
                self.keyboard.press_shortcut_key('alt', '8', times=0.3)
                self.common.change_teamer(times=0.5)
            self.common.get_focus()
            time.sleep(20)

if __name__ == '__main__':
    # 匹配对手 436,520
    # 同意311,492
    TianTi().task_start()