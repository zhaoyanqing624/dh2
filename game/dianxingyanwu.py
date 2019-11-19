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
            endtime = time.time() + int(500)
            while time.time() < endtime:
                time.sleep(1)
                self.mouse.click_element(432, 516)
                for j in range(5):
                    self.mouse.click_element(309, 489, times=0.5)
                    self.common.change_teamer(0.5)
                time.sleep(1)
                self.screen.cut_screen()
                loc_begin = self.screen.get_location_picture("D:\\dh2\\game\\dianxing\\begin.png")
                pos_caozuo = self.screen.get_location_picture("D:\\dh2\\game\\system\\caozuo.png")
                pos_zidong = self.screen.get_location_picture("D:\\dh2\\game\\system\\zidong.png")
                if pos_caozuo is not 0 and pos_zidong is not 0 and loc_begin is 0:
                    # 人物
                    time.sleep(0.5)
                    for z in range(5):
                        self.keyboard.press_key('f7')
                        self.mouse.click_element(198, 338, times=0.5)
                        if z is 2:
                            self.keyboard.press_shortcut_key('alt', 's')
                            self.mouse.click_element(198, 338, times=0.5)
                        else:
                            self.keyboard.press_shortcut_key('alt', 'd')
                    self.keyboard.press_shortcut_key('alt', '8')

                if pos_caozuo is not 0 and pos_zidong is not 0 and loc_begin is 0:
                    # 星将
                    while True:
                        time.sleep(1)
                        self.screen.cut_screen()
                        pos_caozuo2= self.screen.get_location_picture("D:\\dh2\\game\\system\\caozuo.png")
                        loc_begin2 = self.screen.get_location_picture("D:\\dh2\\game\\dianxing\\begin.png")
                        if pos_caozuo2 is not 0:
                            for z in range(5):
                                self.keyboard.press_shortcut_key('alt', 'a')
                                self.keyboard.press_shortcut_key('alt', 'w')
                                self.mouse.click_element(314, 179, times=0.5)
                                self.mouse.click_element(198, 338, times=0.5)
                                self.common.change_teamer(0.5)
                        if loc_begin2 is not 0:
                            break

if __name__ == '__main__':
    # 匹配对手 436,520
    # 同意311,492

    DianXing().task_start()