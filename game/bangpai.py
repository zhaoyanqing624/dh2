import time
from game.common import Common
from system.transform import TransForm
from system.keyboard import KeyBoard
from system.screen import Screen
from system.mouse import Mouse
import pyautogui

class BangPai():
    def __init__(self):
        self.transform = TransForm()
        self.common = Common()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.mouse = Mouse()
        self.task_list = [0, 0, 0, 0, 0]
        self.offset_task = [0, 0, 0, 0, -15]
        self.xiang_list = [0, 0, 0, 0, 0]
        # x:50 y:50 (560, 190) (560, 230) (560, 270)
        self.yao_list = [[310, 200]]

    def task_start(self):
        print("任务开始")
        self.common.get_focus()
        for i in range(10):
            print("------第"+str(i+1)+"轮------")
            if i is 0:
                for j in range(5):
                    self.keyboard.press_shortcut_key('alt', 'q')
                    time.sleep(1)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    self.find_npc(i)
                    self.common.change_teamer(times=0.5)
            for j in range(5):
                self.get_task(j)
                self.common.change_teamer(times=0.5)
            for j in range(5):
                self.return_task(self.task_list[j])
                self.common.change_teamer(times=0.5)
            for j in range(5):
                self.give_task()
                self.common.change_teamer(times=0.5)

    # 寻找NPC
    def find_npc(self, order):
        self.mouse.click_element(206, 135, times=0.5, right=True)
        self.mouse.click_element(63, 106, times=1)
        time.sleep(1)
        if order is 0:
            for i in range(35):
                self.mouse.click_element(484, 250)
        while True:
            result = self.screen.find_ele_picture_time(file_path='game\\bangpai\\0', handle='self', location_=[485, 550, 5])
            if result is True:
                self.mouse.click_element(635, 355, times=1)
                self.mouse.click_element(63, 106, times=1)
                break

    # 获取任务
    def get_task(self, i):
        result = self.screen.find_ele_picture_time(file_path='game\\bangpai\\0_1', date_time=40, handle='mouse', k1=175, k2=327)
        if result is False:
            self.find_npc(order=1)
        self.keyboard.press_shortcut_key('alt', 'q')
        task_result = self.task_classify(cicle=i)
        self.task_list[i] = task_result

    # 任务种类
    def task_classify(self, cicle):
        time.sleep(1)
        self.screen.cut_screen()
        time.sleep(1.5)
        for i in range(1, 11):
            file_name = "C:\\dh2\\game\\bangpai\\" + str(i) + ".png"
            result = self.screen.get_location_picture(file_name, 0.8)
            if result != 0:
                if i == 1:
                    print("除草")
                    self.keyboard.press_shortcut_key('alt', 'q')
                    self.mouse.click_element(170, 350, times=1)
                    self.mouse.click_element(206, 135, times=1, right=True)
                    self.mouse.click_element(206, 135, times=1, right=True)
                    self.screen.cut_screen()
                    time.sleep(1)
                    location = self.screen.get_location_picture('C:\\dh2\\game\\bangpai\\1_1.png', 0.8)
                    for j in range(5):
                        self.mouse.click_element_right(116, 530)
                        time.sleep(1)
                        self.mouse.click_element(location[0], location[1])
                    return i

                elif i == 2:
                    print("武官")
                    self.mouse.click_element(450, 237)
                    time.sleep(0.5)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    if self.xiang_list[cicle] is 0:
                        self.common.capation_eat_xiang()
                        self.xiang_list[cicle] = 1
                    return i

                elif i == 3:
                    print("定酒")
                    self.mouse.click_element(423, 239)
                    time.sleep(0.5)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    return i

                elif i == 4:
                    print("药")
                    self.keyboard.press_shortcut_key('alt', 'q')
                    self.keyboard.press_shortcut_key('alt', 'b')
                    self.mouse.click_element(655, 565, times=1)
                    for j in range(1, 13):
                        file_name = "C:\\dh2\\game\\bangpai\\4_" + str(j) + ".png"
                        yao_result = self.screen.get_location_picture(file_name, 0.9)
                        if yao_result != 0:
                            if j <= 4:
                                self.mouse.click_element(310 + cicle * 50, 200 + (j-1) * 50, times=1)
                            elif 4 < j <= 8:
                                self.mouse.click_element(560, 230, times=1)
                                self.mouse.click_element(310 + cicle * 50, 200 + (j-5) * 50, times=1)
                            elif 8 < j <= 12:
                                self.mouse.click_element(560, 270, times=1)
                                self.mouse.click_element(310 + cicle * 50, 200 + (j-9) * 50, times=1)

                    self.mouse.click_element(537, 495, times=1)
                    self.keyboard.press_shortcut_key('alt', 'b')
                    self.mouse.click_element(401, 145, times=1, right=True)
                    self.mouse.click_element(206, 135, times=1, right=True)
                    return i

                elif i == 5:
                    print("无名侠女")
                    self.mouse.click_element(500, 240)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    return i

                elif i == 6:
                    print("回答问题")
                    self.mouse.click_element(424, 238)
                    time.sleep(0.5)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    return i

                elif i == 7:
                    print("帮派宣传")
                    self.mouse.click_element(405, 240)
                    time.sleep(0.5)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    return i

                elif i == 8:
                    print("作乱妖怪")
                    self.mouse.click_element(430, 240)
                    time.sleep(0.5)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    self.screen.find_ele_picture('game\\system\\zidong', 'keyboard', 'alt', '8')
                    return i

                elif i == 9:
                    print("收银票")
                    self.mouse.click_element(454, 239)
                    time.sleep(0.5)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    return i

                # elif i == 10:
                #     print("神秘任务")
                #     return i


    # 返回帮派管理人
    def return_task(self, i):
        if i is 2:
            self.screen.find_ele_picture('game\\bangpai\\2_1', 'mouse', 170, 350)
            self.keyboard.press_shortcut_key('alt', 'q')
            self.mouse.click_element(480, 240, times=0.5)
            self.keyboard.press_shortcut_key('alt', 'q')
            self.screen.find_ele_picture('game\\bangpai\\2_2', 'mouse', 170, 350)
            self.keyboard.press_shortcut_key('alt', '8')
            self.screen.find_ele_picture('game\\bangpai\\2_3', 'mouse', 170, 350)
        elif i is 3:
            self.screen.find_ele_picture('game\\bangpai\\3_1', 'mouse', 170, 328)
            self.mouse.click_element(170, 350, times=0.5)
            self.mouse.click_element(170, 350, times=0.5)
        elif i is 4:
            self.mouse.click_element(170, 350, times=0.5)
        elif i is 5:
            self.screen.find_ele_picture('game\\bangpai\\5_1', 'mouse', 170, 350)
        elif i is 6:
            self.screen.find_ele_picture('game\\bangpai\\6_1', 'mouse', 153, 328)
            while True:
                self.mouse.click_element(170, 328)
                time.sleep(1.5)
                self.screen.cut_screen()
                time.sleep(1)
                result_answer = self.screen.get_location_picture("C:\\dh2\\game\\bangpai\\6_1.png", 0.8)
                if result_answer == 0:
                    break
        elif i is 7:
            self.screen.find_ele_picture(file_path='game\\bangpai\\7_1', handle='self')
        elif i is 8:
            self.screen.find_ele_picture('game\\bangpai\\8_2', 'mouse', 170, 350)
        elif i is 9:
            self.mouse.click_element(170, 350, times=0.5)
            self.mouse.click_element(170, 350, times=0.5)
        self.mouse.click_element(206, 135, times=0.5, right=True)
        self.mouse.click_direct_element(63, 106)
        time.sleep(2)
        self.mouse.click_element(635, 355, times=0.5)
        self.mouse.click_direct_element(63, 106)

    # 交付任务
    def give_task(self):
        result = self.screen.find_ele_picture_time(file_path='game\\bangpai\\0_2', date_time=40, handle='mouse', k1=176, k2=325)
        if result is False:
            self.find_npc(order=1)
        self.mouse.click_element(170, 350, times=1)
        self.mouse.click_element(206, 135, times=0.5, right=True)
        self.mouse.click_element(63, 106, times=0.5)
        time.sleep(2)
        self.mouse.click_element(635, 355, times=0.5)
        self.mouse.click_direct_element(63, 106)


# if __name__ == '__main__':
#
#     Common().get_focus()
#     BangPai().task_start()
    # print(list)


