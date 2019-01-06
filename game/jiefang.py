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

    def find_flowers(self):
        # 拜访他人获得鲜花
        for i in range(1):
            flower = 0
            if i == 0:
                self.common.get_focus()
            #     else:
            #         self.common.change_teamer()
            #     self.screen.find_ele_picture('game\\jiefang\\0', handle=True, k1='alt', k2='f')
            #     # 打开好友列表查看组队信息
            #     time.sleep(0.5)
            #     self.screen.cut_screen()
            #     result = self.screen.find_color_ele(679, 291)
            #     if result != None:
            #         self.mouse.click_element(result[0], result[1])
            #     self.mouse.click_element_right(730, 315, 1)
            #     self.mouse.click_element(303, 505)
            #     self.mouse.click_element_right(388, 530, 1)
            #     self.mouse.click_element(777, 549)
            #     self.keyboard.press_shortcut_key('alt', 'f')

            # 点击领取街坊任务（花）
            self.mouse.click_element(757, 181)
            self.mouse.click_element(408, 354)
            self.mouse.click_element(182, 346)
            time.sleep(1)
            self.mouse.click_element(92, 227)
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
                self.screen.cut_screen()
                for index, j in enumerate(list_flower):
                    index = index
                    result = self.screen.find_color_ele(j[0], j[1], 10, 10, 190, 220, 10, 40, 0, 30)
                    if result != None:
                        self.mouse.click_element(list[index][0], list[index][1])
                        self.mouse.click_element(167, 327)
                        for w in range(4):
                            self.mouse.click_element_right(219, 250, 1)
                            time.sleep(5)
                            self.screen.cut_screen()
                            # a = sceen.find_color_ele(426, 328, 10, 10)
                            result = self.screen.template_image("E:\\dh2\\game\\jiefang\\1.PNG")
                            result_ = self.screen.template_image("E:\\dh2\\game\\jiefang\\1_1.PNG")
                            if len(result_)>0:
                                list_ = []
                                lists = []
                                for i in result_:
                                    list_.append(i[0] + 1)
                                for i in result:
                                    if i[0] in list_:
                                        str = i[0], i[1]
                                        list.append(str)
                                for i in lists:
                                    self.mouse.click_element(i[0], i[1])
                                    self.click_element(169, 359)
                                    time.sleep(4)

    def jiefang_task(self):
        # 清除任务栏信息
        # for i in range(10):
        #     self.mouse.click_element(356,224)
        self.screen.cut_screen_location(width=200, height=300, x=150, y=190)
        result = self.screen.get_location_picture("E:\\dh2\\game\\system\\task\\0.png", 0.7, cut_zone=True)
        self.mouse.click_element(result[0]+150, result[1]+190)

if __name__ == '__main__':
    ie = JieFang()
    ie.jiefang_task()

    # ie.common.get_focus()
    # for w in range(4):
    #     ie.mouse.click_element_right(219, 241, 1)
    #     time.sleep(5)
