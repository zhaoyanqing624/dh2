import time
from game.common import Common
from system.transform import TransForm
from system.keyboard import KeyBoard
from system.screen import Screen
from system.mouse import Mouse
import _Tools.getFighting
import pyautogui
class DiGong():
    def __init__(self):
        self.transform = TransForm()
        self.common = Common()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.mouse = Mouse()

    def task_start(self,type):
        # 0简单 1困难 2卓越
        self.common.get_focus()
        self.keyboard.press_shortcut_key('alt', '2', times=0.5)
        self.mouse.click_element(540, 388, times=1)
        self.mouse.click_element(616, 463, times=1)


if __name__ == '__main__':
    # 开始
    DiGong().task_start()