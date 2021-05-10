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

    def make_sure(self, type):
        self.common.get_focus()
        if type is 0:
            self.mouse.click_element(311, 490)
        elif type is 1:
            for i in range(5):
                self.mouse.click_element(311, 490)
                self.common.change_teamer()
        self.common.get_focus()

    def game_over(self):
        endtime = time.time() + int(300)
        while time.time() < endtime:
            time.sleep(1)
            self.screen.cut_screen()
            time.sleep(1.5)
            result_ = self.screen.get_location_picture("C:\\dh2\\game\\system\\zidong.png", num=0.8)
            if result_ is 0:
                return True
        return False

    def start_task(self, level):
        for i in range(2):
            self.common.get_focus()
            # 任务开始
            self.keyboard.press_shortcut_key('alt', '2')
            self.mouse.click_element(539, 386)
            time.sleep(1)
            self.mouse.click_element(618, 463)
            time.sleep(10)
            # 寻找NPC 185,380
            self.screen.find_ele_picture('yitiao\\digong\\begin', 'mouse', 185, 380)
            time.sleep(2)
            self.mouse.click_element(547, 146, times=0.5)
            time.sleep(2)
            self.mouse.click_element(204, 378, times=0.5)
            time.sleep(2)
            self.mouse.click_element(64, 242, times=0.5)
            # 点老鼠
            self.screen.find_ele_picture('yitiao\\digong\\1')
            time.sleep(2)
            self.mouse.click_element(202, 363, times=0.5)
            time.sleep(1)
            self.mouse.click_element(197, 345, times=0.5)
            time.sleep(1)
            pyautogui.click()
            # 点击任务栏
            time.sleep(1)
            if level is 0:
                self.mouse.click_element(178, 240, times=0.5)
                time.sleep(2)
                #self.mouse.click_element(486, 239, times=0.5)
                self.screen.find_ele_picture('yitiao\\digong\\2_0', 'mouse', 179, 327)
            elif level is 1:
                self.mouse.click_element(178, 257, times=0.5)
                time.sleep(2)
                #self.mouse.click_element(486, 275, times=0.5)
                self.screen.find_ele_picture('yitiao\\digong\\2_1', 'mouse', 179, 350)
            # 组队确认
            self.make_sure(type=0)
            time.sleep(20)
            self.game_over()
            print("地宫第 " + str(i) + " 次任务结束")




