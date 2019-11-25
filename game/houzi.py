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
    def houzi_task(self,place):
        self.common.get_focus()
        # self.keyboard.press_shortcut_key('alt', '2', times=0.5)
        # self.mouse.click_element(320, 411, times=0.5)
        # self.mouse.click_element(540, 425, times=0.5)
        # self.keyboard.press_shortcut_key('alt', '2', times=0.5)
        # self.common.iswalking()
        num = 0
        while num<30:
            if num%5:
                for j in range(5):
                    if j is 0:
                        self.mouse.click_element(697, 131, times=0.5)
                    else:
                        pyautogui.click()
                    self.common.change_teamer()
            for i in place:
                # 打开地图
                self.keyboard.press_shortcut_key('alt', '1',times=0.5)
                self.mouse.click_element(i[0], i[1], times=0.5)
                self.keyboard.press_shortcut_key('alt', '1', times=0.5)
                while True:
                    walking = self.common.iswalking()
                    if walking is False:
                        break
                while True:
                    result = self.task_start()
                    if result is 'success':
                        # self.keyboard.press_shortcut_key('alt', '2', times=0.5)
                        # self.mouse.click_element(499, 419, times=0.5)
                        # self.mouse.click_element(466, 211, times=0.5)
                        num+=1
                    else:
                        print("找不到")
                        break


    def task_start(self):
        while True:
            self.screen.cut_screen_location(820,650,0,0)
            time.sleep(0.5)
            result = Screen().find_color_ele(400,400,350,250,r1=250,r2=260,g1=250,g2=260,b1=0,b2=10,cut_zone=True)
            if result is not None:
                self.mouse.click_element(result[0]-10, result[1]-25,times=0.5)
                self.screen.cut_screen()
                time.sleep(0.5)
                loc = self.screen.get_location_picture("D:\\dh2\\houzi\\2.png", num=0.7)
                if loc is not 0:
                    self.mouse.click_element(178, 345, times=0.5)
                    time.sleep(10)
                    while True:
                        self.screen.cut_screen()
                        time.sleep(1.5)
                        pos_zidong = self.screen.get_location_picture("D:\\dh2\\game\\system\\zidong.png")
                        if pos_zidong is None:
                            break
                return 'success'
            else:
                return 'failed'
if __name__ == '__main__':
    # 万寿
    list_wangshou = [[530,432],[520,252],[470,300],[409,349],[382,461],[280,461],[270,339],[270,247]]
    HouZi().houzi_task(list_wangshou)
    # print(HouZi().task_start())