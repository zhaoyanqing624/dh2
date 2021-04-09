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
from skimage import io
import pyautogui
class HouZi:
    def __init__(self):
        self.transform = TransForm()
        self.common = Common()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.mouse = Mouse()

    def task_begin(self,num,place):
        time.sleep(20)
        while True:
            walking = self.common.iswalking()
            if walking is False:
                break
        for i in place:
            # 打开地图
            self.keyboard.press_shortcut_key('alt', '1', times=0.5)
            self.mouse.click_element(i[0], i[1], times=0.5)
            self.keyboard.press_shortcut_key('alt', '1', times=0.5)
            while True:
                walking = self.common.iswalking()
                if walking is False:
                    break
            result = self.task_start()
            if result is 'success':
                # self.keyboard.press_shortcut_key('alt', '2', times=0.5)
                # self.mouse.click_element(499, 419, times=0.5)
                # self.mouse.click_element(466, 211, times=0.5)
                num += 1
                if num is 3:
                    self.return_task()
                    return 'success'

    def houzi_task(self,place,pos=[320, 411]):
        total_num = 0
        while total_num < 10:
            self.common.get_focus()
            self.mouse.click_element(183, 197, times=0.5)
            self.keyboard.press_shortcut_key('alt', 'q', times=0.5)
            self.keyboard.press_shortcut_key('alt', 'q', times=0.5)
            self.keyboard.press_shortcut_key('alt', '2', times=0.5)
            self.mouse.click_element(pos[0], pos[1], times=0.5)
            self.mouse.click_element(540, 425, times=0.5)
            self.keyboard.press_shortcut_key('alt', '2', times=0.5)
            self.common.iswalking()
            num = 0
            self.common.capation_eat_xiang()
            # if num%5:
            #     for j in range(5):
            #         if j is 0:
            #             self.mouse.click_element(697, 131, times=0.5)
            #         else:
            #             pyautogui.click()
            #         self.common.change_teamer()
            result = self.task_begin(num, place)
            if result is 'success':
                total_num+=1

    def task_start(self):
        tol = 0
        endtime = time.time() + int(40)
        while time.time() < endtime:
            self.screen.cut_screen_location(820,650,0,0)
            time.sleep(0.5)
            result = Screen().find_color_ele(400,400,350,250,r1=250,r2=260,g1=250,g2=260,b1=0,b2=10,cut_zone=True)
            if result is not None:
                tol = 0
                self.mouse.click_direct_element(result[0]-10, result[1]-25)
                self.screen.cut_screen()
                time.sleep(1.5)
                loc = self.screen.get_location_picture("C:\\dh2\\houzi\\2.png", num=0.9)
                if loc is not 0:
                    self.mouse.click_element(178, 345, times=0.5)
                    time.sleep(2)
                    self.screen.cut_screen()
                    time.sleep(1.5)
                    result = self.screen.get_location_picture("C:\\dh2\\game\\system\\zidong.png", num=0.8)
                    if result is not 0:
                        for i in range(5):
                            self.keyboard.press_shortcut_key('alt', '8', times=0.5)
                            self.common.change_teamer()
                        time.sleep(5)
                        # self.screen.find_ele_picture('game\\system\\caozuo2', 'mouse', 80, 47)
                        self.common.game_over()
                        return "success"
            else:
                tol += 1
                if tol >= 2:
                    return "fail"
        return "fail"

    def return_task(self):
        time.sleep(1)
        self.keyboard.press_shortcut_key('alt', 'q', times=0.5)
        self.mouse.click_element(484, 239, times=0.5)
        self.keyboard.press_shortcut_key('alt', 'q', times=0.5)
        self.screen.find_ele_picture('game\\houzi\\3', 'mouse', 170, 400)
        time.sleep(5)

# if __name__ == '__main__':
#     # 万寿
#     list_wangshou = [[530,432],[560,413],[566,370],[512,378],[522,323],[562,271],[520,252],[470,300],[444,328],[415,319],[409,349],[386,396],[382,461],[343,475],[307,461],[270,476],[280,400],[286,375],[270,348],[274,296],[270,247],[370,255],[530,432],[560,413],[566,370],[512,378],[522,323],[562,271],[520,252],[470,300],[444,328],[415,319],[409,349],[386,396],[382,461],[343,475],[307,461],[270,476],[280,400],[286,375],[270,348],[274,296],[270,247],[370,255]]
#     HouZi().houzi_task(list_wangshou)

    # print(HouZi().task_start())
    # print(HouZi().task_start())
    # num = 0
    # houzi = HouZi()
    # for j in range(6):
    #     result = houzi.task_start()
    #     if result is 'success':
    #         # self.mouse.click_element(499, 419, times=0.5)
    #         # self.mouse.click_element(466, 211, times=0.5)
    #         num += 1
    #         if num is 3:
    #             houzi.return_task()
    #             print(1111111111111111111)
    #     else:
    #         break