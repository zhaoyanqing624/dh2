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
            result_ = self.screen.get_location_picture("D:\\dh2\\game\\system\\zidong.png",num=0.8)
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
        self.keyboard.press_shortcut_key('alt', '2')
        self.mouse.click_element(502, 419)
        time.sleep(2)
        self.mouse.click_element(587, 362)
        time.sleep(10)
        # 寻找NPC 185,380
        self.screen.find_ele_picture('yitiao\\guzhu\\begin')
        self.mouse.click_element(182, 328, times=0.5)
        time.sleep(2)
        self.make_sure()
        time.sleep(10)
        # 宠物医生
        self.mouse.click_element(245, 275, times=0.5)
        self.make_sure_wuyi()
        time.sleep(2)
        # 第一个
        self.mouse.click_element(93, 241, times=0.5)
        self.screen.find_ele_picture('yitiao\\guzhu\\1','mouse',169,329)
        self.operate()
        self.game_over()
        time.sleep(2)
        # 第二个
        self.mouse.click_element(93, 241, times=0.5)
        self.screen.find_ele_picture('yitiao\\guzhu\\2','mouse',169,329)
        self.operate()
        self.game_over()
        time.sleep(2)
        # 第三个
        self.mouse.click_element(93, 241, times=0.5)
        self.screen.find_ele_picture('yitiao\\guzhu\\3','mouse',169,329)
        self.operate()
        self.game_over()
        time.sleep(2)
        # 第四个
        self.mouse.click_element(93, 241, times=0.5)
        self.screen.find_ele_picture('yitiao\\guzhu\\4','mouse',169,329)
        self.operate()
        self.game_over()
        time.sleep(2)
        # 第五个
        self.mouse.click_element(93, 241, times=0.5)
        self.screen.find_ele_picture('yitiao\\guzhu\\5','mouse',169,329)
        self.operate()
        self.game_over()
        time.sleep(2)
        # 第六个
        self.mouse.click_element(93, 241, times=0.5)
        self.screen.find_ele_picture('yitiao\\guzhu\\6','mouse',175,347)
        self.make_sure()
        time.sleep(2)
        self.keyboard.press_shortcut_key('alt', '1')
        # 第七个
        self.mouse.click_element(93, 241, times=0.5)
        self.screen.find_ele_picture('yitiao\\guzhu\\7','mouse',188,328)
        # self.make_sure()
        self.operate()
        self.game_over()
        time.sleep(2)
        # 第八个
        self.mouse.click_element(93, 241, times=0.5)
        self.screen.find_ele_picture('yitiao\\guzhu\\8','mouse',188,328)
        # self.make_sure()
        self.operate()
        self.game_over()
        time.sleep(15)








if __name__ == '__main__':
#     0简单 1难
    GuZhu().start_task()


