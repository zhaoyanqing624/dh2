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
import pyautogui

class KuaFuBiDou():
    def __init__(self):
        self.transform = TransForm()
        self.common = Common()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.mouse = Mouse()
        self.bidou_list = [0, 0, 0]

    def operate(self, type):
        if type is 0:
            self.keyboard.press_shortcut_key('alt', 'a')
        elif type is 1:
            self.keyboard.press_shortcut_key('alt', 'w')
            time.sleep(0.5)
            self.mouse.click_element(317, 178,times=0.5)
            time.sleep(0.5)
            self.mouse.click_element(289, 383,times=0.5)

    def task_start(self, team):
        print("任务开始")
        self.common.get_focus()
        # 去竞技场
        for i in range(len(team)):
            self.screen.find_ele_picture('game\\bidou\\1', 'mouse', 759, 569)
            time.sleep(0.5)
            self.mouse.click_element(163, 329, times=0.5)
            self.common.change_teamer(0.5)
        # 组队
        for i in range(len(team)):
            self.keyboard.press_shortcut_key('alt', '1')
            self.mouse.click_element(428, 347, times=0.5)
            self.keyboard.press_shortcut_key('alt', '1')
            self.common.change_teamer(0.5)
        time.sleep(5)
        for i in range(len(team)):
            if (i % 2) == 0:
                self.keyboard.press_shortcut_key('alt', '5')
                self.keyboard.press_shortcut_key('alt', 't')
                self.mouse.click_element(405, 310, times=0.5)
                while True:
                    time.sleep(1)
                    self.screen.cut_screen()
                    time.sleep(1)
                    result_4 = self.screen.get_location_picture("C:\\dh2\\game\\wuhuan\\9.png", num=0.8)
                    if result_4 is 0:
                        self.keyboard.press_shortcut_key('alt', 'f')
                    else:
                        break
                self.mouse.click_element(701, 312, times=0.5)
                self.mouse.click_element(715, 338, times=0.5, right=True)
                self.screen.find_ele_picture('game\\bidou\\2', 'mouse', 387, 504)
                self.mouse.click_element(414, 531, times=0.5, right=True)
                self.keyboard.press_shortcut_key('alt', 'f')
                self.mouse.click_element(772, 190, times=0.5)
            else:
                self.screen.find_ele_picture('game\\bidou\\3', 'mouse', 344, 413)
            self.common.change_teamer(0.5)
        # 任务开始 
        list_pos = []
        if int(len(team)) is 6:
            list_pos = [77, 330, 575]
        elif int(len(team)) is 4:
            list_pos = [104, 460]
        for j in range(15):
            for z in range(int(len(team)/2)):
                self.mouse.click_element(405, 500, times=0.5, right=True)
                time.sleep(1)
                pyautogui.rightClick()
                self.screen.find_ele_picture('game\\bidou\\begin2', 'mouse', 488, 504)
                self.mouse.click_direct_element(309, 489)
                self.common.change_teamer(2)
                self.mouse.click_element(309, 489)
                self.mouse.click_element(list_pos[z], 42)      
                self.screen.find_ele_picture('game\\system\\zidong', 'mouse', 170, 150)                  
                pyautogui.rightClick()
                if team[z] is 0:
                    self.keyboard.press_shortcut_key('alt', 'a')
                    self.keyboard.press_shortcut_key('alt', 'a')
                    self.keyboard.press_shortcut_key('alt', '8')
                    self.common.change_teamer(0.5)
                    self.keyboard.press_shortcut_key('alt', 'a')
                    self.keyboard.press_shortcut_key('alt', 'a')
                    self.keyboard.press_shortcut_key('alt', '8')
                    self.common.change_teamer(0.5)
                else:
                    if self.bidou_list[z] is 0:
                        result = 0
                        for ii in range(2):
                            self.keyboard.press_shortcut_key('alt', 'w')
                            self.mouse.click_direct_element(317, 178, right=True)
                            if ii is 0:
                                result = self.common.find_attack(type='s', str='zidong', x_pos=376, y_pos=240)
                            else:
                                self.keyboard.press_shortcut_key('alt', 's')
                                self.mouse.click_direct_element(result[0], result[1])

                            self.keyboard.press_shortcut_key('alt', 'w')
                            self.mouse.click_direct_element(317, 178, right=True)
                            self.keyboard.press_shortcut_key('alt', 's')
                            self.mouse.click_direct_element(result[0], result[1])
                            self.keyboard.press_shortcut_key('alt', '8')
                            self.common.change_teamer(0.5)
                        self.bidou_list[z] = 1
                    else:
                        result = 0
                        for ii in range(2):
                            if ii is 0:
                                result = self.common.find_attack(type='s', str='zidong', x_pos=376, y_pos=240)
                            else:
                                self.keyboard.press_shortcut_key('alt', 's')
                                self.mouse.click_direct_element(result[0], result[1])

                            self.keyboard.press_shortcut_key('alt', 's')
                            self.mouse.click_direct_element(result[0], result[1])
                            self.keyboard.press_shortcut_key('alt', '8')
                            self.common.change_teamer(0.5)
                

if __name__ == '__main__':
#     # 0攻击 1法术
    list = [1, 1, 1, 1, 1, 1]
    # print(len(list))
    KuaFuBiDou().task_start(list)

    # for z in range(int(len(list)/2)):
    #     print(z)
