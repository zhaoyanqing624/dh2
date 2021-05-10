import time
from game.common import Common
from system.transform import TransForm
from system.keyboard import KeyBoard
from system.screen import Screen
from system.mouse import Mouse
import pyautogui

class QinLin():

    def __init__(self):
        self.transform = TransForm()
        self.common = Common()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.mouse = Mouse()

    def make_sure(self):
        for i in range(5):
            self.mouse.click_element(311, 490)
            self.common.change_teamer()
        self.common.get_focus()

    def make_sure_wuyi(self):
        for i in range(5):
            self.mouse.click_element(183, 347)
            self.common.change_teamer()
        self.common.get_focus()

    def game_over(self):
        endtime = time.time() + int(300)
        while time.time() < endtime:
            time.sleep(1)
            self.screen.cut_screen()
            time.sleep(1)
            result_ = self.screen.get_location_picture("C:\\dh2\\game\\system\\zidong.png", num=0.8)
            if result_ is 0:
                return True
        return False

    def operate(self, location=None):
        result_ = self.screen.find_ele_picture_time('game\\system\\caozuo')
        if result_ is True:
            if location is None:
                for i in range(5):
                    self.keyboard.press_shortcut_key('alt', '8')
                    self.common.change_teamer()
            else:
                for i in range(5):
                    if i is 0:
                        self.keyboard.press_key('f7')
                        self.mouse.click_direct_element(location[0], location[1])
                        self.keyboard.press_shortcut_key('alt', 't')
                        self.mouse.click_direct_element(650, 400)
                    self.keyboard.press_shortcut_key('alt', '8')
                    self.common.change_teamer()
        self.common.get_focus()

    def find_qingtongding(self):
        self.common.get_focus()
        maze = [(210, 366), (248, 470), (343, 382), (404, 395), (455, 375),
                (448, 328), (604, 319), (560, 302), (604, 256)]
        for i in maze:
            self.keyboard.press_shortcut_key('alt', '1')
            self.mouse.click_element(i[0], i[1])
            self.keyboard.press_shortcut_key('alt', '1')
            pyautogui.moveTo(424, 557, 1, pyautogui.easeInQuad)
            time.sleep(5)
            while True:
                walking = self.common.iswalking()
                if walking is False:
                    break
            self.screen.cut_screen_location(820, 650, 0, 0)
            time.sleep(1)
            result = Screen().find_color_ele(400,400,350,250,r1=250,r2=260,g1=250,g2=260,b1=0,b2=10,cut_zone=True)
            if result is not None:
                self.mouse.click_direct_element(result[0]-15, result[1]-45)
            time.sleep(1)

    def operate_xingdou(self):
        self.common.get_focus()
        self.common.change_teamer()
        for i in range(4):
            self.mouse.click_element(734, 260)
            self.mouse.click_element(169, 328)
            self.common.change_teamer()
        time.sleep(5)

    def find_xingdou(self):
        self.common.get_focus()
        xingdou = [
            (600, 350), (670, 350), (740, 350),
            (600, 430), (670, 430),
        ]
        maze = [
            (280, 270), (340, 270), (400, 270),
            (250, 320), (310, 320), (370, 320), (430, 320),
            (220, 370), (280, 370), (340, 370), (400, 370), (460, 370),
            (250, 420), (310, 420), (370, 420), (430, 420),
            (280, 470), (340, 470), (400, 470),
        ]
        mubiao = 0
        time.sleep(1)
        self.screen.cut_screen()
        time.sleep(1.5)
        pos_dian = self.screen.get_location_picture("C:\\dh2\\yitiao\\qinlin\\5_1.png", num=0.8)
        if pos_dian is 0:
            pos_dian = [0,0]
        for index, i in enumerate(maze):
            if i[0]-10<= pos_dian[0]<= i[0]+10 and i[1]-10<= pos_dian[1]<= i[1]+10:
                mubiao = index+1
        if mubiao is 1:
            self.operate_xingdou()
            self.mouse.click_element(xingdou[0][0], xingdou[0][1])
            self.mouse.click_element(maze[1][0], maze[1][1])
            self.mouse.click_element(xingdou[3][0], xingdou[3][1])
            self.mouse.click_element(maze[7][0], maze[7][1])
            self.mouse.click_element(xingdou[0][0], xingdou[0][1])
            self.mouse.click_element(maze[5][0], maze[5][1])
            self.mouse.click_element(xingdou[4][0], xingdou[4][1])
            self.mouse.click_element(maze[11][0], maze[11][1])
            self.mouse.click_element(xingdou[2][0], xingdou[2][1])
            self.mouse.click_element(maze[13][0], maze[13][1])
            self.mouse.click_element(xingdou[2][0], xingdou[2][1])
            self.mouse.click_element(maze[17][0], maze[17][1])
        elif mubiao is 3:
            self.operate_xingdou()
            self.mouse.click_element(xingdou[0][0], xingdou[0][1])
            self.mouse.click_element(maze[0][0], maze[0][1])
            self.mouse.click_element(xingdou[2][0], xingdou[2][1])
            self.mouse.click_element(maze[5][0], maze[5][1])
            self.mouse.click_element(xingdou[2][0], xingdou[2][1])
            self.mouse.click_element(maze[8][0], maze[8][1])
            self.mouse.click_element(xingdou[0][0], xingdou[0][1])
            self.mouse.click_element(maze[10][0], maze[10][1])
            self.mouse.click_element(xingdou[4][0], xingdou[4][1])
            self.mouse.click_element(maze[13][0], maze[13][1])
            self.mouse.click_element(xingdou[1][0], xingdou[1][1])
            self.mouse.click_element(maze[17][0], maze[17][1])
        elif mubiao is 5:
            self.operate_xingdou()
            self.mouse.click_element(xingdou[0][0], xingdou[0][1])
            self.mouse.click_element(maze[0][0], maze[0][1])
            self.mouse.click_element(xingdou[3][0], xingdou[3][1])
            self.mouse.click_element(maze[5][0], maze[5][1])
            self.mouse.click_element(xingdou[4][0], xingdou[4][1])
            self.mouse.click_element(maze[8][0], maze[8][1])
            self.mouse.click_element(xingdou[2][0], xingdou[2][1])
            self.mouse.click_element(maze[10][0], maze[10][1])
            self.mouse.click_element(xingdou[0][0], xingdou[0][1])
            self.mouse.click_element(maze[13][0], maze[13][1])
            self.mouse.click_element(xingdou[1][0], xingdou[1][1])
            self.mouse.click_element(maze[18][0], maze[18][1])
        elif mubiao is 14:
            self.operate_xingdou()
            self.mouse.click_element(xingdou[3][0], xingdou[3][1])
            self.mouse.click_element(maze[3][0], maze[3][1])
            self.mouse.click_element(xingdou[4][0], xingdou[4][1])
            self.mouse.click_element(maze[5][0], maze[5][1])
            self.mouse.click_element(xingdou[4][0], xingdou[4][1])
            self.mouse.click_element(maze[8][0], maze[8][1])
            self.mouse.click_element(xingdou[1][0], xingdou[1][1])
            self.mouse.click_element(maze[10][0], maze[10][1])
            self.mouse.click_element(xingdou[1][0], xingdou[1][1])
            self.mouse.click_element(maze[15][0], maze[15][1])
            self.mouse.click_element(xingdou[2][0], xingdou[2][1])
            self.mouse.click_element(maze[17][0], maze[17][1])
        elif mubiao is 15:
            self.operate_xingdou()
            self.mouse.click_element(xingdou[0][0], xingdou[0][1])
            self.mouse.click_element(maze[0][0], maze[0][1])
            self.mouse.click_element(xingdou[1][0], xingdou[1][1])
            self.mouse.click_element(maze[5][0], maze[5][1])
            self.mouse.click_element(xingdou[2][0], xingdou[2][1])
            self.mouse.click_element(maze[8][0], maze[8][1])
            self.mouse.click_element(xingdou[3][0], xingdou[3][1])
            self.mouse.click_element(maze[10][0], maze[10][1])
            self.mouse.click_element(xingdou[4][0], xingdou[4][1])
            self.mouse.click_element(maze[13][0], maze[13][1])
            self.mouse.click_element(xingdou[1][0], xingdou[1][1])
            self.mouse.click_element(maze[18][0], maze[18][1])
        elif mubiao is 18:
            self.operate_xingdou()
            self.mouse.click_element(xingdou[0][0], xingdou[0][1])
            self.mouse.click_element(maze[0][0], maze[0][1])
            self.mouse.click_element(xingdou[3][0], xingdou[3][1])
            self.mouse.click_element(maze[5][0], maze[5][1])
            self.mouse.click_element(xingdou[1][0], xingdou[1][1])
            self.mouse.click_element(maze[8][0], maze[8][1])
            self.mouse.click_element(xingdou[2][0], xingdou[2][1])
            self.mouse.click_element(maze[10][0], maze[10][1])
            self.mouse.click_element(xingdou[4][0], xingdou[4][1])
            self.mouse.click_element(maze[13][0], maze[13][1])
            self.mouse.click_element(xingdou[4][0], xingdou[4][1])
            self.mouse.click_element(maze[15][0], maze[15][1])
        else:
            # 重新找
            self.mouse.click_element(774, 212)
            self.mouse.click_element(339, 401)
            self.screen.find_ele_picture(file_path='yitiao\\qinlin\\0', handle='self')
            self.mouse.click_element(169, 331)
            self.keyboard.press_shortcut_key('alt', 'c')
            time.sleep(2)
            self.keyboard.press_shortcut_key('alt', '2')
            time.sleep(1)
            self.mouse.click_element(457, 479)
            time.sleep(2)
            self.mouse.click_element(281, 336)
            time.sleep(2)
            self.screen.find_ele_picture('yitiao\\qinlin\\begin')
            self.mouse.click_element(180, 345, times=0.5)
            time.sleep(2)
            self.make_sure()
            time.sleep(5)
            self.mouse.click_element(231, 233, times=0.5)
            self.mouse.click_element(177, 328, times=0.5)
            self.find_xingdou()

    def start_task(self, num, level):
        self.common.get_focus()
        self.keyboard.press_shortcut_key('alt', '2')
        time.sleep(1)
        self.mouse.click_element(457, 479)
        time.sleep(2)
        self.mouse.click_element(281, 336)
        time.sleep(10)
        # 寻找NPC
        self.screen.find_ele_picture('yitiao\\qinlin\\begin')
        self.mouse.click_element(180, 345, times=0.5)
        time.sleep(2)
        self.make_sure()
        time.sleep(5)
        # 第一个 - 点灯
        self.mouse.click_element(73, 255, times=0.5)
        self.screen.find_ele_picture('yitiao\\qinlin\\1', 'mouse', 174, 327)
        self.mouse.click_element(100, 255, times=0.5)
        self.screen.find_ele_picture('yitiao\\qinlin\\1', 'mouse', 174, 327)

        # 第二个 - 机关兽
        time.sleep(3)
        self.keyboard.press_key('esc')
        time.sleep(1)
        self.mouse.click_element(76, 255, times=0.5)
        time.sleep(2)
        if int(level[0]) is 0:
            self.screen.find_ele_picture('yitiao\\qinlin\\2', 'mouse', 175, 328)
        elif int(level[0]) is 1:
            self.screen.find_ele_picture('yitiao\\qinlin\\2', 'mouse', 175, 345)
            self.mouse.click_element(311, 490)
        self.operate()
        self.game_over()
        time.sleep(2)
        self.screen.find_ele_picture(file_path='yitiao\\qinlin\\2_1', handle='self')

        # 第三个 - 虎符
        self.keyboard.press_key('esc')
        self.mouse.click_element(102, 255, times=0.5)
        self.screen.find_ele_picture('yitiao\\qinlin\\3', 'mouse', 178, 345, location_=[102, 255])
        time.sleep(3)

        # 第四个 - 沙盘
        self.keyboard.press_key('esc')
        self.mouse.click_element(103, 256, times=0.5)
        self.screen.find_ele_picture('yitiao\\qinlin\\4', 'mouse', 175, 328)
        self.keyboard.press_shortcut_key('alt', '1')
        self.mouse.click_element(150, 241, times=0.5)
        pyautogui.rightClick()
        self.mouse.click_element(150, 241, times=0.5)
        time.sleep(10)
        if int(level[1]) is 0:
            self.screen.find_ele_picture('yitiao\\qinlin\\4_1', 'mouse', 175, 345)
        elif int(level[1]) is 1:
            self.screen.find_ele_picture('yitiao\\qinlin\\4_1', 'mouse', 175, 360)
            self.mouse.click_element(311, 490)
        self.operate()
        self.game_over()
        time.sleep(2)
        self.screen.find_ele_picture(file_path='yitiao\\qinlin\\2_1', handle='self')
        time.sleep(5)
        self.find_qingtongding()

        # 第五个 - 沙盘星座
        self.mouse.click_element(64, 241, times=0.5)
        self.screen.find_ele_picture('yitiao\\qinlin\\5', 'mouse', 177, 329)
        self.find_xingdou()
        time.sleep(5)

        # 宠物医生
        self.keyboard.press_key('esc')
        time.sleep(2)
        #self.keyboard.press_shortcut_key('alt', '1')
        self.mouse.click_element(452, 360, times=0.5)
        self.screen.find_ele_picture('game\\system\\wuyi', 'mouse', 188, 344)
        self.common.change_teamer()
        for i in range(4):
            self.mouse.click_element(188, 344, times=0.5)
            self.common.change_teamer()
        self.keyboard.press_shortcut_key('alt', '1')
        self.make_sure_wuyi()
        time.sleep(2)

        # 第六个 - 将军俑
        if num >= 6:
            self.screen.find_ele_picture(file_path='system\\zidong_', handle='self')
            self.mouse.click_element(110, 240, times=0.5)
            if int(level[2]) is 0:
                self.screen.find_ele_picture('yitiao\\qinlin\\6', 'mouse', 176, 331)
            elif int(level[2]) is 1:
                self.screen.find_ele_picture('yitiao\\qinlin\\6', 'mouse', 176, 345)
                self.mouse.click_element(311, 490)
            self.operate([112, 485])
            self.game_over()
            time.sleep(2)
            self.screen.find_ele_picture(file_path='yitiao\\qinlin\\2_1', handle='self')
            time.sleep(2)
            self.keyboard.press_key('esc')
            # 宠物医生
            self.keyboard.press_key('esc')
            time.sleep(2)
            self.keyboard.press_shortcut_key('alt', '1')
            self.mouse.click_element(452, 360, times=0.5)
            self.screen.find_ele_picture('game\\system\\wuyi', 'mouse', 188, 344)
            self.common.change_teamer()
            for i in range(4):
                self.mouse.click_element(188, 344, times=0.5)
                self.common.change_teamer()
            self.keyboard.press_shortcut_key('alt', '1')
            self.make_sure_wuyi()
            time.sleep(2)

        # 第七个
        if num>=7:
            self.screen.find_ele_picture(file_path='system\\zidong_', handle='self')
            self.mouse.click_element(70, 243, times=0.5)
            if int(level[3]) is 0:
                self.screen.find_ele_picture('yitiao\\qinlin\\7', 'mouse', 176, 327)
                self.operate([214, 472])
            elif int(level[3]) is 1:
                self.screen.find_ele_picture('yitiao\\qinlin\\7', 'mouse', 176, 345)
                self.mouse.click_element(311, 490)
                self.operate([237, 230])
            self.game_over()
            time.sleep(15)

        # 宠物医生
        self.keyboard.press_key('esc')
        self.keyboard.press_shortcut_key('alt', '1')
        self.mouse.click_element(452, 360, times=0.5)
        self.screen.find_ele_picture('game\\system\\wuyi', 'mouse', 188, 344)
        self.common.change_teamer()
        for i in range(4):
            self.mouse.click_element(188, 344, times=0.5)
            self.common.change_teamer()
        self.keyboard.press_shortcut_key('alt', '1')
        self.make_sure_wuyi()
        time.sleep(2)

        # 退出
        self.screen.find_ele_picture(file_path='yitiao\\qinlin\\0', handle='self')
        self.mouse.click_element(172, 328, times=0.5)



