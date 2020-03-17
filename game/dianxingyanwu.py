import time
from game.common import Common
from system.transform import TransForm
from system.keyboard import KeyBoard
from system.screen import Screen
from system.mouse import Mouse
import _Tools.getFighting
import pyautogui
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
        jiangxing = 0
        print("任务开始")
        self.common.get_focus()
        time.sleep(1)
        self.mouse.click_element(768, 195)
        time.sleep(1)
        for i in range(8):
            # for x in range(5):
            #     self.mouse.click_element(421, 208, times=1, right=True)
            #     self.common.change_teamer(0.5)
            endtime = time.time() + int(500)
            while time.time() < endtime:
                self.screen.cut_screen()
                time.sleep(2)
                loc_begin = self.screen.get_location_picture("D:\\dh2\\game\\dianxing\\begin2.png",num=0.9)
                if loc_begin is not 0:
                    self.mouse.click_element(432, 516)
                    for j in range(5):
                        self.mouse.click_element(309, 489, times=0.2, right=True)
                        self.mouse.click_element(309, 489, times=0.2)
                        self.common.change_teamer(0.2)
                pos_zidong = self.screen.get_location_picture("D:\\dh2\\game\\dianxing\\1.png",num=0.99)
                pos_caozuo = self.screen.get_location_picture("D:\\dh2\\game\\dianxing\\2.png",num=0.99)
                if pos_zidong is not 0 and pos_caozuo is 0:
                    # 人物
                    flag = 0
                    while True:
                        # self.mouse.click_element(412, 137, times=1, right=True
                        if flag is 0:
                            result = self.common.find_attack(type='f7')
                            self.mouse.click_element(result[0], result[1], times=0.5)
                            self.keyboard.press_shortcut_key('alt', '8')
                            self.common.change_teamer(0.3)
                            for jj in range(4):
                                self.keyboard.press_key('f7')
                                time.sleep(0.3)
                                pyautogui.click()
                                time.sleep(0.3)
                                pyautogui.click()
                                time.sleep(0.3)
                                self.keyboard.press_shortcut_key('alt', '8')
                                self.common.change_teamer(0.3)
                            flag+=1
                        self.screen.cut_screen()
                        time.sleep(1)
                        loc_begin2 = self.screen.get_location_picture("D:\\dh2\\game\\dianxing\\begin.png")
                        time.sleep(0.5)
                        if loc_begin2 is not 0:
                            break

                if pos_caozuo is not 0 and pos_zidong is 0:
                    # 星将
                    while True:
                        # self.mouse.click_element(412, 137, times=1, right=True)
                        self.screen.cut_screen()
                        time.sleep(1)
                        pos_caozuo2= self.screen.get_location_picture("D:\\dh2\\game\\dianxing\\2.png")
                        if pos_caozuo2 is not 0:
                            if jiangxing is 0:
                                for z in range(5):
                                    self.keyboard.press_shortcut_key('alt', 'a')
                                    self.keyboard.press_shortcut_key('alt', 'w')
                                    self.mouse.click_element(314, 179, times=0.2, right=True)
                                    self.keyboard.press_shortcut_key('alt', 's')
                                    if z is 0:
                                        result = self.common.find_attack(type='other',str='caozuo2')
                                        self.mouse.click_element(result[0], result[1], times=0.2)
                                    else:
                                        self.mouse.click_element(result[0], result[1], times=0.2)
                                    self.common.change_teamer(0.3)
                                    jiangxing+=1
                            else:
                                for z in range(5):
                                    self.keyboard.press_shortcut_key('alt', 'a')
                                    self.keyboard.press_shortcut_key('alt', 's')
                                    if z is 0:
                                        result = self.common.find_attack(type='other',str='caozuo2')
                                        self.mouse.click_element(result[0], result[1], times=0.2)
                                    else:
                                        pyautogui.click()
                                    self.common.change_teamer(0.3)
                        if loc_begin2 is not 0:
                            break

if __name__ == '__main__':
    # 匹配对手 436,520
    # 同意311,492
    DianXing().task_start()