import time
from system.transform import TransForm
from game.common import Common
from system.keyboard import KeyBoard
from system.screen import Screen
from system.mouse import Mouse
from game.walking import Walking

class BangPai:
    def __init__(self):
        self.transform = TransForm()
        self.common = Common()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.mouse = Mouse()
        self.walking = Walking()
    def find_bangpai_task(self):
        for j in range(10):
            if j == 0:
                # 寻找NPC
                self.common.clear_task()
                self.screen.cut_screen()
                result_task = self.screen.get_location_picture('E:\\dh2\\game\\system\\task\\1.png')
                self.mouse.click_element(result_task[0] + 50, result_task[1], 0.7)

                self.screen.cut_screen()
                result_task_bangpai = self.screen.get_location_picture('E:\\dh2\\game\\system\\task\\2.png')
                self.mouse.click_element(result_task_bangpai[0] + 50, result_task_bangpai[1], 0.7)
                self.mouse.click_element(428, 240)
                time.sleep(5)
                # 领取任务
                self.screen.find_ele_picture('game\\bangpai\\0', 'mouse', 223, 329)
                self.mouse.click_element(163, 350)
            else:
                self.mouse.click_element(461, 288)
                # 领取任务
                self.screen.find_ele_picture('game\\bangpai\\0', 'mouse', 223, 329)
                self.mouse.click_element(163, 350)
                self.keyboard.press_shortcut_key('alt', 'q')
            self.screen.cut_screen_location(267, 136, 373, 209)
            for i in range(1, 10):
                print(i)
                file_name = "E:\\dh2\\game\\bangpai\\" + str(i) + ".png"
                result = self.screen.get_location_picture(file_name, 0.6, True)
                if result != 0:
                    if i == 1:
                        print("除草")
                        self.keyboard.press_shortcut_key('alt', 'q')
                        for j in range(5):
                            self.mouse.click_element_right(10, 582)
                            time.sleep(1)
                            self.mouse.click_element(787, 539)
                        self.return_bangpai_npc()
                    elif i == 2:
                        print("武官")
                        self.mouse.click_element(464, 240)
                        self.keyboard.press_shortcut_key('alt', 'q')
                        time.sleep(25)
                        self.screen.find_ele_picture('game\\bangpai\\2_1', 'mouse', 193, 327)
                        self.keyboard.press_shortcut_key('alt', 'q')
                        self.mouse.click_element(506, 241)
                        self.keyboard.press_shortcut_key('alt', 'q')
                        time.sleep(20)
                        self.screen.find_ele_picture('game\\bangpai\\2_2', 'mouse', 193, 327)
                        self.return_bangpai_npc()
                    elif i == 3:
                        print("订酒")
                        self.mouse.click_element(448, 240)
                        self.keyboard.press_shortcut_key('alt', 'q')
                        time.sleep(10)
                        self.screen.find_ele_picture('game\\bangpai\\3_1', 'mouse', 182, 345)
                        self.mouse.click_element(182, 345)
                        self.return_bangpai_npc()
                    elif i == 4:
                        print("药")
                        self.keyboard.press_shortcut_key('alt', 'q')
                        self.mouse.click_element(461, 288)
                        self.mouse.click_element(201, 328)
                        time.sleep(3)
                        self.mouse.click_element(201, 328)
                    elif i == 5:
                        print("无名侠女")
                        self.mouse.click_element(500, 240)
                        self.keyboard.press_shortcut_key('alt', 'q')
                        time.sleep(5)
                        self.screen.find_ele_picture('game\\bangpai\\5_1', 'keyboard', 'alt', '8')
                        self.screen.find_ele_picture('game\\bangpai\\5_2', 'mouse', 182, 345)
                        self.return_bangpai_npc()
                    elif i == 6:
                        print("回答问题")
                        self.mouse.click_element(445, 240)
                        self.keyboard.press_shortcut_key('alt', 'q')
                        self.mouse.click_element(185, 327)
                        while True:
                            self.mouse.click_element(159, 329)
                            time.sleep(1)
                            self.screen.cut_screen()
                            result_answer = self.screen.get_location_picture("E:\\dh2\\game\\bangpai\\6_1.png", 0.8)
                            if result_answer == 0:
                                break
                        self.mouse.click_element(461, 288)
                        self.mouse.click_element(201, 328)
                        time.sleep(3)
                        self.mouse.click_element(201, 328)
                    elif i == 7:
                        print("帮派宣传")
                        self.mouse.click_element(410, 240)
                        self.keyboard.press_shortcut_key('alt', 'q')
                        time.sleep(10)
                        while True:
                            if self.walking.iswalking() is 0:
                                self.mouse.click_element(784, 540)
                                break
                        self.return_bangpai_npc()

                    elif i == 8:
                        print("作乱妖怪")
                        self.mouse.click_element(440, 240)
                        self.keyboard.press_shortcut_key('alt', 'q')
                        self.screen.find_ele_picture('game\\system\\zidong', 'keyboard', 'alt', '8')
                        self.screen.find_ele_picture('game\\bangpai\\8_1', 'mouse', 182, 345)
                        self.return_bangpai_npc()
                    elif i==9:
                        print("收银票")
                        self.mouse.click_element(455, 240)
                        self.keyboard.press_shortcut_key('alt', 'q')
                        self.screen.find_ele_picture('game\\bangpai\\9_1', 'mouse', 182, 345)
                        self.return_bangpai_npc()
                    else:
                        print("找不到")

    def return_bangpai_npc(self):
        self.keyboard.press_shortcut_key('alt', 'q')
        self.mouse.click_element(517, 239)
        self.keyboard.press_shortcut_key('alt', 'q')
        time.sleep(5)
        self.screen.find_ele_picture('game\\bangpai\\0_1', 'mouse', 193, 327)
        self.mouse.click_element(193, 327)
        time.sleep(3)
        self.mouse.click_element(460, 290)

    def bangpai_start(self):
        self.common.get_focus()
        for i in range(5):
            self.common.capation_eat_xiang()
            self.find_bangpai_task()
            self.common.change_teamer()

if __name__ == '__main__':
    BangPai().bangpai_start()