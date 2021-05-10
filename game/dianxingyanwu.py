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
import _Tools.getFighting
import pyautogui
class DianXing():
    def __init__(self):
        self.transform = TransForm()
        self.common = Common()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.mouse = Mouse()
        self.wujiang = 0

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
            endtime = time.time() + int(1500)
            while time.time() < endtime:
                time.sleep(0.5)
                self.screen.cut_screen()
                time.sleep(1)
                loc_begin = self.screen.get_location_picture("C:\\dh2\\game\\dianxing\\begin2.png",num=0.9)
                if loc_begin is not 0:
                    self.mouse.click_element(432, 516)
                    for j in range(5):
                        if j is 0:
                            self.mouse.click_element(309, 489, times=0.2, right=True)
                            self.mouse.click_element(309, 489, times=0.2)
                        else:
                            pyautogui.rightClick()
                            time.sleep(0.5)
                            pyautogui.click()
                        self.common.change_teamer(0.5)
                pos_zidong = self.screen.get_location_picture("C:\\dh2\\game\\dianxing\\1.png", num=0.99)
                pos_caozuo = self.screen.get_location_picture("C:\\dh2\\game\\dianxing\\2.png", num=0.99)
                if pos_zidong is not 0 and pos_caozuo is 0:
                    # 人物
                    flag = 0
                    while True:
                        # self.mouse.click_element(412, 137, times=1, right=True
                        if flag is 0:
                            self.mouse.click_element(309, 489, times=0.2, right=True)
                            self.common.find_attack(type='f7')
                            pyautogui.click()
                            self.keyboard.press_shortcut_key('alt', '8', times=0.3)
                            self.common.change_teamer(0.5)
                            for jj in range(4):
                                pyautogui.rightClick()
                                self.keyboard.press_key('f7')
                                time.sleep(0.3)
                                pyautogui.click()
                                pyautogui.click()
                                self.keyboard.press_shortcut_key('alt', '8', times=0.3)
                                self.common.change_teamer(0.5)
                            flag+=1
                        self.screen.cut_screen()
                        time.sleep(1)
                        loc_begin2 = self.screen.get_location_picture("C:\\dh2\\game\\dianxing\\begin.png")
                        time.sleep(0.5)
                        if loc_begin2 is not 0:
                            break

                elif pos_caozuo is not 0 and pos_zidong is 0:
                    flag = 0
                    while True:
                        # self.mouse.click_element(412, 137, times=1, right=True
                        if flag is 0:
                            if self.wujiang is 0:
                                self.mouse.click_direct_element(314, 179, right=True)
                                self.keyboard.press_shortcut_key('alt', 'w')
                                self.mouse.click_direct_element(270, 270, right=True)
                                result = self.common.find_attack(type='other')

                                pyautogui.click()
                                self.mouse.click_direct_element(775, 570)
                                self.common.change_teamer(0.5)
                                for ji in range(4):
                                    self.mouse.click_direct_element(314, 179, right=True)
                                    self.keyboard.press_shortcut_key('alt', 'w')
                                    self.mouse.click_direct_element(270, 270, right=True)
                                    self.mouse.click_direct_element(result[0], result[1])
                                    pyautogui.click()
                                    self.mouse.click_direct_element(775, 570)
                                    self.common.change_teamer(0.5)
                                self.wujiang = 1
                            else:
                                # self.mouse.click_element(314, 179, times=0.2, right=True)
                                # result = self.common.find_attack(type='other')
                                # self.mouse.click_element(result[0], result[1], times=0.2)
                                # pyautogui.click()
                                self.mouse.click_direct_element(775, 570)
                                self.common.change_teamer(0.3)
                                for jj in range(4):
                                    # self.mouse.click_element(314, 179, times=0.2, right=True)
                                    # self.keyboard.press_shortcut_key('alt', 's')
                                    # self.mouse.click_element(result[0], result[1], times=0.2)
                                    # pyautogui.click()
                                    self.mouse.click_direct_element(775, 570)
                                    self.common.change_teamer(0.3)
                            flag += 1
                        self.screen.cut_screen()
                        time.sleep(1)
                        loc_begin2 = self.screen.get_location_picture("C:\\dh2\\game\\dianxing\\begin.png")
                        time.sleep(0.5)
                        if loc_begin2 is not 0:
                            break

if __name__ == '__main__':
    # 匹配对手 436,520
    # 同意311,492
    DianXing().task_start()