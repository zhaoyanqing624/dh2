import time
from game.common import Common
from system.transform import TransForm
from system.keyboard import KeyBoard
from system.screen import Screen
from system.mouse import Mouse
import _Tools.getFighting
class DianXing():
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
            self.mouse.click_element(317, 178)
            time.sleep(0.5)
            self.mouse.click_element(289, 383)
    def task_start(self):
        print("任务开始")
        self.common.get_focus()
        time.sleep(1)
        self.mouse.click_element(768, 195)
        time.sleep(1)
        for i in range(8):
            pass

if __name__ == '__main__':
    # 匹配对手 436,520
    # 同意311,492

    DianXing().task_start()