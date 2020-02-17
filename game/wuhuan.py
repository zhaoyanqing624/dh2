import time
from game.common import Common
from system.transform import TransForm
from system.keyboard import KeyBoard
from system.screen import Screen
from system.mouse import Mouse
import _Tools.getFighting
import pyautogui
class WuHuan():
    def __init__(self):
        self.transform = TransForm()
        self.common = Common()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.mouse = Mouse()
    def classify(self):
        self.screen.cut_screen()
        time.sleep(1)
        jieshou = self.screen.get_location_picture("D:\\dh2\\game\\wuhuan\\2.png",num=0.8)
        if jieshou is not 0:
            return 'jieshou',jieshou
        jieshou2 = self.screen.get_location_picture("D:\\dh2\\game\\wuhuan\\3.png",num=0.8)
        if jieshou2 is not 0:
            return 'jieshou2',jieshou2
        guidui = self.screen.get_location_picture("D:\\dh2\\game\\wuhuan\\5.png",num=0.8)
        if guidui is not 0:
            return 'guidui',[177, 345]
        return 'wu,0'


    def task_start(self):
        self.common.get_focus()
        while True:
            try:
                self.screen.cut_screen()
                time.sleep(1.5)
                location = self.screen.get_location_picture("D:\\dh2\\game\\wuhuan\\1.png",num=0.996)
                print(location)
                if location is not 0:
                    self.mouse.click_element(location[0],location[1])
                    result = self.classify()
                    if result[0] is 'jieshou':
                        self.mouse.click_element(result[1][0], result[1][1])
                        pyautogui.moveTo(166, 366, 1, pyautogui.easeInQuad)
                        self.mouse.click_element(374, 384,times=1)
                        pyautogui.click()
                    elif result[0] is 'jieshou2':
                        self.mouse.click_element(result[1][0], result[1][1])
                        pyautogui.moveTo(166, 366, 1, pyautogui.easeInQuad)
                        # 判断归队
                        self.screen.cut_screen()
                        time.sleep(1)
                        guidui = self.screen.get_location_picture("D:\\dh2\\game\\wuhuan\\4.png",num=0.7)
                        if guidui is not 0:
                            self.mouse.click_element(guidui[0], guidui[1])
                            time.sleep(1)
                            self.screen.cut_screen()
                            time.sleep(1)
                            guidui2 = self.screenget_location_picture("D:\\dh2\\game\\wuhuan\\5.png", num=0.9)
                            if guidui2 is not 0:
                                self.mouse.click_element(177, 345)
                        self.mouse.click_element(374, 384,times=1)
                        pyautogui.click()
                    elif result[0] is 'guidui':
                        self.mouse.click_element(177, 345)
                        self.mouse.click_element(374, 384, times=1)
                        pyautogui.click()
                else:
                    result = self.classify()
                    if result[0] is 'jieshou':
                        self.mouse.click_element(result[1][0], result[1][1])
                        pyautogui.moveTo(166, 366, 1, pyautogui.easeInQuad)
                        self.mouse.click_element(374, 384,times=1)
                        pyautogui.click()
                    elif result[0] is 'jieshou2':
                        self.mouse.click_element(result[1][0], result[1][1])
                        pyautogui.moveTo(166, 366, 1, pyautogui.easeInQuad)
                        # 判断归队
                        self.screen.cut_screen()
                        time.sleep(1)
                        guidui = self.screen.get_location_picture("D:\\dh2\\game\\wuhuan\\4.png",num=0.7)
                        if guidui is not 0:
                            self.mouse.click_element(guidui[0], guidui[1])
                        guidui2 = self.screenget_location_picture("D:\\dh2\\game\\wuhuan\\5.png", num=0.8)
                        if guidui2 is not 0:
                            self.mouse.click_element(177, 345)
                        self.mouse.click_element(374, 384,times=1)
                        pyautogui.click()
                    elif result[0] is 'guidui':
                        self.mouse.click_element(177, 345)
                        self.mouse.click_element(374, 384, times=1)
                        pyautogui.click()
            except:
                pass





if __name__ == '__main__':
    # 开始
    WuHuan().task_start()