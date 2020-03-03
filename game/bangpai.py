import time
from system.transform import TransForm
from game.common import Common
from system.keyboard import KeyBoard
from system.screen import Screen
from system.mouse import Mouse
from game.walking import Walking
import pyautogui
class BangPai:
    def __init__(self):
        self.transform = TransForm()
        self.common = Common()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.mouse = Mouse()
        self.walking = Walking()
    def bangpai_task(self):
        self.screen.cut_screen()
        time.sleep(2)
        endtime = time.time() + int(1000)
        while time.time() < endtime:
            for i in range(1, 11):
                file_name = "D:\\dh2\\game\\bangpai\\" + str(i) + ".png"
                result = self.screen.get_location_picture(file_name, 0.8)
                if result != 0:
                    if i == 1:
                        print("除草")
                        self.keyboard.press_shortcut_key('alt', 'q')
                        self.mouse.click_element(223, 329)
                        for j in range(5):
                            self.mouse.click_element_right(10, 582)
                            time.sleep(1)
                            self.mouse.click_element(787, 539)
                        self.return_bangpai_npc()
                        return 'success'
                    elif i == 2:
                        print("武官")
                        self.keyboard.press_shortcut_key('alt', 'q')
                        self.mouse.click_element(223, 329)
                        time.sleep(1)
                        self.mouse.click_element(459, 266)
                        time.sleep(1)
                        self.mouse.click_element(181, 347)
                        time.sleep(1)
                        self.mouse.click_element(164, 344)
                        time.sleep(2)
                        pyautogui.click()
                        time.sleep(25)
                        pyautogui.moveTo(393,557,1,pyautogui.easeInQuad)
                        self.keyboard.press_shortcut_key('alt', 'q')
                        self.screen.cut_screen()
                        time.sleep(2.5)
                        loca = self.screen.get_location_picture("D:\\dh2\\game\\bangpai\\0_2.png", 0.8)
                        if loca is 0:
                            self.mouse.click_element(193, 367)
                        else:
                            self.mouse.click_element(loca[0], loca[1])
                        self.mouse.click_element(420, 239)
                        self.keyboard.press_shortcut_key('alt', '1')
                        self.keyboard.press_shortcut_key('alt', 'q')
                        return 'failed'
                    elif i == 3:
                        print("订酒")
                        self.keyboard.press_shortcut_key('alt', 'q')
                        time.sleep(1)
                        self.mouse.click_element(459, 266)
                        time.sleep(1)
                        self.mouse.click_element(181, 347)
                        time.sleep(1)
                        self.mouse.click_element(164, 344)
                        time.sleep(2)
                        pyautogui.click()
                        time.sleep(25)
                        pyautogui.moveTo(393,557,1,pyautogui.easeInQuad)
                        self.keyboard.press_shortcut_key('alt', 'q')
                        self.screen.cut_screen()
                        time.sleep(2.5)
                        loca = self.screen.get_location_picture("D:\\dh2\\game\\bangpai\\0_2.png", 0.8)
                        if loca is 0:
                            self.mouse.click_element(193, 367)
                        else:
                            self.mouse.click_element(loca[0], loca[1])
                        self.mouse.click_element(420, 239)
                        self.keyboard.press_shortcut_key('alt', '1')
                        self.keyboard.press_shortcut_key('alt', 'q')
                        return 'failed'
                    elif i == 4:
                        print("药")
                        self.keyboard.press_shortcut_key('alt', 'q')
                        self.mouse.click_element(223, 329)
                        self.mouse.click_element(461, 269)
                        self.mouse.click_element(201, 328)
                        time.sleep(3)
                        pyautogui.click()
                        self.keyboard.press_shortcut_key('alt', 'q')
                        pyautogui.moveTo(393, 557, 1, pyautogui.easeInQuad)
                        time.sleep(1)
                        self.screen.cut_screen()
                        time.sleep(2.5)
                        loca = self.screen.get_location_picture("D:\\dh2\\game\\bangpai\\0_2.png", 0.8)
                        if loca is 0:
                            self.mouse.click_element(193, 367)
                        else:
                            self.mouse.click_element(loca[0], loca[1])
                        self.mouse.click_element(420, 239)
                        self.keyboard.press_shortcut_key('alt', '1')
                        self.keyboard.press_shortcut_key('alt', 'q')
                        return 'success'
                        # time.sleep(1)
                        # self.mouse.click_element(461, 288)
                    elif i == 5:
                        print("无名侠女")
                        self.mouse.click_element(500, 240)
                        self.keyboard.press_shortcut_key('alt', 'q')
                        time.sleep(5)
                        self.screen.find_ele_picture('game\\system\\zidong', 'keyboard', 'alt', '8')
                        self.screen.find_ele_picture('game\\bangpai\\5_2', 'mouse', 182, 335)
                        self.return_bangpai_npc()
                        return 'success'
                    elif i == 6:
                        print("回答问题")
                        self.mouse.click_element(445, 240)
                        self.keyboard.press_shortcut_key('alt', 'q')
                        self.mouse.click_element(185, 327)
                        while True:
                            self.mouse.click_element(159, 329)
                            time.sleep(1)
                            self.screen.cut_screen()
                            time.sleep(2.5)
                            result_answer = self.screen.get_location_picture("D:\\dh2\\game\\bangpai\\6_1.png", 0.8)
                            if result_answer == 0:
                                break
                        self.return_bangpai_npc()
                        return 'success'
                    elif i == 7:
                        print("帮派宣传")
                        self.mouse.click_element(410, 240)
                        self.keyboard.press_shortcut_key('alt', 'q')
                        time.sleep(10)
                        endtime2 = time.time() + int(90)
                        while time.time() < endtime2:
                            if self.walking.iswalking() is 0:
                                self.mouse.click_element(784, 540)
                                break
                        self.mouse.click_element(784, 540)
                        self.return_bangpai_npc()
                        return 'success'
                    elif i == 8:
                        print("作乱妖怪")
                        self.mouse.click_element(440, 240)
                        self.keyboard.press_shortcut_key('alt', 'q')
                        self.screen.find_ele_picture('game\\system\\zidong','keyboard','alt','8')
                        self.screen.find_ele_picture('game\\bangpai\\8_1', 'mouse', 182, 345)
                        self.return_bangpai_npc()
                        return 'success'
                    elif i == 9:
                        print("收银票")
                        self.keyboard.press_shortcut_key('alt', 'q')
                        time.sleep(1)
                        self.mouse.click_element(459, 266)
                        time.sleep(1)
                        self.mouse.click_element(181, 347)
                        time.sleep(1)
                        self.mouse.click_element(164, 344)
                        time.sleep(2)
                        pyautogui.click()
                        time.sleep(25)
                        pyautogui.moveTo(393, 557, 1, pyautogui.easeInQuad)
                        self.keyboard.press_shortcut_key('alt', 'q')
                        self.screen.cut_screen()
                        time.sleep(2.5)
                        loca = self.screen.get_location_picture("D:\\dh2\\game\\bangpai\\0_2.png", 0.8)
                        if loca is 0:
                            self.mouse.click_element(193, 367)
                        else:
                            self.mouse.click_element(loca[0], loca[1])
                        self.mouse.click_element(420, 239)
                        self.keyboard.press_shortcut_key('alt', '1')
                        self.keyboard.press_shortcut_key('alt', 'q')
                        return 'failed'
                    elif i == 10:
                        return 'success'
            return 'pass'
    def find_bangpai_task(self):
        num = 0
        for j in range(15):
            if num > 9:
                break
            try:
                if j == 0:
                    self.keyboard.press_shortcut_key('alt', '2')
                    time.sleep(1)
                    self.mouse.click_element(507, 419)
                    time.sleep(1)
                    self.mouse.click_element(310, 381)
                    self.screen.find_ele_picture('game\\bangpai\\0_', 'mouse', 220, 328)
                    time.sleep(2)
                    self.mouse.click_element(220, 328)
                    self.keyboard.press_shortcut_key('alt', '1')
                    time.sleep(1)
                    self.mouse.click_element(500, 313)
                    self.mouse.click_element(500, 313)

                # 领取任务
                self.screen.find_ele_picture('game\\bangpai\\0', 'mouse', 223, 329)
                time.sleep(2)
                # pyautogui.click()
                self.keyboard.press_shortcut_key('alt', 'q')
                result = self.bangpai_task()
                if result is 'success' or result is 'pass':
                    num+=1
            except:
                pass
    def return_bangpai_npc(self):
        self.keyboard.press_shortcut_key('alt', 'q')
        self.mouse.click_element(517, 239)
        self.keyboard.press_shortcut_key('alt', 'q')
        time.sleep(5)
        self.screen.find_ele_picture('game\\bangpai\\0_1', 'mouse', 193, 327)
        time.sleep(1)
        pyautogui.click()
        time.sleep(3)
        pyautogui.moveTo(392, 239, 1, pyautogui.easeInQuad)
        self.keyboard.press_shortcut_key('alt', 'q')
        self.screen.cut_screen()
        time.sleep(2.5)
        loca = self.screen.get_location_picture("D:\\dh2\\game\\bangpai\\0_2.png",0.8)
        print(loca)
        if loca is 0:
            self.mouse.click_element(193, 367)
        else:
            self.mouse.click_element(loca[0], loca[1])
        self.mouse.click_element(420, 239)
        self.keyboard.press_shortcut_key('alt', '1')
        self.keyboard.press_shortcut_key('alt', 'q')

    def bangpai_start(self):
        self.common.get_focus()
        for i in range(5):
            # self.common.capation_eat_xiang()
            self.find_bangpai_task()
            self.common.change_teamer()

