import time
from game.common import Common
from system.transform import TransForm
from system.keyboard import KeyBoard
from system.screen import Screen
from system.mouse import Mouse
import pyautogui

class DaYanTa():
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
            result_ = self.screen.get_location_picture("C:\\dh2\\game\\system\\zidong.png",num=0.8)
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

    def start_task(self, num, level):
        self.common.get_focus()
        self.keyboard.press_shortcut_key('alt', '2')
        self.mouse.click_element(502, 419)
        time.sleep(2)
        self.mouse.click_element(202, 254)
        time.sleep(10)
        # 寻找NPC 185,380
        self.screen.find_ele_picture('yitiao\\dayanta\\begin')
        self.mouse.click_element(177, 349, times=0.5)
        time.sleep(2)
        self.make_sure()
        time.sleep(5)
        # 第一个
        self.mouse.click_element(30, 257, times=0.5)
        self.screen.find_ele_picture('yitiao\\dayanta\\1', 'mouse', 180, 361)
        self.mouse.click_element(91, 240, times=0.5)
        self.screen.find_ele_picture('yitiao\\dayanta\\1_2', 'mouse', 169, 339)
        self.operate(location=None)
        self.game_over()
        self.mouse.click_element(30, 257, times=0.5)
        self.screen.find_ele_picture('yitiao\\dayanta\\1_3', 'mouse', 175, 344)
        time.sleep(3)
        # 第二个
        self.mouse.click_element(30, 257, times=0.5)
        self.screen.find_ele_picture('yitiao\\dayanta\\2', 'mouse', 180, 361)
        time.sleep(1.5)
        pyautogui.click()
        self.mouse.click_element(78, 240, times=0.5)
        time.sleep(60)
        self.screen.find_ele_picture(file_path='yitiao\\dayanta\\2_1', handle='self')
        time.sleep(1)
        self.mouse.click_element(91, 241, times=0.5)
        time.sleep(1)
        self.mouse.click_element(173, 327, times=0.5)
        self.operate(location=None)
        self.game_over()
        self.mouse.click_element(30, 257, times=0.5)
        self.screen.find_ele_picture('yitiao\\dayanta\\2_2', 'mouse', 183, 325)
        time.sleep(3)
        # 第三个
        self.mouse.click_element(319, 339, times=0.5)
        self.make_sure_wuyi()
        self.mouse.click_element(30, 257, times=0.5)
        self.screen.find_ele_picture('yitiao\\dayanta\\3', 'mouse', 180, 413)
        self.mouse.click_element(91, 240, times=0.5)
        self.operate(location=None)
        self.game_over()
        self.mouse.click_element(30, 257, times=0.5)
        self.screen.find_ele_picture('yitiao\\dayanta\\3_1', 'mouse', 175, 344)
        time.sleep(3)
        # 第四个
        self.screen.find_ele_picture(file_path='system\\zidong_', handle='self')
        self.mouse.click_element(30, 257, times=0.5)
        self.screen.find_ele_picture('yitiao\\dayanta\\4', 'mouse', 180, 361)
        time.sleep(1.5)
        pyautogui.click()
        time.sleep(2.5)
        self.mouse.click_element(41, 240, times=0.5)
        if int(level[0]) is 0:
            self.screen.find_ele_picture('yitiao\\dayanta\\4_1', 'mouse', 178, 345)
        elif int(level[0]) is 1:
            self.screen.find_ele_picture('yitiao\\dayanta\\4_1', 'mouse', 178, 360)
            self.mouse.click_element(311, 490)
        self.operate([292, 387])
        self.game_over()
        self.mouse.click_element(33, 255, times=0.5)
        self.screen.find_ele_picture('yitiao\\dayanta\\4_2', 'mouse', 183, 343)
        time.sleep(3)
        # 第五个
        self.screen.find_ele_picture(file_path='system\\zidong_', handle='self')
        self.mouse.click_element(30, 257, times=0.5)
        self.screen.find_ele_picture('yitiao\\dayanta\\5', 'mouse', 180, 344)
        time.sleep(1.5)
        pyautogui.click()
        time.sleep(1)
        self.mouse.click_element(150, 240, times=0.5)
        time.sleep(1)
        if int(level[1]) is 0:
            self.screen.find_ele_picture('yitiao\\dayanta\\5_1', 'mouse', 178, 345)
        elif int(level[1]) is 1:
            self.screen.find_ele_picture('yitiao\\dayanta\\5_1', 'mouse', 178, 360)
            self.mouse.click_element(311, 490)
        self.operate([370, 235])
        self.game_over()
        time.sleep(1)
        self.mouse.click_element(33, 255, times=0.5)
        if num is 5:
            self.screen.find_ele_picture('yitiao\\dayanta\\5_2', 'mouse', 190, 380)
            self.mouse.click_element(325, 400, times=0.5)
        else:
            self.screen.find_ele_picture('yitiao\\dayanta\\5_2', 'mouse', 190, 365)
        time.sleep(3)

        # 第六个
        if num >= 6:
            self.screen.find_ele_picture(file_path='system\\zidong_', handle='self')
            self.keyboard.press_shortcut_key('alt', '5')
            self.keyboard.press_shortcut_key('alt', 'q')
            self.keyboard.press_shortcut_key('alt', 'q')
            self.mouse.click_element(430, 250, times=0.5)
            self.make_sure_wuyi()
            self.mouse.click_element(30, 257, times=0.5)
            self.screen.find_ele_picture('yitiao\\dayanta\\6', 'mouse', 180, 381)
            time.sleep(1.5)
            pyautogui.click()
            if int(level[2]) is 0:
                for ii in range(4):
                    self.keyboard.press_shortcut_key('alt', 'q')
                    self.mouse.click_element(450, 305+ii*20, times=0.5)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    self.screen.find_ele_picture('yitiao\\dayanta\\6_1_'+str(ii+1), 'mouse', 190, 328)
                    self.operate()
                    self.game_over()
                self.mouse.click_element(41, 240, times=0.5)
                # 未完待续 -
                time.sleep(3)
                self.mouse.click_element(41, 240, times=0.5)
                self.screen.find_ele_picture('yitiao\\dayanta\\7_4', 'mouse', 190, 328)
                self.operate(location=None)
                self.game_over()
            elif int(level[2]) is 1:
                self.mouse.click_element(41, 240, times=0.5)
                self.screen.find_ele_picture('yitiao\\dayanta\\6_1', 'mouse', 178, 350)
                self.mouse.click_element(311, 490)
                self.operate([110, 487])
                self.game_over()
            self.mouse.click_element(30, 257, times=0.5)
            self.screen.find_ele_picture('yitiao\\dayanta\\6_2', 'mouse', 175, 344)
            time.sleep(3)

        # 第七个
        if num >= 7:
            self.screen.find_ele_picture(file_path='system\\zidong_', handle='self')
            self.keyboard.press_shortcut_key('alt', '1')
            self.mouse.click_element(441, 452, times=0.5)
            self.keyboard.press_shortcut_key('alt', '1')
            time.sleep(2)
            self.keyboard.press_shortcut_key('alt', '5')
            self.mouse.click_element(326, 455, times=0.5)
            self.make_sure_wuyi()
            self.mouse.click_element(156, 240, times=0.5)
            self.screen.find_ele_picture('yitiao\\dayanta\\7', 'mouse', 180, 345)
            time.sleep(1)
            self.mouse.click_element(54, 240, times=0.5)
            if int(level[3]) is 0:
                self.mouse.click_element(111, 240, times=0.5)
                self.screen.find_ele_picture('yitiao\\dayanta\\7_1', 'mouse', 182, 329)
                self.operate([250, 464])
            elif int(level[3]) is 1:
                self.mouse.click_element(155, 255, times=0.5)
                self.screen.find_ele_picture('yitiao\\dayanta\\7_2', 'mouse', 182, 325)
                self.mouse.click_element(311, 490)
                self.operate([295, 354])
            self.game_over()
            time.sleep(1)
            self.mouse.click_element(85, 243, times=0.5)
            self.screen.find_ele_picture('yitiao\\dayanta\\7_3', 'mouse', 192, 330)
            time.sleep(3)







