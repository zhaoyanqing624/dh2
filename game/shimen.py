import time
from game.common import Common
from system.transform import TransForm
from system.keyboard import KeyBoard
from system.screen import Screen
from system.mouse import Mouse
import _Tools.getFighting
class ShiMen():
    def __init__(self):
        self.transform = TransForm()
        self.common = Common()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.mouse = Mouse()
        self.yao = ''
        self.offset = 17
    def position(self,type):
        if type is 'ren':
            return 596, 508,168,345
        elif type is 'mo':
            return 587, 498,168,362
        elif type is 'gui':
            return 585, 486,163,398
        elif type is 'xian':
            return 595, 520,168,345
    def npc_position(self,type):
        if type is 'ren':
            return 659, 300,404,381
        elif type is 'mo':
            return 528,257,458,359
        elif type is 'gui':
            return 726, 299,538,298
        elif type is 'xian':
            return 222, 190,445,318
    def npc_start(self):
        self.keyboard.press_shortcut_key('alt', 'q')
        time.sleep(1)
        self.mouse.click_element(198, 386)
        time.sleep(1)
        self.mouse.click_element(420, 240)
        time.sleep(1)
        self.screen.find_ele_picture('game\\shimen\\1', 'mouse', 193, 361)
        self.keyboard.press_shortcut_key('alt', 'q')
        time.sleep(1)
        self.keyboard.press_shortcut_key('alt', 'q')
    def later(self,zu,offset_,x,y):
        time.sleep(2)
        self.screen.cut_screen()
        time.sleep(1)
        icon_ = self.screen.get_location_picture("E:\\dh2\\game\\shimen\\1.png")
        time.sleep(1)
        print(icon_)
        self.mouse.click_element(icon_[0], icon_[1] - self.offset)
        time.sleep(1)
        self.mouse.click_element(x, y)
        time.sleep(1)
        self.screen.find_ele_picture('game\\shimen\\' + zu, 'mouse', 195, offset_)
        time.sleep(1)
        self.keyboard.press_shortcut_key('alt', 'q')
    def classify(self,zu,index):
        if index is 0:
            begin = 361
        else:
            begin = 345
        self.screen.cut_screen_location(267, 136, 373, 209)
        for i in range(2, 11):
            print(i)
            if zu is 'ren' or zu is 'xian':
                offset_ = 360
            elif zu is 'mo':
                offset_ = 365
            else:
                offset_ = 345
            file_name = "E:\\dh2\\game\\shimen\\" + str(i) + ".png"
            result = self.screen.get_location_picture(file_name, 0.6, True)
            if result != 0:
                if i == 2:
                    print("风水混元丹")
                    x = 404
                    y = 258
                    self.mouse.click_element(386, 257)
                    time.sleep(1)
                    self.mouse.click_element(195, 363)
                    time.sleep(1)
                    self.mouse.click_element(195, 363)
                    time.sleep(0.5)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    time.sleep(1)
                    self.keyboard.press_shortcut_key('alt', '1')
                    time.sleep(1)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    # self.later(zu, offset_, x, y)
                    if index is 0:
                        self.yao = 'yao'
                    break
                elif i ==3:
                    print("顶天柱")
                    x = 545
                    y = 239
                    self.mouse.click_element(434, 237)
                    time.sleep(1)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    self.screen.find_ele_picture('game\\shimen\\3_1', 'mouse', 184, 329)
                    time.sleep(1)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    time.sleep(1)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    self.later(zu, offset_, x, y)
                    break
                elif i==4:
                    print("密探")
                    x = 416
                    y = 257
                    self.mouse.click_element(593, 239)
                    time.sleep(1)
                    self.screen.find_ele_picture('game\\shimen\\4_1', 'keyboard', 'alt', '8')
                    while True:
                        time.sleep(5)
                        self.screen.cut_screen()
                        location = self.screen.get_location_picture("E:\\dh2\\game\\system\\zidong.png", 0.8)
                        if location is 0:
                            break
                    self.keyboard.press_shortcut_key('alt', 'q')
                    time.sleep(1)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    self.later(zu, offset_,x,y)
                    break
                elif i==5:
                    print("陈夫人")
                    x = 545
                    y = 239
                    self.mouse.click_element(434, 240)
                    self.screen.find_ele_picture('game\\shimen\\5_1', 'mouse', 184, 329)
                    time.sleep(1)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    time.sleep(1)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    self.later(zu, offset_, x, y)
                    break
                elif i==6:
                    print("大香玉")
                    x = 545
                    y = 239
                    self.mouse.click_element(434, 240)
                    self.screen.find_ele_picture('game\\shimen\\6_1', 'mouse', 184, 329)
                    time.sleep(1)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    time.sleep(1)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    self.later(zu, offset_, x, y)
                    break
                elif i==7:
                    print("风姑娘")
                    x = 545
                    y = 239
                    self.mouse.click_element(434, 240)
                    self.screen.find_ele_picture('game\\shimen\\7_1', 'mouse', 184, 329)
                    time.sleep(1)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    time.sleep(1)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    self.later(zu, offset_, x, y)
                    break
                elif i==8:
                    print("何小姐")
                    x = 545
                    y = 239
                    self.mouse.click_element(434, 240)
                    self.screen.find_ele_picture('game\\shimen\\8_1', 'mouse', 184, 329)
                    time.sleep(1)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    time.sleep(1)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    self.later(zu, offset_, x, y)
                    break
                elif i==9:
                    print("胡巧儿")
                    x = 545
                    y = 239
                    self.mouse.click_element(434, 240)
                    self.screen.find_ele_picture('game\\shimen\\9_1', 'mouse', 184, 329)
                    time.sleep(1)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    time.sleep(1)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    self.later(zu, offset_, x, y)
                    break
                elif i==10:
                    print("切磋")
                    x = 514
                    y = 240
                    self.mouse.click_element(388, 256)
                    self.screen.find_ele_picture('game\\shimen\\10_1', 'mouse', 207, 329)
                    time.sleep(2)
                    self.keyboard.press_shortcut_key('alt', '8')
                    while True:
                        time.sleep(5)
                        self.screen.cut_screen()
                        location = self.screen.get_location_picture("E:\\dh2\\game\\system\\zidong.png", 0.8)
                        if location is 0:
                            break
                    self.keyboard.press_shortcut_key('alt', 'q')
                    time.sleep(1)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    self.later(zu, offset_, x, y)
                    break


    def task_start(self,list):
        print("任务开始")
        self.common.get_focus()
        for i in list:
            if i is 'gui':
                aaa = 345
            else:
                aaa = 360
            self.yao = ''
            self.keyboard.press_shortcut_key('alt', '2')
            time.sleep(1)
            self.mouse.click_element(505, 415)
            time.sleep(1)
            positon_ = self.position(i)
            self.mouse.click_element(positon_[0], positon_[1])
            self.screen.find_ele_picture('game\\shimen\\0', 'mouse', positon_[2], positon_[3])
            time.sleep(2)
            positon2_ = self.npc_position(i)
            self.mouse.click_element(positon2_[0], positon2_[1],right=True)
            time.sleep(2)
            self.mouse.click_element(positon2_[2], positon2_[3])
            time.sleep(1)

            self.screen.find_ele_picture('game\\shimen\\'+i, 'mouse', 193, aaa)
            time.sleep(1)
            self.keyboard.press_shortcut_key('alt', 'q')
            time.sleep(2)
            self.screen.cut_screen()
            time.sleep(1)
            icon = self.screen.get_location_picture("E:\\dh2\\game\\shimen\\1.png")
            time.sleep(1)
            self.mouse.click_element(icon[0],icon[1]-self.offset)
            time.sleep(1)

            for j in range(10):
                print("第"+str(j+1)+"次")
                # if j is 1 and self.yao is 'yao':
                #     # self.mouse.click_element(505, 415)
                #     # time.sleep(1)
                #     self.mouse.click_element(405, 240)
                #     time.sleep(1)
                if j is not 0:
                    if i is 'ren' or i is 'xian':
                        offset_1 = 360
                    elif i is 'mo':
                        offset_1 = 365
                    else:
                        offset_1 = 345
                    time.sleep(1)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    self.later(i, offset_1, 412, 240)
                self.classify(i,j)
if __name__ == '__main__':
    list = ['ren']
    # list = ['ren','mo','mo','xian','gui']

    ShiMen().task_start(list)
    # ShiMen().classify()
    # Screen().cut_screen_location(267, 136, 373, 209)