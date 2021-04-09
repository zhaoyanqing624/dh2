import time
from game.common import Common
from system.transform import TransForm
from system.keyboard import KeyBoard
from system.screen import Screen
from system.mouse import Mouse
import pyautogui

class ShiMen():
    def __init__(self):
        self.transform = TransForm()
        self.common = Common()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.mouse = Mouse()
        self.task_list = [0, 0, 0, 0, 0]
        self.offset_task = [0, 0, 0, 0, -15]
        self.fight_list = [0, 0, 0, 0, 0]

    def task_start(self):
        print("任务开始")
        self.common.get_focus()
        # 切换宝宝
        # for i in range(5):
        #     self.common.change_dog(2)
        #     time.sleep(1)
        #     self.common.change_teamer(times=0.3)
        for i in range(10):
            print("------第"+str(i+1)+"轮------")
            if i is 0:
                for j in range(5):
                    self.find_npc(i)
                    self.common.change_teamer(times=0.5)
            for j in range(5):
                self.get_task(j)
                self.common.change_teamer(times=0.5)
            for j in range(5):
                self.return_task(self.task_list[j])
                self.common.change_teamer(times=0.5)
            for j in range(5):
                self.give_task(cicle=i, i=self.offset_task[j], j=self.task_list[j])
                self.common.change_teamer(times=0.5)

    # 寻找NPC
    def find_npc(self, order):
        if order is 0:
            for i in range(10):
                self.keyboard.press_shortcut_key('alt', 'q')
                time.sleep(0.5)
        self.mouse.click_element(63, 106, times=1)
        time.sleep(1)
        if order is 0:
            for i in range(7):
                self.mouse.click_element(484, 250)
        while True:
            result = self.screen.find_ele_picture_time(file_path='game\\shimen\\1', handle='self', location_=[485, 550, 5])
            if result is True:
                self.mouse.click_element(582, 294, times=1)
                self.mouse.click_element(63, 106, times=1)
                break

    # 获取任务
    def get_task(self, i):
        result = self.screen.find_ele_picture_time(file_path='game\\shimen\\1_1_0', date_time=40, handle='mouse', k1=165, k2=363+self.offset_task[i])
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
        for i in range(2, 11):
            file_name = "C:\\dh2\\game\\shimen\\" + str(i) + ".png"
            result = self.screen.get_location_picture(file_name, 0.7)
            if result != 0:
                if i == 2:
                    print("风水混元丹")
                    self.keyboard.press_shortcut_key('alt', 'q')
                    self.mouse.click_element(170, 350, times=1)
                    self.mouse.click_element(206, 135, times=1, right=True)
                    self.mouse.click_element(206, 135, times=1, right=True)
                    return i

                elif i == 3:
                    print("顶天柱")
                    self.mouse.click_element(434, 237)
                    time.sleep(0.5)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    return i

                elif i == 4:
                    print("密探")
                    self.mouse.click_element(593, 239)
                    time.sleep(0.5)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    self.screen.find_ele_picture('game\\shimen\\4_1', 'mouse', 207, 329)
                    time.sleep(2)
                    if self.fight_list[cicle] is 0:
                        self.common.find_attack('f5')
                        self.keyboard.press_shortcut_key('alt', 'a')
                        self.fight_list[cicle] = 1
                    self.keyboard.press_shortcut_key('alt', '8')
                    self.mouse.click_element(206, 135, times=1, right=True)
                    return i

                elif i == 10:
                    print("切磋")
                    self.mouse.click_element(388, 256)
                    time.sleep(0.5)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    self.screen.find_ele_picture('game\\shimen\\10_1', 'mouse', 207, 329)
                    time.sleep(2)
                    if self.fight_list[cicle] is 0:
                        self.common.find_attack('f5')
                        self.keyboard.press_shortcut_key('alt', 'a')
                        self.fight_list[cicle] = 1
                    self.keyboard.press_shortcut_key('alt', '8')
                    self.mouse.click_element(206, 135, times=1, right=True)
                    return i
        return 0

    # 返回师门
    def return_task(self, i):
        if i is 4 or i is 10:
            self.mouse.click_element(170, 350, times=0.5)
        elif i is 3:
            self.mouse.click_element(162, 330, times=0.5)
            self.mouse.click_element(170, 350, times=0.5)
            self.mouse.click_element(170, 350, times=0.5)
            self.mouse.click_element(170, 350, times=0.5)
        self.mouse.click_element(206, 135, times=0.5, right=True)
        self.mouse.click_direct_element(63, 106)
        time.sleep(2)
        self.mouse.click_element(582, 294, times=0.5)
        self.mouse.click_direct_element(63, 106)

    # 交付师门
    def give_task(self, cicle, i, j):
        result = self.screen.find_ele_picture_time(file_path='game\\shimen\\1_2', date_time=30, handle='mouse', k1=172, k2=360 + i)
        if result is False:
            self.find_npc(order=1)
        if j is 2:
            self.mouse.click_element(170, 350, times=0.5)
            self.mouse.click_element(170, 350, times=0.5)
        if cicle is not 9:
            self.mouse.click_element(63, 106, times=0.5)
            time.sleep(2)
            self.mouse.click_element(582, 294, times=0.5)
            self.mouse.click_direct_element(63, 106)



















# if __name__ == '__main__':
#     ShiMen().task_start()
    # print(list)


