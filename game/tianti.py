import time
from game.common import Common
from system.transform import TransForm
from system.keyboard import KeyBoard
from system.screen import Screen
from system.mouse import Mouse
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
            self.common.change_teamer()
        time.sleep(1)
        self.mouse.click_element(757, 553)
        time.sleep(1)
        self.mouse.click_element(161, 327)
        time.sleep(3)
        # 开始点击天梯
        self.mouse.click_element(770, 193)
        time.sleep(1)
        for i in range(10):
            if i is not 0:
                time.sleep(30)
            self.mouse.click_element(470, 444)
            for z in range(5):
                self.mouse.click_element(312, 490)
                time.sleep(1)
                self.common.change_teamer()
            endtime = time.time() + int(500)
            while time.time() < endtime:
                pos_caozuo = self.screen.get_location_picture("D:\\dh2\\game\\system\\caozuo.png")
                pos_zidong = self.screen.get_location_picture("D:\\dh2\\game\\system\\zidong.png")
                if pos_caozuo is not 0 and pos_zidong is not 0:
                    for j in range(5):
                        time.sleep(1)
                        self.keyboard.press_key('f7')
                        self.mouse.click_element(289, 383)
                        self.chong_operate(0)
                        self.keyboard.press_shortcut_key('alt', '8')
                        time.sleep(1)
                        self.common.change_teamer()

if __name__ == '__main__':
    # 匹配对手 436,520
    # 同意311,492

    TianTi().task_start()