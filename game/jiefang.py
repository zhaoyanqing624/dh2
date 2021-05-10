import time
from system.transform import TransForm
from game.common import Common
from system.keyboard import KeyBoard
from system.screen import Screen
from system.mouse import Mouse


class JieFang:
    def __init__(self):
        self.transform = TransForm()
        self.common = Common()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.mouse = Mouse()

    def task_start(self):
        self.common.get_focus()
        for i in range(5):
            self.find_npc()
            # 种植物
            # self.zhong_flowers(type=3)
            self.find_flowers()
            self.common.change_teamer()

    def find_npc(self):
        self.keyboard.press_shortcut_key('alt', '2')
        self.mouse.click_element(499, 419)
        self.mouse.click_element(312, 362)
        self.screen.find_ele_picture('game\\jiefang\\5', 'mouse', 165, 345)

    def zhong_flowers(self, type= 1):
        self.keyboard.press_shortcut_key('alt', '1')
        self.mouse.click_element(396, 371)
        self.mouse.click_element(396, 371)
        self.screen.find_ele_picture('game\\jiefang\\4', 'mouse', 160, 372)
        self.mouse.click_element(396, 371)
        self.mouse.click_element(396, 371)
        self.screen.find_ele_picture('game\\jiefang\\4', 'mouse', 160, 352)
        if type is 1:
            self.mouse.click_element(432, 220)
        elif type is 2:
            self.mouse.click_element(536, 273)
        elif type is 3:
            self.mouse.click_element(433, 322)
        self.mouse.click_element(533, 485)
        self.mouse.click_element(413, 535, times=1, right=True)

    def find_flowers(self):
        # 点击领取街坊任务（花）
        self.mouse.click_element(757, 181)
        self.mouse.click_element(408, 354)
        self.mouse.click_element(182, 330)
        time.sleep(1)
        # for y_ in range(14):
        self.mouse.click_element(92, 227)
        flower_num = 0
        for y in range(30):
            if y < 13:
                self.mouse.click_element(240, 235 + 20 * y)
            if y > 13:
                self.mouse.mouse_scroll(-10)
                time.sleep(0.5)
                self.mouse.click_element(240, 235 + 20 * 12)
            list = [[543, 307], [481, 334], [422, 366],
                    [480, 396], [541, 427], [597, 395],
                    [657, 362], [598, 332]]
            list_flower = [[556, 267], [483, 294], [426, 328],
                           [488, 365], [545, 398], [602, 360],
                           [672, 329], [617, 295]]
            time.sleep(1)
            self.screen.cut_screen()
            time.sleep(1.5)
            for index, j in enumerate(list_flower):
                index = index
                result = self.screen.find_color_ele(j[0], j[1], 30, 15, 190, 210, 10, 40, 0, 20)
                if result != None:
                    self.mouse.click_element(list[index][0], list[index][1])
                    self.mouse.click_element(167, 327)
                    for w in range(6):
                        self.mouse.click_element_right(219, 250, 1)
                        time.sleep(3)
                        while True:
                            time.sleep(1)
                            self.screen.cut_screen()
                            time.sleep(2)
                            file_name = "C:\\dh2\\game\\jiefang\\3.png"
                            result = self.screen.get_location_picture(file_name, 0.8)
                            if result != 0:
                                self.mouse.click_element(result[0], result[1], times=1)
                                self.mouse.click_element(162, 361, times=1)
                                flower_num += 1
                                if flower_num >= 10:
                                    return "success"
                            else:
                                break
                    self.mouse.click_element(760, 184)
                    self.mouse.click_element(408, 350)
                    self.mouse.click_element(182, 327)


    def jiefang_task(self):
        # 清除任务栏信息
        # for i in range(10):
        #     self.mouse.click_element(356,224)
        self.screen.cut_screen_location(width=200, height=300, x=150, y=190)
        result = self.screen.get_location_picture("C:\\dh2\\game\\system\\task\\0.png", 0.7, cut_zone=True)
        self.mouse.click_element(result[0]+150, result[1]+190)



    # ie.common.get_focus()
    # for w in range(4):
    #     ie.mouse.click_element_right(219, 241, 1)
    #     time.sleep(5)
