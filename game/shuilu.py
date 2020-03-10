import time
from game.common import Common
from system.transform import TransForm
from system.keyboard import KeyBoard
from system.screen import Screen
from system.mouse import Mouse
import _Tools.getFighting
import pyautogui
class ShuiLu():
    def __init__(self):
        self.transform = TransForm()
        self.common = Common()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.mouse = Mouse()

    def task_start(self):
        self.screen.find_ele_picture('game\\system\\zidong')
        time.sleep(5)
        for i in range(5):
            self.keyboard.press_key('f7')
            if i is 0:
                self.mouse.click_element(198, 338, times=1)
            else:
                pyautogui.click()
            pyautogui.click()
            self.keyboard.press_shortcut_key('alt', '8')
            self.common.change_teamer(0.3)
if __name__ == '__main__':
    # 开始
    ShuiLu().task_start()