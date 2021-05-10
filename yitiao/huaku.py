import time
from game.common import Common
from system.transform import TransForm
from system.keyboard import KeyBoard
from system.screen import Screen
from system.mouse import Mouse
import pyautogui

class HuaKu():

    def __init__(self):
        self.transform = TransForm()
        self.common = Common()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.mouse = Mouse()
        self.maze = [
            [(200, 350), (200 + 75 * 1, 350 - 20 * 1), (200 + 75 * 1, 350 - 20 * 1), (200 + 75 * 1, 350 - 20 * 1),
             (200 + 75 * 1, 350 - 20 * 1)],
            [(260, 400), (260 + 75 * 1, 400 - 20 * 1), (260 + 75 * 1, 400 - 20 * 1), (260 + 75 * 1, 400 - 20 * 1),
             (260 + 75 * 1, 400 - 20 * 1)],
            [(320, 450), (320 + 75 * 1, 450 - 20 * 1), (320 + 75 * 1, 450 - 20 * 1), (320 + 75 * 1, 450 - 20 * 1),
             (320 + 75 * 1, 450 - 20 * 1)],
        ]

    def make_sure(self):
        for i in range(5):
            self.mouse.click_element(311, 490)
            self.common.change_teamer()
        self.common.get_focus()

    def make_sure_wuyi(self):
        for i in range(5):
            self.mouse.click_element(183, 347)
            self.common.change_teamer()
        self.common.get_focus()

    def game_over(self):
        endtime = time.time() + int(300)
        while time.time() < endtime:
            time.sleep(1)
            self.screen.cut_screen()
            time.sleep(1)
            result_ = self.screen.get_location_picture("C:\\dh2\\game\\system\\zidong.png", num=0.8)
            if result_ is 0:
                return True
        return False

    def operate(self, location=None):
        result_ = self.screen.find_ele_picture_time('game\\system\\caozuo')
        if result_ is True:
            if location is None:
                for i in range(5):
                    self.keyboard.press_shortcut_key('alt', '8')
                    self.common.change_teamer()
            else:
                for i in range(5):
                    if i is 0:
                        self.keyboard.press_key('f7')
                        self.mouse.click_direct_element(location[0], location[1])
                        self.keyboard.press_shortcut_key('alt', 't')
                        self.mouse.click_direct_element(650, 400)
                    self.keyboard.press_shortcut_key('alt', '8')
                    self.common.change_teamer()
        self.common.get_focus()

    def is_jiuren(self):
        Screen().cut_screen_by_PIL(60, 240, 80, 260, "C:\\dh2\\system\\1.PNG")
        result = Screen().find_color_ele(10, 10, 8, 8, 0, 0, 255, 255, 0, 0, True)
        if result is not None:
            return True
        else:
            return False

    def start_task(self, num, level):
        self.common.get_focus()
        self.keyboard.press_shortcut_key('alt', '2')
        self.mouse.click_element(241, 398)
        time.sleep(2)
        self.mouse.click_element(326, 379)
        time.sleep(10)
        # 寻找NPC
        self.screen.find_ele_picture('yitiao\\huaku\\begin')
        self.mouse.click_element(177, 328, times=0.5)
        time.sleep(2)
        self.make_sure()
        time.sleep(10)
        # 第一个
        self.keyboard.press_key('esc')
        while True:
            self.mouse.click_element(26, 252, times=0.5)
            if self.is_jiuren() is True:
                break
            else:
                time.sleep(5)
        self.mouse.click_element(63, 240, times=0.5)
        self.screen.find_ele_picture('yitiao\\huaku\\1', 'mouse', 177, 327)
        self.operate()
        self.game_over()
        time.sleep(2)
        # 第二个
        self.keyboard.press_key('esc')
        self.mouse.click_element(63, 244, times=0.5)
        time.sleep(10)
        self.mouse.click_element(56, 240, times=0.5)
        time.sleep(3)
        self.mouse.click_element(56, 240, times=0.5)
        self.screen.find_ele_picture('yitiao\\huaku\\2', 'mouse', 177, 327)
        self.operate()
        self.game_over()
        time.sleep(2)

        # 第三个
        self.keyboard.press_key('esc')
        time.sleep(1)
        self.mouse.click_element(60, 240, times=0.5)
        self.keyboard.press_shortcut_key('alt', '1')
        self.screen.find_ele_picture('yitiao\\huaku\\3', 'mouse', 168, 345)
        self.mouse.click_element(168, 345, times=0.5)
        time.sleep(5)

        # 第四个
        self.keyboard.press_key('esc')
        time.sleep(1)
        self.mouse.click_element(144, 240, times=0.5)
        if int(level[0]) is 0:
            self.screen.find_ele_picture('yitiao\\huaku\\4', 'mouse', 175, 345)
        elif int(level[0]) is 1:
            self.screen.find_ele_picture('yitiao\\huaku\\4', 'mouse', 175, 360)
            self.mouse.click_element(311, 490)
        self.operate()
        self.game_over()
        time.sleep(2)

        # 第五个
        self.mouse.click_element(72, 241, times=0.5)
        if int(level[1]) is 0:
            self.screen.find_ele_picture('yitiao\\huaku\\5', 'mouse', 175, 325)
        elif int(level[1]) is 1:
            self.screen.find_ele_picture('yitiao\\huaku\\5', 'mouse', 175, 345)
            self.mouse.click_element(311, 490)
        self.operate()
        self.game_over()
        time.sleep(2)

        # 宠物医生
        self.keyboard.press_key('esc')
        self.keyboard.press_shortcut_key('alt', '1')
        self.mouse.click_element(430, 363, times=0.5)
        self.screen.find_ele_picture('game\\system\\wuyi', 'mouse', 188, 344)
        self.common.change_teamer()
        for i in range(4):
            self.mouse.click_element(188, 344, times=0.5)
            self.common.change_teamer()
        self.keyboard.press_shortcut_key('alt', '1')
        self.make_sure_wuyi()
        time.sleep(2)

        # 第六个 - 摆弄阵眼
        self.mouse.click_element(60, 241, times=0.5)
        self.screen.find_ele_picture('yitiao\\huaku\\6', 'mouse', 171, 345)
        self.mouse.click_element(171, 345)
        time.sleep(2)
        self.keyboard.press_shortcut_key('alt', '1')
        time.sleep(2)

        # 第七个
        if num>=7:
            self.keyboard.press_key('esc')
            self.screen.find_ele_picture(file_path='system\\zidong_', handle='self')
            self.mouse.click_element(155, 240, times=0.5)
            if int(level[2]) is 0:
                self.screen.find_ele_picture('yitiao\\huaku\\7', 'mouse', 176, 327)
            elif int(level[2]) is 1:
                self.screen.find_ele_picture('yitiao\\huaku\\7', 'mouse', 176, 345)
                self.mouse.click_element(311, 490)
            self.operate([292, 358])
            self.game_over()
            time.sleep(2)

            # 宠物医生
            self.keyboard.press_key('esc')
            time.sleep(1)
            self.keyboard.press_shortcut_key('alt', '1')
            self.mouse.click_element(430, 363, times=0.5)
            self.screen.find_ele_picture('game\\system\\wuyi', 'mouse', 188, 344)
            self.common.change_teamer()
            for i in range(4):
                self.mouse.click_element(188, 344, times=0.5)
                self.common.change_teamer()
            self.keyboard.press_shortcut_key('alt', '1')
            self.make_sure_wuyi()
            time.sleep(2)

        # 第八个
        if num>=8:
            self.screen.find_ele_picture(file_path='system\\zidong_', handle='self')
            self.mouse.click_element(73, 241, times=0.5)
            if int(level[3]) is 0:
                self.screen.find_ele_picture('yitiao\\huaku\\8', 'mouse', 176, 327)
            elif int(level[3]) is 1:
                self.screen.find_ele_picture('yitiao\\huaku\\8', 'mouse', 176, 345)
                self.mouse.click_element(311, 490)
            self.operate([151, 431])
            self.game_over()
            time.sleep(5)

        # 宠物医生
        self.keyboard.press_key('esc')
        self.keyboard.press_shortcut_key('alt', '1')
        self.mouse.click_element(430, 363, times=0.5)
        self.screen.find_ele_picture('game\\system\\wuyi', 'mouse', 188, 344)
        self.common.change_teamer()
        for i in range(4):
            self.mouse.click_element(188, 344, times=0.5)
            self.common.change_teamer()
        self.keyboard.press_shortcut_key('alt', '1')
        self.make_sure_wuyi()
        time.sleep(2)

        # 退出
        self.screen.find_ele_picture(file_path='yitiao\\huaku\\0', handle='self')
        self.mouse.click_element(172, 328, times=0.5)



