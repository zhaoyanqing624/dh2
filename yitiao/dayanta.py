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
        self.common.get_focus()
        for i in range(3):
            self.mouse.click_element(311, 490)
            self.common.change_teamer()
        self.common.get_focus()
    def make_sure_wuyi(self):
        for i in range(3):
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
    def operate(self):
        result_ = self.screen.find_ele_picture_time('game\\system\\zidong')
        if result_ is True:
            for i in range(3):
                self.keyboard.press_shortcut_key('alt', '8')
                if i is not 2:
                    self.common.change_teamer()
        self.common.get_focus()

    def start_task(self):
        self.common.get_focus()
        self.keyboard.press_shortcut_key('alt', '1')
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
        self.screen.find_ele_picture('yitiao\\dayanta\\1','mouse',180,361)
        self.mouse.click_element(91, 240, times=0.5)
        self.screen.find_ele_picture('yitiao\\dayanta\\1_2', 'mouse', 169, 339)
        self.operate()
        self.game_over()
        self.mouse.click_element(30, 257, times=0.5)
        self.screen.find_ele_picture('yitiao\\dayanta\\1_3', 'mouse', 175, 344)
        time.sleep(3)
        # 第二个
        self.mouse.click_element(30, 257, times=0.5)
        self.screen.find_ele_picture('yitiao\\dayanta\\2','mouse',180,361)
        time.sleep(1)
        pyautogui.click()
        self.mouse.click_element(78, 240, times=0.5)
        time.sleep(60)
        self.screen.cut_screen()
        time.sleep(1)
        res = self.screen.get_locations_picture("C:\\dh2\\yitiao\\dayanta\\2_1.png", 0.7)
        print(res)
        self.mouse.click_element(res[0]['result'][0], res[0]['result'][1])
        time.sleep(1)
        self.mouse.click_element(91,241, times=0.5)
        time.sleep(1)
        self.mouse.click_element(173, 327, times=0.5)
        self.operate()
        self.game_over()
        self.mouse.click_element(30, 257, times=0.5)
        self.screen.find_ele_picture('yitiao\\dayanta\\2_2', 'mouse', 183, 325)
        time.sleep(3)
        # 第三个
        self.mouse.click_element(30, 257, times=0.5)
        self.screen.find_ele_picture('yitiao\\dayanta\\3','mouse',180,413)
        self.mouse.click_element(91, 240, times=0.5)
        self.operate()
        self.game_over()
        self.mouse.click_element(30, 257, times=0.5)
        self.screen.find_ele_picture('yitiao\\dayanta\\3_1', 'mouse', 175, 344)
        time.sleep(3)
        # 第四个
        self.mouse.click_element(30, 257, times=0.5)
        self.screen.find_ele_picture('yitiao\\dayanta\\4','mouse',180,361)
        time.sleep(1)
        pyautogui.click()
        while True:
            time.sleep(4)
            self.mouse.click_element(41, 240, times=0.5)
            time.sleep(1)
            self.screen.cut_screen()
            time.sleep(1)
            location = self.screen.get_locations_picture("C:\\dh2\\yitiao\\dayanta\\4_1.png", 0.9)
            if len(location) is not 0:
                self.mouse.click_element(178, 365, times=0.5)
                break
        self.make_sure()
        self.operate()
        self.game_over()
        while True:
            time.sleep(4)
            self.mouse.click_element(33, 255, times=0.5)
            time.sleep(1)
            self.screen.cut_screen()
            time.sleep(1)
            location = self.screen.get_locations_picture("C:\\dh2\\yitiao\\dayanta\\4_2.png", 0.7)
            if len(location) is not 0:
                self.mouse.click_element(183, 343, times=0.5)
                break
        time.sleep(3)
        # 第五个
        self.mouse.click_element(30, 257, times=0.5)
        self.screen.find_ele_picture('yitiao\\dayanta\\5','mouse',180,344)
        time.sleep(1)
        pyautogui.click()
        while True:
            time.sleep(4)
            self.mouse.click_element(150, 240, times=0.5)
            time.sleep(1)
            self.screen.cut_screen()
            time.sleep(1)
            location = self.screen.get_locations_picture("C:\\dh2\\yitiao\\dayanta\\5_1.png", 0.7)
            if len(location) is not 0:
                self.mouse.click_element(178, 365, times=0.5)
                break
        self.make_sure()
        self.operate()
        self.game_over()
        while True:
            time.sleep(4)
            self.mouse.click_element(33, 255, times=0.5)
            time.sleep(1)
            self.screen.cut_screen()
            time.sleep(1)
            location = self.screen.get_locations_picture("C:\\dh2\\yitiao\\dayanta\\5_2.png", 0.7)
            if len(location) is not 0:
                self.mouse.click_element(190, 365, times=0.5)
                break
        time.sleep(3)
        # 第六个
        self.mouse.click_element(30, 257, times=0.5)
        self.screen.find_ele_picture('yitiao\\dayanta\\6','mouse',180,381)
        time.sleep(1)
        pyautogui.click()
        self.mouse.click_element(41, 240, times=0.5)
        self.screen.find_ele_picture('yitiao\\dayanta\\6_1', 'mouse', 182, 353)
        self.make_sure()
        self.operate()
        self.game_over()
        self.mouse.click_element(30, 257, times=0.5)
        self.screen.find_ele_picture('yitiao\\dayanta\\6_2', 'mouse', 175, 344)
        time.sleep(3)
        # 第七个
        self.mouse.click_element(156, 240, times=0.5)
        self.screen.find_ele_picture('yitiao\\dayanta\\7','mouse',180,345)
        time.sleep(1)
        self.mouse.click_element(54, 240, times=0.5)
        time.sleep(1)
        self.mouse.click_element(461, 292, times=0.5)
        self.screen.find_ele_picture('yitiao\\dayanta\\7_1', 'mouse', 182, 329)
        self.operate()
        self.game_over()
        self.mouse.click_element(85, 243, times=0.5)
        self.screen.find_ele_picture('yitiao\\dayanta\\7_2', 'mouse', 192, 330)
        self.keyboard.press_shortcut_key('alt', 'q')
        time.sleep(3)









if __name__ == '__main__':
#     0简单 1难
    DaYanTa().start_task()


