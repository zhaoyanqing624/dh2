import sys
import os
current_dir = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(current_dir)[0]
sys.path.append(rootPath)
import time
from system.transform import TransForm
from game.common import Common
from system.keyboard import KeyBoard
from system.screen import Screen
from system.mouse import Mouse
import pyautogui
class XiuLuo():

    def __init__(self):
        self.transform = TransForm()
        self.common = Common()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.mouse = Mouse()
        self.total_num = 0

    def go_wuyi(self):
        self.common.get_focus()
        for i in range(5):
            if i is 0:
                self.keyboard.press_shortcut_key('alt', '1')
                time.sleep(0.5)
            if i is 0:
                self.mouse.click_element(390, 353)
            self.screen.find_ele_picture('game\\system\\wuyi', 'mouse', 188, 344)
            if i is 0:
                self.keyboard.press_shortcut_key('alt', '1')
            self.common.change_teamer()

    def is_xiuluoKing(self):
        Screen().cut_screen_by_PIL(20, 265, 50, 350, "C:\\dh2\\system\\1.PNG")
        result = Screen().find_color_ele(10, 10, 8, 8, 255, 255, 0, 0, 0, 0, True)
        if result is not None:
            return True
        else:
            return False

    def is_bingKu(self, level):
        time.sleep(1)
        self.screen.cut_screen()
        time.sleep(1)
        location = self.screen.get_location_picture('C:\\dh2\\game\\xiuluo\\4.png', 0.8)
        if location is not 0:
            if level is None:
                self.mouse.click_element(44, 254, times=0.5)
                self.screen.find_ele_picture('game\\xiuluo\\3', 'mouse', 175, 328)
                time.sleep(1)
                self.mouse.click_element(49, 241, times=0.5)
            else:
                self.mouse.click_element(125, 241, times=0.5)
                time.sleep(5)
                for z in range(5):
                    if z is 0:
                        self.mouse.click_element(312, 490)
                    else:
                        pyautogui.click()
                    self.common.change_teamer(0.5)
                self.screen.find_ele_picture('game\\xiuluo\\4', 'mouse', 82, 241)
                time.sleep(5)
            return True
        self.mouse.click_element(49, 241, times=0.5)
        return False

    def cancle_task(self):
        # self.keyboard.press_shortcut_key('alt', '1')
        self.mouse.click_element(355, 312, times=0.5)
        self.mouse.click_element(345, 312, times=0.5)
        self.keyboard.press_shortcut_key('alt', '1')
        self.screen.find_ele_picture('game\\xiuluo\\1', 'mouse', 195, 396)
        time.sleep(2)
        self.mouse.click_element(162, 329, times=0.5)
        time.sleep(2)
        self.mouse.click_element(162, 329, times=0.5)

    def task_start(self, level=None):
        print("任务开始")
        for i in range(80):
            if self.total_num >=40:
                break
            print("第"+str(i)+"次")
            if i % 10 is 0:
                self.go_wuyi()
            if i is 0:
                self.common.get_focus()
                self.keyboard.press_shortcut_key('alt', '1')
                self.mouse.click_element(355, 312, times=0.5)
                self.mouse.click_element(345, 312, times=0.5)
                self.keyboard.press_shortcut_key('alt', '1')
                self.screen.find_ele_picture('game\\xiuluo\\1', 'mouse', 189, 364)
                self.task(i, level)
            else:
                if self.is_bingKu(level) is False:
                    self.task(i, level)

        # 返回长安
        self.keyboard.press_shortcut_key('alt', '2')
        self.mouse.click_element(505, 420, times=0.5)
        self.mouse.click_element(432, 506, times=0.5)
        time.sleep(180)

    def task(self, i, level):
        time.sleep(5)
        if level is None:
            # 是否修罗王
            xiuluowang = self.is_xiuluoKing()
            if xiuluowang is True:
                self.cancle_task()
            else:
                self.mouse.click_element(29, 257, times=0.5)
                time.sleep(2)
                self.mouse.click_element(45, 257, times=0.5)
                self.common.capation_eat_xiang()
                time.sleep(30)
                self.screen.find_ele_picture('system\\zidong', 'keyboard', 'alt', '8')
                if (i % 2) == 0:
                    for j in range(5):
                        self.common.change_teamer(0.5)
                        self.keyboard.press_shortcut_key('alt', '8')
                self.total_num+=1
        else:
            self.mouse.click_element(29, 257, times=0.5)
            time.sleep(2)
            self.mouse.click_element(45, 257, times=0.5)
            self.common.capation_eat_xiang()
            time.sleep(30)
            self.screen.find_ele_picture('system\\zidong', 'keyboard', 'alt', '8')
            if (i % 2) == 0:
                for j in range(5):
                    self.common.change_teamer(0.5)
                    self.keyboard.press_shortcut_key('alt', '8')
            self.total_num += 1
        # 结束后回家
        if self.total_num is 40:
            endtime = time.time() + int(3000)
            while time.time() < endtime:
                self.screen.cut_screen()
                time.sleep(1)
                location = self.screen.get_location_picture('C:\\dh2\\game\\system\\zidong.png', 0.8)
                if location is 0:
                    self.mouse.click_element(736, 566)
                    break
        else:
            endtime = time.time() + int(3000)
            while time.time() < endtime:
                self.screen.cut_screen()
                time.sleep(1)
                location = self.screen.get_location_picture('C:\\dh2\\game\\xiuluo\\2.png', 0.8)
                if location is not 0:
                    self.mouse.click_element(location[0], location[1])
                    break
            time.sleep(5)

if __name__ == '__main__':
    XiuLuo().task_start(True)
