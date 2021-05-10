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
import gc


class WuHuan():
    def __init__(self):
        self.transform = TransForm()
        self.common = Common()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.mouse = Mouse()
        self.operate_list = [0, 0, 0, 0, 0]

    # 寻找NPC
    def find_npc(self):
        self.common.capation_eat_xiang()
        self.keyboard.press_shortcut_key('alt', '2')
        self.mouse.click_element(500, 418, times=1)
        self.mouse.click_element(214, 288, times=1)

    # 操作
    def operate(self, i, i_, operate=[]):
        self.screen.find_ele_picture('game\\system\\zidong')
        time.sleep(1)
        if self.operate_list[i] is 0:
            # 未操作过
            result = self.common.find_attack('f6')
            if operate[i] is 0:
                pyautogui.click()
            else:
                if i_ is 0:
                    self.keyboard.press_shortcut_key('alt', 'w')
                    self.mouse.click_element(317, 200, times=0.5, right=True)
                    self.keyboard.press_shortcut_key('alt', 's')
                    self.mouse.click_direct_element(result[0], result[1])
            self.operate_list[i] = 1
        self.keyboard.press_shortcut_key('alt', '8')

    # 获取任务
    def get_task(self, zhongzu, sanzhuan, operate):
        haha = 0
        self.screen.find_ele_picture('game\\wuhuan\\6', 'mouse', 207, 395)
        while True:
            time.sleep(1)
            self.screen.cut_screen()
            time.sleep(1.5)
            result_1 = self.screen.get_location_picture("C:\\dh2\\game\\wuhuan\\7.png", num=0.8)
            if result_1 is not 0:
                if sanzhuan is None:
                    self.mouse.click_element(163, 328, times=1)
                else:
                    self.mouse.click_element(163, 338, times=1)
                    haha =1
            else:
                result_2 = self.screen.get_location_picture("C:\\dh2\\game\\wuhuan\\7_1.png", num=0.8)
                if result_2 is not 0:
                    self.mouse.click_element(170, 350, times=0.5)
                    self.keyboard.press_shortcut_key('alt', '2')
                    self.mouse.click_element(500, 418, times=1)
                    self.mouse.click_element(214, 288, times=1)
                    self.keyboard.press_shortcut_key('alt', '2')
                    time.sleep(2)
                    self.mouse.click_element(207, 395, times=1)
                else:
                    result_3 = self.screen.get_location_picture("C:\\dh2\\game\\wuhuan\\8.png", num=0.8)
                    if result_3 is not 0:
                        self.mouse.click_element(170, 350, times=0.5)
                        break
        if haha is 0:
            while True:
                time.sleep(1)
                self.screen.cut_screen()
                time.sleep(1)
                result_4 = self.screen.get_location_picture("C:\\dh2\\game\\wuhuan\\9.png", num=0.8)
                if result_4 is 0:
                    self.keyboard.press_shortcut_key('alt', 'f')
                else:
                    self.mouse.click_element(689, 351, times=0.5)
                    self.mouse.click_element(689, 375, times=1, right=True)
                    self.mouse.click_element(382, 504, times=0.5)
                    self.mouse.click_element(162, 225, times=0.5)
                    self.mouse.click_element(340, 402, times=0.5)
                    self.mouse.click_element(689, 351, times=0.5)
                    self.keyboard.press_shortcut_key('alt', 'f')
                    time.sleep(20)
                    self.screen.cut_screen()
                    time.sleep(1)
                    result_4 = self.screen.get_location_picture("C:\\dh2\\game\\wuhuan\\4_1.png", num=0.8)
                    if result_4 is not 0:
                        self.mouse.click_element(439, 99, times=1)
                    break
        # 开始任务
        for i in range(5):
            if i is 0:
                self.mouse.click_element(399, 200, times=1, right=True)
                pyautogui.rightClick()
                self.mouse.click_element(399, 168, times=1, right=True)
                pyautogui.rightClick()
                self.mouse.click_element(399, 135, times=1, right=True)
                pyautogui.rightClick()
            self.mouse.click_element(165, 240, times=1)
            pyautogui.rightClick()
            self.mouse.click_element(130, 240, times=1)
            pyautogui.rightClick()
            self.common.heyao()
            while True:
                if self.task_classify(zhongzu, i, operate) is not 0:
                    break
            if i is 4:
                self.keyboard.press_shortcut_key('alt', '2')
                self.mouse.click_element(500, 418, times=1)
                self.mouse.click_element(214, 288, times=1)
                time.sleep(100)
                self.keyboard.press_shortcut_key('alt', 't')
                #self.screen.find_ele_picture('game\\wuhuan\\6_', 'keyboard', 'alt', 't')
                self.mouse.click_element(338, 505, times=1)

    # 任务种类
    def task_classify(self, zhongzu, cicle, operate):
        time.sleep(1)
        self.screen.cut_screen()
        time.sleep(1.5)
        for i in range(10, 16):
            file_name = "C:\\dh2\\game\\wuhuan\\" + str(i) + ".png"
            result = self.screen.get_location_picture(file_name, 0.8)
            if result != 0:
                if i == 10:
                    print("盗号贼")
                    self.mouse.click_element(170, 350, times=1)
                    self.mouse.click_element(146, 241, times=1)
                    self.operate(zhongzu, cicle, operate)
                    if cicle is not 4:
                        self.screen.find_ele_picture('game\\wuhuan\\10_1', 'mouse', 170, 350)
                    else:
                        self.screen.find_ele_picture('game\\wuhuan\\15', 'mouse', 170, 350)
                    self.mouse.click_element(170, 350, times=1)
                    return i
                elif i == 11:
                    print("惯骗")
                    self.mouse.click_element(170, 350, times=1)
                    self.mouse.click_element(158, 241, times=1)
                    self.operate(zhongzu, cicle, operate)
                    if cicle is not 4:
                        self.screen.find_ele_picture('game\\wuhuan\\11_1', 'mouse', 170, 350)
                    else:
                        self.screen.find_ele_picture('game\\wuhuan\\15', 'mouse', 170, 350)
                    self.mouse.click_element(170, 350, times=1)
                    return i
                elif i == 12:
                    print("过称")
                    self.mouse.click_element(170, 350, times=1)
                    self.mouse.click_element(170, 241, times=1)
                    self.operate(zhongzu, cicle, operate)
                    if cicle is not 4:
                        self.screen.find_ele_picture('game\\wuhuan\\12_1', 'mouse', 170, 350)
                    else:
                        self.screen.find_ele_picture('game\\wuhuan\\15', 'mouse', 170, 350)
                    self.mouse.click_element(170, 350, times=1)
                    return i
                elif i == 13:
                    print("PK狂")
                    self.mouse.click_element(170, 350, times=1)
                    self.mouse.click_element(158, 241, times=1)
                    self.operate(zhongzu, cicle, operate)
                    if cicle is not 4:
                        self.screen.find_ele_picture('game\\wuhuan\\13_1', 'mouse', 170, 350)
                    else:
                        self.screen.find_ele_picture('game\\wuhuan\\15', 'mouse', 170, 350)
                    self.mouse.click_element(170, 350, times=1)
                    return i
                elif i == 14:
                    print("送温暖")
                    self.mouse.click_element(170, 390, times=1)
                    self.mouse.click_element(165, 240, times=0.5)
                    time.sleep(1)
                    self.mouse.click_element(165, 345, times=1)
                    if cicle is 4:
                        self.screen.find_ele_picture('game\\wuhuan\\15', 'mouse', 170, 350)
                    self.mouse.click_element(170, 350, times=1)
                    self.mouse.click_element(170, 350, times=1)
                    self.mouse.click_element(170, 350, times=1)
                    return i
        return 0

    def classify(self):
        self.screen.cut_screen()
        time.sleep(1)
        jieshou = self.screen.get_location_picture("C:\\dh2\\game\\wuhuan\\2.png", num=0.8)
        if jieshou is not 0:
            return 'jieshou', jieshou
        jieshou2 = self.screen.get_location_picture("C:\\dh2\\game\\wuhuan\\3.png", num=0.8)
        if jieshou2 is not 0:
            return 'jieshou2', jieshou2
        guidui = self.screen.get_location_picture("C:\\dh2\\game\\wuhuan\\5.png", num=0.8)
        if guidui is not 0:
            return 'guidui', [177, 345]
        return 'wu,0'

    def task_start(self, type=0, sanzhuan=None, operate=None):
        self.common.get_focus()
        # 切换宝宝
        for i in range(5):
            self.keyboard.press_shortcut_key('alt', '5')
            time.sleep(1)
            self.keyboard.press_shortcut_key('alt', 't')
            self.mouse.click_element(406, 325, times=0.5)
            self.common.change_dog(3)
            time.sleep(1)
            self.common.change_teamer(times=0.3)

        if type is 0:
            index = 0
            while True:
                try:
                    self.screen.cut_screen()
                    time.sleep(1.5)
                    location = self.screen.get_location_picture("C:\\dh2\\game\\wuhuan\\1.png", num=0.996)
                    if location is not 0:
                        self.mouse.click_element(location[0], location[1])
                        result = self.classify()
                        if result[0] is 'jieshou':
                            self.mouse.click_element(result[1][0], result[1][1])
                            pyautogui.moveTo(166, 366, 1, pyautogui.easeInQuad)
                            self.mouse.click_element(374, 384, times=1)
                            pyautogui.click()
                            pyautogui.click()
                        elif result[0] is 'jieshou2':
                            self.mouse.click_element(result[1][0], result[1][1])
                            pyautogui.moveTo(166, 366, 1, pyautogui.easeInQuad)
                            # 判断归队
                            self.screen.cut_screen()
                            time.sleep(1)
                            guidui = self.screen.get_location_picture("C:\\dh2\\game\\wuhuan\\4.png", num=0.7)
                            if guidui is not 0:
                                self.mouse.click_element(guidui[0], guidui[1])
                                time.sleep(1)
                                self.screen.cut_screen()
                                time.sleep(1)
                                guidui2 = self.screenget_location_picture("C:\\dh2\\game\\wuhuan\\5.png", num=0.9)
                                if guidui2 is not 0:
                                    self.mouse.click_element(177, 345)
                            self.mouse.click_element(374, 384, times=1)
                            pyautogui.click()
                            pyautogui.click()
                        elif result[0] is 'guidui':
                            self.mouse.click_element(177, 345)
                            self.mouse.click_element(374, 384, times=1)
                            pyautogui.click()
                            pyautogui.click()
                    else:
                        result = self.classify()
                        if result[0] is 'jieshou':
                            self.mouse.click_element(result[1][0], result[1][1])
                            pyautogui.moveTo(166, 366, 1, pyautogui.easeInQuad)
                            self.mouse.click_element(374, 384, times=1)
                            pyautogui.click()
                            pyautogui.click()
                        elif result[0] is 'jieshou2':
                            self.mouse.click_element(result[1][0], result[1][1])
                            pyautogui.moveTo(166, 366, 1, pyautogui.easeInQuad)
                            # 判断归队
                            self.screen.cut_screen()
                            time.sleep(1)
                            guidui = self.screen.get_location_picture("C:\\dh2\\game\\wuhuan\\4.png", num=0.7)
                            if guidui is not 0:
                                self.mouse.click_element(guidui[0], guidui[1])
                            guidui2 = self.screenget_location_picture("C:\\dh2\\game\\wuhuan\\5.png", num=0.8)
                            if guidui2 is not 0:
                                self.mouse.click_element(177, 345)
                            self.mouse.click_element(374, 384, times=1)
                            pyautogui.click()
                            pyautogui.click()
                        elif result[0] is 'guidui':
                            self.mouse.click_element(177, 345)
                            self.mouse.click_element(374, 384, times=1)
                            pyautogui.click()
                            pyautogui.click()
                        else:
                            index += 1
                        if index > 100:
                            index = 0
                        if not index % 15:
                            self.common.change_teamer()
                    gc.collect()
                except:
                    gc.collect()
                    pass
        else:
            for j in range(5):
                self.find_npc()
                self.get_task(j, sanzhuan, operate)
                self.common.change_teamer()

if __name__ == '__main__':
     # 开始
     WuHuan().task_start(type=1, sanzhuan=True, operate=[1, 1, 1, 1, 1])
     #WuHuan().task_start(type=0)
