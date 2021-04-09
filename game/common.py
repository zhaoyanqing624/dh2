import pyautogui
from system.mouse import Mouse
from system.transform import TransForm
from system.keyboard import KeyBoard
from system.screen import Screen
from game.walking import Walking
import time


class Common:
    def __init__(self):
        self.personList = [75, 250, 400, 545, 700]
        self.mouse = Mouse()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.transform = TransForm()

    def get_focus(self,index=True):
        if index is True:
            self.mouse.click_direct_element(self.transform.trans_location(75, 0), self.transform.trans_location(45, 1))
        else:
            self.mouse.click_direct_element(self.transform.trans_location(700, 0), self.transform.trans_location(45, 1))

    def create_team(self):
        # 创建队伍
        self.keyboard.press_shortcut_key('alt', 't', 1)
        self.mouse.click_element(403, 318)
        # 打开好友列表查看组队信息
        self.keyboard.press_shortcut_key('alt', 'f', 1)
        time.sleep(0.5)

        self.screen.cut_screen()
        result = self.screen.find_color_ele(679, 291)
        if result != None:
            self.mouse.click_element(result[0], result[1])
        list = [315, 345, 375, 405]
        for i in list:
            self.mouse.click_element_right(730, i, 1)
            self.mouse.click_element(388, 505)
        self.mouse.click_element_right(388, 530, 1)
        self.keyboard.press_shortcut_key('alt', 'f', 1)

        for i in range(4):
            self.keyboard.press_shortcut_key('ctrl', 'tab', 1)
            self.mouse.click_element(347, 410)
        self.keyboard.press_shortcut_key('ctrl', 'tab', 1)

    def change_teamer(self,times = 1):
        self.keyboard.press_shortcut_key('ctrl', 'tab', times)

    def change_dog(self, num):
        self.keyboard.press_shortcut_key('alt', 'o')
        if num == 1:
            self.mouse.click_element(90, 186)
        elif num == 2:
            self.mouse.click_element(90, 208)
        elif num == 3:
            self.mouse.click_element(90, 230)
        elif num == 4:
            self.mouse.click_element(90, 252)
        elif num == 5:
            self.mouse.click_element(90, 274)
        elif num == 6:
            self.mouse.click_element(90, 296)
        time.sleep(1.5)
        self.screen.cut_screen_location(width=200, height=50, x=200, y=350)
        time.sleep(1)
        result = self.screen.get_location_picture("C:\\dh2\\game\\system\\0.png", 0.9, cut_zone=True)
        if result == 0:
            self.mouse.click_element(320, 380)
        self.keyboard.press_shortcut_key('alt', 'o')

    def clear_task(self):
        # 清除任务列表
        # self.keyboard.press_shortcut_key('alt', 'q')
        # for i in range(5):
        #     self.mouse.click_element(359, 223)
        # list = [27, 46, 65, 85, 103, 122, 141]
        # for i in list:
        #     time.sleep(1)
        #     self.screen.cut_screen_location(width=200, height=300, x=150, y=190)
        #     result = self.screen.find_color_ele(11, i, 2, 1, 190, 220, 60, 75, 50, 60, True)
        #     print(result)
        #     if result == None:
        #         self.mouse.click_element(11 + 200, i + 190)
        self.keyboard.press_shortcut_key('alt', '2')
        time.sleep(1)
        self.mouse.click_element(507, 419)
        time.sleep(1)
        self.mouse.click_element(310, 381)
        self.screen.find_ele_picture('game\\bangpai\\0_', 'mouse', 220, 328)
        time.sleep(2)
        self.keyboard.press_shortcut_key('alt', '1')
        time.sleep(1)
        self.mouse.click_element(500, 313)

    def iswalking(self):
        self.screen.cut_screen_by_PIL(30, 65, 140, 85, "C:\\dh2\\system\\2.PNG")
        time.sleep(2)
        self.screen.cut_screen_by_PIL(30, 65, 140, 85, "C:\\dh2\\system\\2_.PNG")
        result = Walking().iswalking()
        if result < 10:
            return False
        else:
            return True

    def capation_eat_xiang(self):
        KeyBoard().press_shortcut_key('alt', 'e')
        Mouse().click_element(344, 397)
        Mouse().click_element(44, 454, right=True)
        KeyBoard().press_shortcut_key('alt', 'e')

    def score_for_shifu(self):
        Screen().cut_screen()
        result = Screen().get_location_picture("C:\\dh2\\game\\system\\3.PNG")
        if result is not 0:
            Mouse().click_element(222, 264)
            Mouse().click_element(409, 506)

    # 创建队伍
    def create_team(self):
        self.keyboard.press_shortcut_key('alt', '5')
        self.keyboard.press_shortcut_key('alt', 't')
        self.mouse.click_element(415, 306, times=0.5)
        self.keyboard.press_shortcut_key('alt', 'f')
        self.mouse.click_element(701, 312, times=0.5)
        self.mouse.click_element(715, 338, times=0.5, right=True)
        self.screen.find_ele_picture('game\\bidou\\2', 'mouse', 387, 504)
        self.mouse.click_element(414, 531, times=0.5, right=True)

        self.mouse.click_element(701, 290, times=0.5)
        for i in range(3):
            self.mouse.click_element(715, 320+25*i, times=0.5, right=True)
            self.screen.find_ele_picture('game\\bidou\\2', 'mouse', 387, 504)
            self.mouse.click_element(414, 531, times=0.5, right=True)
        self.keyboard.press_shortcut_key('alt', 'f')

        for i in range(5):
            self.mouse.click_element(347, 415, times=0.5)
            time.sleep(1)
            self.common.change_teamer(times=0.3)

    # 寻找共计目标
    def find_attack(self, type, str='zidong', x_pos= 200, y_pos =360):
        list_ = [[x_pos, y_pos], [x_pos, y_pos-40], [x_pos, y_pos-80]]
        endtime = time.time() + int(1000)
        while time.time() < endtime:
            self.screen.cut_screen()
            time.sleep(1)
            pos_zidong = self.screen.get_location_picture("C:\\dh2\\game\\system\\"+str+".png")
            if pos_zidong is not 0:
                if type is 'f5' or type is 'f6' or type is 'f7':
                    self.keyboard.press_key(type)
                    for i in list_:
                        self.mouse.click_direct_element(i[0], i[1])
                        self.screen.cut_screen()
                        time.sleep(1)
                        pos_zidong = self.screen.get_location_picture("C:\\dh2\\game\\system\\"+str+".png")
                        if pos_zidong is not 0:
                            return i
                else:
                    for i in list_:
                        self.keyboard.press_shortcut_key('alt', 's')
                        time.sleep(0.5)
                        self.mouse.click_direct_element(i[0], i[1])
                        self.screen.cut_screen()
                        time.sleep(1)
                        pos_zidong = self.screen.get_location_picture("C:\\dh2\\game\\system\\"+str+".png")
                        if pos_zidong is not 0:
                            return i
        return 'failed'

    def game_over(self):
        endtime = time.time() + int(100)
        while time.time() < endtime:
            time.sleep(1)
            self.screen.cut_screen()
            time.sleep(1.5)
            result = self.screen.get_location_picture("C:\\dh2\\game\\system\\zidong.png", num=0.8)
            if result is 0:
                return True
        return False

    # 补充酒店老板+巫医
    def go_jiudian_wuyi(self, jiudian=None, wuyi=None):
        self.get_focus()
        for i in range(5):
            if i is 0:
                self.keyboard.press_shortcut_key('alt', '1')
                time.sleep(0.5)
            # jiudian laoban
            if jiudian is not None:
                if i is 0:
                    self.mouse.click_element(502, 430)
                self.screen.find_ele_picture('game\\system\\jiudian', 'mouse', 184, 328)
                self.mouse.click_element(184, 328)
            # wuyi
            if wuyi is not None:
                if i is 0:
                    self.mouse.click_element(293, 410)
                self.screen.find_ele_picture('game\\system\\wuyi', 'mouse', 188, 344)
            if i is 0:
                self.keyboard.press_shortcut_key('alt', '1')
            self.change_teamer()

    # 自动开始
    def begin_zidong(self):
        for i in range(5):
            if i is 0:
                self.keyboard.press_shortcut_key('alt', '2')
                self.mouse.click_element(577, 457, times=0.5)
                self.mouse.click_element(246, 247, times=0.5)
                self.screen.find_ele_picture('game\\system\\changandong', 'mouse', 634, 222)
                j = 0
                while True:
                    time.sleep(1)
                    self.screen.cut_screen()
                    time.sleep(1)
                    result = self.screen.get_location_picture("C:\\dh2\\game\\system\\zidong.png", num=0.8)
                    if result is 0:
                        if (j % 2) == 0:
                            self.mouse.click_element(634, 222, times=1, right=True)
                        else:
                            self.mouse.click_element(215, 442, times=1, right=True)
                    else:
                        self.find_attack(type='f5')
                        break
                    j += 1
            else:
                self.keyboard.press_shortcut_key('alt', '2')
                self.mouse.click_element(503, 419, times=0.5)
                self.mouse.click_element(428, 376, times=0.5)

            self.change_teamer()
            
    # 喝药
    def heyao(self):
        self.mouse.click_element(583, 78, times=0.5, right=True)
        self.mouse.click_element(267, 554, times=0.5, right=True)
        self.mouse.click_element(230, 560, times=0.5, right=True)
        pyautogui.rightClick()

