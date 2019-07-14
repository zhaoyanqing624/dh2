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
    def operate(self,type):
        if type is 'gong':
            self.mouse.click_element(289, 383)
        elif type is 'fa':
            self.keyboard.press_shortcut_key('alt', 'w')
            time.sleep(0.5)
            self.mouse.click_element(317, 178)
            time.sleep(0.5)
            self.mouse.click_element(289, 383)
    def task_start(self):
        print("任务开始")
        self.common.get_focus()
        for i in range(1):
            self.keyboard.press_shortcut_key('alt', 'o')
            self.mouse.click_element(248, 385)
            time.sleep(0.5)
            self.mouse.click_element(547, 420)
            time.sleep(0.5)
            self.screen.find_ele_picture('game\\system\\zidong')
            self.operate('fa')
            self.operate('fa')
            self.operate('gong')
            self.keyboard.press_shortcut_key('alt', '8')
            #317 178
            # 214 477
            # self.common.change_teamer()
            # time.sleep(1)
if __name__ == '__main__':
    BiDou().task_start()