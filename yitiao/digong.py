import time
from game.common import Common
from system.transform import TransForm
from system.keyboard import KeyBoard
from system.screen import Screen
from system.mouse import Mouse
import pyautogui

class DiGong():
    def __init__(self):
        self.transform = TransForm()
        self.common = Common()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.mouse = Mouse()
    def make_sure(self):
        self.common.get_focus()
        for i in range(3):
            self.mouse.click_element(311, 490)
            self.common.change_teamer()
        self.common.get_focus()
    def game_over(self):
        endtime = time.time() + int(300)
        while time.time() < endtime:
            time.sleep(1)
            self.screen.cut_screen()
            time.sleep(1)
            result_ = self.screen.get_location_picture("D:\\dh2\\game\\system\\zidong.png",num=0.8)
            if result_ is 0:
                return True
        return False

    def operate(self,level):
        self.common.get_focus()
        self.keyboard.press_shortcut_key('alt', '2')
        self.mouse.click_element(539, 386)
        time.sleep(2)
        self.mouse.click_element(618, 463)
        time.sleep(10)
        # 寻找NPC 185,380
        self.screen.find_ele_picture('yitiao\\digong\\begin')
        self.mouse.click_element(185, 380, times=0.5)
        time.sleep(2)
        self.mouse.click_element(547, 146, times=0.5)
        time.sleep(2)
        self.mouse.click_element(204, 378, times=0.5)
        time.sleep(2)
        self.mouse.click_element(64, 242, times=0.5)
        # 点老鼠
        self.screen.find_ele_picture('yitiao\\digong\\1')
        time.sleep(2)
        self.mouse.click_element(64, 242, times=0.5)
        time.sleep(2)
        self.mouse.click_element(202, 363, times=0.5)
        time.sleep(1)
        self.mouse.click_element(197, 345, times=0.5)
        time.sleep(1)
        pyautogui.click()
        # 点击任务栏
        time.sleep(1)
        self.mouse.click_element(44, 269, times=0.5)
        time.sleep(2)
        if level is '0':
            self.mouse.click_element(486, 239, times=0.5)
            self.screen.find_ele_picture('yitiao\\digong\\2_0')
            self.mouse.click_element(179, 327, times=0.5)
        elif level is '1':
            self.mouse.click_element(486, 275, times=0.5)
            self.screen.find_ele_picture('yitiao\\digong\\2_1')
            self.mouse.click_element(179, 350, times=0.5)
        # 组队确认
        self.make_sure()
        time.sleep(2)
        self.screen.find_ele_picture('system\\zidong')
        self.common.find_attack('f7')
        self.keyboard.press_shortcut_key('alt', 'd')
        self.keyboard.press_shortcut_key('alt', '8')
        self.common.change_teamer()
        for i in range(2):
            self.keyboard.press_key('f7')
            pyautogui.click()
            self.keyboard.press_shortcut_key('alt', 'd')
            self.keyboard.press_shortcut_key('alt', '8')
            self.common.change_teamer()
        self.common.get_focus()
        time.sleep(20)
        self.game_over()
        print("任务结束")







if __name__ == '__main__':
#     0简单 1难
    DiGong().operate('0')


