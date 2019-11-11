# 街坊
import pyautogui
import random
import time
import _Tools.getCutPicture
import _Tools.getWalking
import _Tools.getFighting
import _Tools.getLocation
import _Tools.isWalking


def fight():
    time.sleep(1.5)
    pyautogui.keyDown('F5')
    pyautogui.keyUp('F5')
    time.sleep(0.5)
    pyautogui.moveTo(194 + random.randint(0, 5), 319 + random.randint(0, 5), 1, pyautogui.easeInQuad)
    pyautogui.click()
    time.sleep(1)
    pyautogui.keyDown('alt')
    pyautogui.keyDown('a')
    pyautogui.keyUp('a')
    pyautogui.keyUp('alt')
    time.sleep(1)
    pyautogui.keyDown('alt')
    pyautogui.keyDown('8')
    pyautogui.keyUp('8')
    pyautogui.keyUp('alt')

def cicle(x):
    while True:
        pyautogui.moveTo(412 + random.randint(0, 5), 590 + random.randint(0, 5), 1, pyautogui.easeInQuad)
        time.sleep(1)
        _Tools.getCutPicture.window_capture()
        time.sleep(1)
        location = _Tools.getLocation.getPictureLocation("D:\\dh2\\bangpai\\"+x+".png", 0.9)
        if location != 0:
            break
def start(y):
    # 点击领取任务
    time.sleep(1)
    pyautogui.moveTo(229 + random.randint(0, 5), 347 + random.randint(0, 5), 1, pyautogui.easeInQuad)
    pyautogui.click()
    time.sleep(1.5)
    pyautogui.click()
    # 任务过程
    time.sleep(1)
    taskClassify(y)

def goHome():
    time.sleep(1)
    pyautogui.keyDown('alt')
    pyautogui.keyDown('q')
    pyautogui.keyUp('q')
    pyautogui.keyUp('alt')
    time.sleep(1)
    pyautogui.keyDown('alt')
    pyautogui.keyDown('q')
    pyautogui.keyUp('q')
    pyautogui.keyUp('alt')
    time.sleep(1)
    pyautogui.moveTo(525 + random.randint(0, 5), 239, 1, pyautogui.easeInQuad)
    pyautogui.click()
    time.sleep(1)
    cicle("2")
    time.sleep(0.5)
    pyautogui.moveTo(195 + random.randint(0, 5), 345, 1, pyautogui.easeInQuad)
    pyautogui.click()
    time.sleep(1.5)
    pyautogui.click()
    time.sleep(2.5)
    pyautogui.moveTo(511 + random.randint(0, 5), 134, 1, pyautogui.easeInQuad)
    pyautogui.click()

def taskClassify(y):
    global outside
    if y ==0:
        pyautogui.keyDown('alt')
        pyautogui.keyDown('q')
        pyautogui.keyUp('q')
        pyautogui.keyUp('alt')
        print()
    else:
        if outside == False:
            time.sleep(1)
            pyautogui.keyDown('alt')
            pyautogui.keyDown('q')
            pyautogui.keyUp('q')
            pyautogui.keyUp('alt')
            time.sleep(1)
            pyautogui.keyDown('alt')
            pyautogui.keyDown('q')
            pyautogui.keyUp('q')
            pyautogui.keyUp('alt')
        else:
            time.sleep(1)
            pyautogui.keyDown('alt')
            pyautogui.keyDown('q')
            pyautogui.keyUp('q')
            pyautogui.keyUp('alt')
    time.sleep(1)
    y = ["2_1", "2_2", "2_3", "2_4", "2_5", "2_6", "2_7"]
    time.sleep(1)
    for x in y:
        time.sleep(0.5)
        _Tools.getCutPicture.window_capture()
        location = _Tools.getLocation.getPictureLocation("D:\\dh2\\bangpai\\"+x+".PNG", 0.9)
        if location != 0:
            if x == "2_1":
                print("无名侠女")
                outside = True
                pyautogui.moveTo(502 + random.randint(0, 5), 240, 1, pyautogui.easeInQuad)
                pyautogui.click()
                time.sleep(1)
                cicle("0_")
                time.sleep(1)
                # fight()
                cicle("2_1_1")
                goHome()
            elif x == "2_2":
                print("帮药")
                outside = False
                time.sleep(1)
                pyautogui.moveTo(502 + random.randint(0, 5), 129, 1, pyautogui.easeInQuad)
                pyautogui.click()
                time.sleep(1)
                pyautogui.moveTo(195 + random.randint(0, 5), 345, 1, pyautogui.easeInQuad)
                pyautogui.click()
                time.sleep(0.5)
                pyautogui.click()
                time.sleep(2.5)
                pyautogui.moveTo(511 + random.randint(0, 5), 134, 1, pyautogui.easeInQuad)
                pyautogui.click()
                time.sleep(1)
            elif x == "2_3":
                print("回答问题")
                outside = False
                # 关闭任务栏
                time.sleep(1)
                pyautogui.keyDown('alt')
                pyautogui.keyDown('q')
                pyautogui.keyUp('q')
                pyautogui.keyUp('alt')
                # 点击雕像
                time.sleep(1)
                pyautogui.moveTo(location[0] + random.randint(0, 5), location[1], 1, pyautogui.easeInQuad)
                pyautogui.click()
                # 185 345 点击回答问题
                time.sleep(1)
                pyautogui.moveTo(185, 345, 1, pyautogui.easeInQuad)
                pyautogui.click()
                # 判断点击的东西
                time.sleep(1)
                y2 = ["2_3_1", "2_3_2", "2_3_3"]
                for x2 in y2:
                    time.sleep(1)
                    _Tools.getCutPicture.window_capture()
                    location_q = _Tools.getLocation.getPictureLocation("D:\\dh2\\bangpai\\" + x2 + ".PNG", 0.9)
                    if location_q != 0:
                        time.sleep(0.5)
                        pyautogui.moveTo(location_q[0], location_q[1], 1, pyautogui.easeInQuad)
                        pyautogui.click()
                        time.sleep(1)
                # 点击交付任务
                time.sleep(1)
                pyautogui.moveTo(location[0] + random.randint(0, 5), location[1], 1, pyautogui.easeInQuad)
                pyautogui.click()
                # 确定
                time.sleep(1)
                pyautogui.moveTo(185, 345, 1, pyautogui.easeInQuad)
                pyautogui.click()
            elif x == "2_4":
                print("作乱妖怪")
                outside = False
                time.sleep(1)
                pyautogui.moveTo(443 + random.randint(0, 5), 238, 1, pyautogui.easeInQuad)
                pyautogui.click()
                cicle("0_")
                time.sleep(1)
                # fight()
                cicle("2_4_1")
                goHome()

            elif x == "2_5":
                print("酒店老板")
                outside = True
                time.sleep(1)
                pyautogui.moveTo(445 + random.randint(0, 5), 240, 1, pyautogui.easeInQuad)
                pyautogui.click()
                # 判断是否走到了
                cicle("2_5_1")
                time.sleep(1)
                pyautogui.moveTo(184 + random.randint(0, 5), 330, 1, pyautogui.easeInQuad)
                pyautogui.click()
                time.sleep(0.5)
                pyautogui.click()
                time.sleep(0.5)
                goHome()
            elif x == "2_6":
                print("长安武馆")
                outside = True
                time.sleep(1)
                pyautogui.moveTo(430 + random.randint(0, 5), 240, 1, pyautogui.easeInQuad)
                pyautogui.click()
                # 判断是否走到了
                time.sleep(40)
                pyautogui.moveTo(785 + random.randint(0, 5), 538, 1, pyautogui.easeInQuad)
                pyautogui.click()
                time.sleep(0.5)
                goHome()
            elif x == "2_7":
                print("除草")
                outside = False
                time.sleep(1)
                pyautogui.keyDown('alt')
                pyautogui.keyDown('q')
                pyautogui.keyUp('q')
                pyautogui.keyUp('alt')
                for i in range(0,3):
                    time.sleep(1)
                    pyautogui.moveTo(86 + random.randint(0, 5), 602, 1, pyautogui.easeInQuad)
                    pyautogui.rightClick()
                    time.sleep(2)
                    pyautogui.moveTo(792 + random.randint(0, 5), 541, 1, pyautogui.easeInQuad)
                    pyautogui.rightClick()
                time.sleep(1)
                pyautogui.keyDown('alt')
                pyautogui.keyDown('q')
                pyautogui.keyUp('q')
                pyautogui.keyUp('alt')
                time.sleep(1)
                goHome()
def click(x, y):
    time.sleep(1)
    pyautogui.moveTo(x, y, 1, pyautogui.easeInQuad)
    pyautogui.click()
def keyBoard(str,str2):
    time.sleep(1)
    pyautogui.keyDown(str)
    pyautogui.keyDown(str2)
    pyautogui.keyUp(str2)
    pyautogui.keyUp(str)
def step_01():
    # 打开地图
    keyBoard('alt','e')
    time.sleep(1)
    pyautogui.moveTo(50, 400, 1, pyautogui.easeInQuad)
    pyautogui.rightClick()
    time.sleep(1)
    keyBoard('alt', 'e')
    time.sleep(1)
    pyautogui.keyDown('alt')
    pyautogui.keyDown('2')
    pyautogui.keyUp('2')
    pyautogui.keyUp('alt')
    # 点击到帮派传送人处
    time.sleep(1)
    pyautogui.moveTo(507 + random.randint(0, 5), 420 + random.randint(0, 5), 1, pyautogui.easeInQuad)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(313, 386 , 1, pyautogui.easeInQuad)
    pyautogui.click()
def step_02():
    # 屏蔽周围的人
    time.sleep(1)
    pyautogui.keyDown('alt')
    pyautogui.keyDown('5')
    pyautogui.keyUp('5')
    pyautogui.keyUp('alt')
    # 点击帮派接引人
    time.sleep(1)
    _Tools.getCutPicture.window_capture()
    time.sleep(1)
    location_0 = _Tools.getLocation.getPictureLocation("D:\\dh2\\bangpai\\0.png", 0.7)
    time.sleep(0.5)
    pyautogui.moveTo(location_0[0] + random.randint(0, 5), location_0[1] - 50 + random.randint(0, 5), 1,
                     pyautogui.easeInQuad)
    pyautogui.click()
    # 进入帮派
    time.sleep(1)
    pyautogui.moveTo(219 + random.randint(0, 5), 330 + random.randint(0, 5), 1, pyautogui.easeInQuad)
    pyautogui.click()
    # 走到任务处
    time.sleep(3)
    pyautogui.keyDown('alt')
    pyautogui.keyDown('1')
    pyautogui.keyUp('1')
    pyautogui.keyUp('alt')
    time.sleep(1)
    pyautogui.moveTo(440, 332, 1, pyautogui.easeInQuad)
    pyautogui.click()

def step_03(i):
    if i == 1:
        # 屏蔽人
        time.sleep(1)
        pyautogui.keyDown('alt')
        pyautogui.keyDown('5')
        pyautogui.keyUp('5')
        pyautogui.keyUp('alt')
        # 点击老虎雕像
        time.sleep(1)
        _Tools.getCutPicture.window_capture()
        time.sleep(1)
        location_1 = _Tools.getLocation.getPictureLocation("D:\\dh2\\bangpai\\1.png", 0.7)
        time.sleep(0.5)
        pyautogui.moveTo(location_1[0] + random.randint(0, 5), location_1[1] + random.randint(0, 5), 1,
                         pyautogui.easeInQuad)
        pyautogui.click()
    else:
        click(511, 134)
    time.sleep(1)
    step_04()


def step_04():
    # 开始执行
    click(218, 347)
    time.sleep(1)
    _Tools.getCutPicture.window_capture()
    time.sleep(1)
    location = _Tools.getLocation.getPictureLocation("D:\\dh2\\bangpai\\1_1.png", 0.8)
    if location == 0:
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        step_05()
    else:
        click(191, 345)
        time.sleep(1.5)
        pyautogui.click()
        time.sleep(1)
        step_05()

def step_05():
    time.sleep(1)
    pyautogui.keyDown('alt')
    pyautogui.keyDown('q')
    pyautogui.keyUp('q')
    pyautogui.keyUp('alt')
    time.sleep(1)
    y = ["2_1", "2_2", "2_3", "2_4", "2_5", "2_6", "2_7", "2_8", "2_9"]
    for i in y:
        time.sleep(1)
        _Tools.getCutPicture.window_capture()
        location = _Tools.getLocation.getPictureLocation("D:\\dh2\\bangpai\\"+i+".PNG", 0.9)
        if location!=0:
            if i=="2_1":
                # 无名侠女
                print("无名侠女")
                time.sleep(1)
                click(46, 611)
                click(503, 241)
                keyBoard('alt', 'q')
                cicle("2_1_1")
                click(223, 349)
                keyBoard('alt', 'q')
                click(525, 238)
                keyBoard('alt', 'q')
                cicle("2")
                click(199, 347)
                time.sleep(1.5)
                pyautogui.click()
                break
            elif i=="2_2":
                # 帮派药
                keyBoard('alt', 'q')
                click(511, 134)
                click(199, 347)
                time.sleep(1.5)
                pyautogui.click()
                break
            elif i=="2_3":
                # 答题
                keyBoard('alt','q')
                click(511, 134)
                click(182, 345)
                while True:
                    time.sleep(1)
                    _Tools.getCutPicture.window_capture()
                    time.sleep(2)
                    location_11 = _Tools.getLocation.getPictureLocation("D:\\dh2\\bangpai\\2_3_1.png",0.4)
                    if location_11!=0:
                        click(164,329)
                        time.sleep(3)
                    else:
                        break
                click(511, 134)
                click(199, 347)
                time.sleep(1.5)
                pyautogui.click()
                break
            elif i=="2_4":
                # 作乱妖怪
                time.sleep(1)
                click(46, 611)
                click(445, 239)
                keyBoard('alt','q')
                cicle("2_4_1")
                keyBoard('alt', 'q')
                click(525, 238)
                keyBoard('alt', 'q')
                cicle("2")
                click(199, 347)
                time.sleep(1.5)
                pyautogui.click()
                break
            elif i=="2_5":
                # 酒店老板
                click(449, 242)
                keyBoard('alt', 'q')
                time.sleep(20)
                cicle("2_5_1")
                click(184, 346)
                keyBoard('alt', 'q')
                click(525, 238)
                keyBoard('alt', 'q')
                cicle("2")
                click(199, 347)
                time.sleep(1.5)
                pyautogui.click()
                break
            elif i=="2_6":
                # 帮派宣传
                click(435, 237)
                keyBoard('alt', 'q')
                time.sleep(60)
                click(789, 537)
                keyBoard('alt', 'q')
                click(525, 238)
                keyBoard('alt', 'q')
                cicle("2")
                click(199, 347)
                time.sleep(1.5)
                pyautogui.click()
                break
            elif i=="2_7":
                # 除草
                keyBoard('alt', 'q')
                for i in range(0,8):
                    click(785, 540)
                    pyautogui.moveTo(401 + random.randint(0, 5), 573 + random.randint(0, 5), 1,
                                     pyautogui.easeInQuad)
                    pyautogui.rightClick()
                    time.sleep(2.5)
                keyBoard('alt', 'q')
                click(522, 240)
                time.sleep(1)
                keyBoard('alt', 'q')
                cicle("2")
                click(199, 347)
                time.sleep(1.5)
                pyautogui.click()
                break
            elif i=="2_8":
                # 武官
                # keyBoard('alt','c')
                time.sleep(1)
                click(46, 611)
                click(463, 241)
                keyBoard('alt', 'q')
                cicle("2_8_1")
                keyBoard('alt', 'q')
                time.sleep(1)
                # keyBoard('alt', 'c')
                click(484, 240)
                keyBoard('alt', 'q')
                cicle("2_8_2")
                click(209, 318)
                keyBoard('alt', 'q')
                # keyBoard('alt', 'c')
                click(522, 240)
                time.sleep(1)
                keyBoard('alt', 'q')
                cicle("2")
                # keyBoard('alt', 'c')
                click(199, 347)
                time.sleep(1.5)
                pyautogui.click()
                break
            elif i == "2_9":
                # 收取银票
                # keyBoard('alt', 'c')
                click(457, 237)
                time.sleep(1)
                keyBoard('alt', 'q')
                cicle("2_9_1")
                keyBoard('alt', 'q')
                click(522, 240)
                time.sleep(1)
                keyBoard('alt', 'q')
                cicle("2")
                click(199, 347)
                time.sleep(1.5)
                pyautogui.click()
                break



def keyBoard(str, str2, time_=1):
    time.sleep(time_)
    pyautogui.keyDown(str)
    pyautogui.keyDown(str2)
    pyautogui.keyUp(str2)
    pyautogui.keyUp(str)

def BPstartTask():
    list = [75, 250, 400, 545, 700]
    for i in list:
        click(i, 45)
        step_01()
        time.sleep(20)
        step_02()
        time.sleep(1)
        for x in range(1,11):
            if x ==1:
                time.sleep(20)
            step_03(x)








