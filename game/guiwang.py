import time
from system.transform import TransForm
from game.common import Common
from system.keyboard import KeyBoard
from system.screen import Screen
from system.mouse import Mouse
import _Tools.getFighting


class GuiWang():
    def __init__(self):
        self.transform = TransForm()
        self.common = Common()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.mouse = Mouse()

    def task_start(self):
        print("任务开始")
        self.common.get_focus()
        for i in range(3):
            self.mouse.click_element(675, 366, 1, True)
            time.sleep(2.5)
        self.keyboard.press_shortcut_key('alt', '5')
        time.sleep(10)
        # 领取任务
        while True:
            print("领取任务")
            self.mouse.click_element(392, 350)
            time.sleep(1)
            self.screen.cut_screen()
            result = self.screen.get_locations_picture("E:\\dh2\\game\\guiwang\\0.png",0.9)
            if result is not 0:
                self.mouse.click_element(225, 383)
                time.sleep(0.5)
                self.mouse.click_element(180, 353)
                time.sleep(0.5)
                self.mouse.click_element(180, 353)
                result_king = self.is_ghostKing()
                if result_king is True:
                    self.mouse.click_element(392, 350)
                    time.sleep(1)
                    self.screen.cut_screen()
                    result = self.screen.get_locations_picture("E:\\dh2\\game\\guiwang\\0.png", 0.9)
                    if result is not 0:
                        self.mouse.click_element(268, 330)
                        time.sleep(1)
                        self.mouse.click_element(268, 330)
                else:
                    break
        # 返回长安 开始寻路
        print("返回长安")
        while True:
            self.mouse.click_element(392, 350)
            time.sleep(1)
            self.screen.cut_screen()
            result = self.screen.get_locations_picture("E:\\dh2\\game\\guiwang\\0.png",0.75)
            if result is not 0:
                self.mouse.click_element(268, 365)
                time.sleep(2)
                self.mouse.click_element(29, 255)
                break

        self.common.capation_eat_xiang()
        # 找到NPC,开始战斗
        print("找NPC")
        time.sleep(10)
        self.screen.find_ele_picture('game\\guiwang\\1', 'mouse', 210, 340)
        for i in range(5):
            time.sleep(2)
            self.keyboard.press_shortcut_key('alt', '8')
            self.common.change_teamer()
            self.mouse.click_element(412, 429)
        time.sleep(10)
        self.screen.find_ele_picture('game\\guiwang\\2', 'mouse', 172, 340)
        time.sleep(1)
        self.mouse.click_element(784, 539)
        time.sleep(1)
        print("回家 判断")
        self.return_home()

    def is_ghostKing(self):
        self.screen.cut_screen_by_PIL(20,265,50,300,"E:\\dh2\\system\\1.PNG")
        result = self.screen.find_color_ele(10,10,8,8,255,255,0,0,0,0,True)
        if result is not None:
            return True
        else:
            return False
    def return_home(self):
        time.sleep(1)
        self.screen.cut_screen()
        result = self.screen.get_locations_picture("E:\\dh2\\game\\guiwang\\3.png", 0.7)
        print(result)
        if len(result) is not 0:
            self.mouse.click_element(757, 455, 1, True)
            time.sleep(1.5)
            self.mouse.click_element(757, 455, 1, True)
            self.mouse.click_element(569, 450)
            self.mouse.click_element(178, 347)

if __name__ == '__main__':
    # for i in range(10000):
    #     time.sleep(3)
    #     GuiWang().mouse.click_element(315,240)
    #     time.sleep(3)
    #     GuiWang().mouse.click_element(243, 345)
    #     time.sleep(10)
    for i in range(200):
        print("执行第"+str(i+1)+"次")
        GuiWang().task_start()
        time.sleep(13)





