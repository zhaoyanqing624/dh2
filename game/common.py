import pyautogui
from system.mouse import Mouse
from system.transform import TransForm
from system.keyboard import KeyBoard
from system.screen import Screen
import time


class Common:
    def __init__(self):
        self.personList = [75, 250, 400, 545, 700]
        self.mouse = Mouse()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.transform = TransForm()

    def get_focus(self):
        self.mouse.click_direct_element(self.transform.trans_location(75, 0), self.transform.trans_location(45, 1))

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

    def change_teamer(self):
        self.keyboard.press_shortcut_key('ctrl', 'tab', 1)

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

        self.screen.cut_screen_location(width=200, height=50, x=200, y=350)
        result = self.screen.get_location_picture("E:\\dh2\\game\\system\\0.png", 0.9, cut_zone=True)
        if result == 0:
            self.mouse.click_element(320, 380)
        self.keyboard.press_shortcut_key('alt', 'o')

    def clear_task(self):
        # 清除任务列表
        self.keyboard.press_shortcut_key('alt', 'q')
        for i in range(15):
            self.mouse.click_element(359, 223)
        list = [27, 46, 65, 85, 103, 122, 141]
        for i in list:
            time.sleep(1)
            self.screen.cut_screen_location(width=200, height=300, x=150, y=190)
            result = self.screen.find_color_ele(11, i, 2, 1, 190, 220, 60, 75, 50, 60, True)
            print(result)
            if result == None:
                self.mouse.click_element(11 + 200, i + 190)

    def iswalking(self):
        self.screen.cut_screen_by_PIL(30, 65, 140, 85, "E:\\dh2\\system\\2.PNG")
        time.sleep(2)
        self.screen.cut_screen_by_PIL(30, 65, 140, 85, "E:\\dh2\\system\\2_.PNG")



if __name__ == '__main__':
    common = Common()
    # common.get_focus()
    # time.sleep(1)
    # common.change_dog(4)
    # common.clear_task()
    common.iswalking()
