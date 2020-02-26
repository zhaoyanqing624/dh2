import time
from game.common import Common
from system.transform import TransForm
from system.keyboard import KeyBoard
from system.screen import Screen
from system.mouse import Mouse
import pyautogui
import _Tools.getFighting
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
        for i in range(5):
            self.common.change_dog(2)
            time.sleep(1)
            self.common.change_teamer(times=0.3)
        time.sleep(1)
        self.mouse.click_element(757, 553)
        time.sleep(1)
        self.mouse.click_element(161, 327)
        time.sleep(3)
        # 开始点击天梯
        self.mouse.click_element(770, 193)
        time.sleep(1)
        for i in range(10):
            for z in range(5):
                self.mouse.click_element(413, 142,right=True)
                time.sleep(1)
                self.common.change_teamer(times=0.3)
            if i is not 0:
                time.sleep(3)
            self.screen.find_ele_picture('game\\tianti\\begin')
            self.mouse.click_element(470, 444)
            for z in range(5):
                if z is 0:
                    self.mouse.click_element(312, 490)
                else:
                    pyautogui.click()
                time.sleep(1)
                self.common.change_teamer(times=0.3)
            # flag = 0
            self.screen.find_ele_picture('system\\zidong')
            self.common.find_attack('f7')
            pyautogui.click()
            self.keyboard.press_shortcut_key('alt', '8',times=0.3)
            self.common.change_teamer(times=0.3)
            for i in range(4):
                self.keyboard.press_key('f7')
                pyautogui.click()
                pyautogui.click()
                self.keyboard.press_shortcut_key('alt', '8',times=0.3)
                self.common.change_teamer(times=0.3)
            self.common.get_focus()

if __name__ == '__main__':
    # 匹配对手 436,520
    # 同意311,492

    TianTi().task_start()