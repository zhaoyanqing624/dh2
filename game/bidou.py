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
        if type is 0:
            self.keyboard.press_shortcut_key('alt', 'a')
        elif type is 1:
            self.keyboard.press_shortcut_key('alt', 'w')
            time.sleep(0.5)
            self.mouse.click_element(317, 178)
            time.sleep(0.5)
            self.mouse.click_element(289, 383)
    def task_start(self,team):
        print("任务开始")
        self.common.get_focus()
        for j in range(10):
            for index,i in enumerate(team):
                if j is 0:
                    time.sleep(1)
                    self.keyboard.press_shortcut_key('alt', 'o')
                    self.mouse.click_element(248, 385)
                else:
                    self.mouse.click_element(417,588,right=True)
                    time.sleep(3)
                    self.screen.find_ele_picture('game\\bidou\\begin')
                time.sleep(1)
                self.mouse.click_element(547, 420)
                time.sleep(1)
                self.screen.find_ele_picture('game\\system\\zidong',location_=[547, 420])
                if j is 0:
                    self.operate(i[0])
                    self.operate(i[1])
                    self.operate(i[2])
                self.keyboard.press_shortcut_key('alt', '8')
                time.sleep(1)
                self.common.change_teamer()
            # time.sleep(1)
if __name__ == '__main__':
    # 0攻击 1法术
    list = [[1,1,1],[1,1,0],[1,1,1],[1,1,0],[1,1,0]]
    BiDou().task_start(list)