import time
from game.common import Common
from system.transform import TransForm
from system.keyboard import KeyBoard
from system.screen import Screen
from system.mouse import Mouse
import pyautogui

class GuZhu():
    def __init__(self):
        self.transform = TransForm()
        self.common = Common()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.mouse = Mouse()

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

    def start_task(self, level):
        self.common.get_focus()
        self.keyboard.press_shortcut_key('alt', '2')
        self.mouse.click_element(502, 419)
        time.sleep(2)
        self.mouse.click_element(587, 362)
        time.sleep(10)
        # 寻找NPC
        self.screen.find_ele_picture('yitiao\\guzhu\\begin')
        self.mouse.click_element(182, 328, times=0.5)
        time.sleep(2)
        self.make_sure()
        time.sleep(10)
        # 宠物医生
        self.screen.find_ele_picture(file_path='system\\zidong_', handle='self')
        self.mouse.click_element(245, 275, times=0.5)
        self.make_sure_wuyi()
        time.sleep(2)
        # 第一个
        self.mouse.click_element(93, 241, times=0.5)
        self.screen.find_ele_picture('yitiao\\guzhu\\1', 'mouse', 169, 329)
        self.operate()
        self.game_over()
        time.sleep(2)

        # 第二个
        self.screen.find_ele_picture(file_path='system\\zidong_', handle='self')
        self.mouse.click_element(93, 241, times=0.5)
        self.screen.find_ele_picture('yitiao\\guzhu\\2', 'mouse', 169, 329)
        self.operate([276, 185])
        self.game_over()
        time.sleep(2)

        # 第三个
        self.screen.find_ele_picture(file_path='system\\zidong_', handle='self')
        self.mouse.click_element(93, 241, times=0.5)
        self.screen.find_ele_picture('yitiao\\guzhu\\3', 'mouse', 169, 329)
        self.operate([201, 339])
        self.game_over()
        time.sleep(2)

        # 第四个
        self.screen.find_ele_picture(file_path='system\\zidong_', handle='self')
        self.mouse.click_element(93, 241, times=0.5)
        if int(level[0]) is 0:
            self.screen.find_ele_picture('yitiao\\guzhu\\4', 'mouse', 169, 329)
        elif int(level[0]) is 1:
            self.screen.find_ele_picture('yitiao\\guzhu\\4', 'mouse', 169, 345)
            self.mouse.click_element(311, 490)
        self.operate([236, 245])
        self.game_over()
        time.sleep(2)
        # 宠物医生
        self.mouse.click_element(475, 275, times=0.5)
        self.make_sure_wuyi()
        time.sleep(2)

        # 第五个
        self.screen.find_ele_picture(file_path='system\\zidong_', handle='self')
        self.mouse.click_element(93, 241, times=0.5)
        if int(level[1]) is 0:
            self.screen.find_ele_picture('yitiao\\guzhu\\5', 'mouse', 169, 329)
        elif int(level[1]) is 1:
            self.screen.find_ele_picture('yitiao\\guzhu\\5', 'mouse', 169, 345)
            self.mouse.click_element(311, 490)
        self.operate([273, 173])
        self.game_over()
        time.sleep(2)

        # 第六个
        self.mouse.click_element(93, 241, times=0.5)
        self.screen.find_ele_picture('yitiao\\guzhu\\6', 'mouse', 175, 347)
        self.mouse.click_element(169, 346)
        time.sleep(2)
        self.keyboard.press_shortcut_key('alt', '1')

        # 第七个
        self.screen.find_ele_picture(file_path='system\\zidong_', handle='self')
        self.mouse.click_element(93, 241, times=0.5)
        if int(level[2]) is 0:
            self.screen.find_ele_picture('yitiao\\guzhu\\7', 'mouse', 169, 329)
        elif int(level[2]) is 1:
            self.screen.find_ele_picture('yitiao\\guzhu\\7', 'mouse', 169, 345)
            self.mouse.click_element(311, 490)
        self.operate([296, 366])
        self.game_over()
        time.sleep(2)

        # 第八个
        self.screen.find_ele_picture(file_path='system\\zidong_', handle='self')
        self.mouse.click_element(93, 241, times=0.5)
        if int(level[3]) is 0:
            self.screen.find_ele_picture('yitiao\\guzhu\\8', 'mouse', 169, 329)
            self.operate([116, 505])
        elif int(level[3]) is 1:
            self.screen.find_ele_picture('yitiao\\guzhu\\8', 'mouse', 169, 345)
            self.mouse.click_element(311, 490)
            self.operate([332, 282])
        self.game_over()
        time.sleep(15)





