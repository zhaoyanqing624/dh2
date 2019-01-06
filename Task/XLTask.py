import pyautogui
import random
import time
import _Tools.getCutPicture
import _Tools.getWalking
import _Tools.getFighting
import _Tools.getLocation
import _Tools.isWalking
import aircv as ac

import time
import random
def click_fast(x, y):
    pyautogui.moveTo(x, y, 0.5, pyautogui.easeInQuad)
    pyautogui.click()

def keyBoard(str, str2, time_=1):
    time.sleep(time_)
    pyautogui.keyDown(str)
    pyautogui.keyDown(str2)
    pyautogui.keyUp(str2)
    pyautogui.keyUp(str)
def doing_fighting(a):
    # 203 334
    if a ==1:
        for i in range(0, 5):
            if i == 0:
                time.sleep(2.5)
            else:
                time.sleep(0.5)
            if i==0 or i==1 or i==2:
                pyautogui.keyDown('f7')
                pyautogui.keyUp('f7')
                click_fast(203, 334)
                if i == 3:
                    keyBoard('alt', 'a', 0.3)
                    click_fast(203, 334)
                    keyBoard('alt', '8', 0.3)
                elif i == 2:
                    keyBoard('alt', 's', 0.3)
                    click_fast(203, 334)
                    keyBoard('alt', '8', 0.3)
                else:
                    keyBoard('alt', 'd', 0.3)
                    keyBoard('alt', '8', 0.3)
            elif i==3:
                pyautogui.keyDown('f7')
                pyautogui.keyUp('f7')
                click_fast(203, 334)
                keyBoard('alt', 'a', 0.3)
                keyBoard('alt', '8', 0.3)
            elif i==4:
                pyautogui.keyDown('f7')
                pyautogui.keyUp('f7')
                click_fast(203, 334)
                keyBoard('alt', 'd', 0.3)
                keyBoard('alt', '8', 0.3)
            else:
                pyautogui.keyDown('f7')
                pyautogui.keyUp('f7')
                click_fast(203, 334)
                keyBoard('alt', 'd', 0.3)
                keyBoard('alt', '8', 0.3)
            keyBoard('ctrl', 'tab', 0.3)
def ice():
    time.sleep(1)
    _Tools.getCutPicture.window_capture()
    time.sleep(1)
    location = pyautogui.locateCenterOnScreen("E:\\dh2\\xiuluo\\5.PNG")
    if location != None:
        pyautogui.moveTo(460 + random.randint(0, 5), 180 + random.randint(0, 5), 1, pyautogui.easeInQuad)
        pyautogui.click()
        time.sleep(1)
        _Tools.isWalking.isWalking()
        time.sleep(1)
        _Tools.getCutPicture.window_capture()
        time.sleep(1)
        tiger_location = pyautogui.locateCenterOnScreen("E:\\dh2\\xiuluo\\6.PNG")
        time.sleep(1)
        pyautogui.moveTo(tiger_location[0], tiger_location[1] - 60)
        pyautogui.click()
        # 选择离开
        time.sleep(1)
        pyautogui.moveTo(220 + random.randint(0, 5), 329 + random.randint(0, 5), 1, pyautogui.easeInQuad)
        pyautogui.click()

def findNPC(flag=1):
    # 寻路开始
    time.sleep(1)
    pyautogui.moveTo(38 + random.randint(0, 2), 253 + random.randint(0, 2), 1, pyautogui.easeInQuad)
    pyautogui.click()
    if flag ==1:
        # 打开物品
        time.sleep(1)
        pyautogui.keyDown('alt')
        pyautogui.keyDown('e')
        pyautogui.keyUp('e')
        pyautogui.keyUp('alt')
        # 吃香
        time.sleep(1)
        pyautogui.moveTo(47 + random.randint(0, 2), 435 + random.randint(0, 2), 1, pyautogui.easeInQuad)
        pyautogui.rightClick()
        # 关闭物品
        time.sleep(2)
        pyautogui.keyDown('alt')
        pyautogui.keyDown('e')
        pyautogui.keyUp('e')
        pyautogui.keyUp('alt')
        time.sleep(1)
    else:
        time.sleep(10)
    try:
        # 判断是否需要重点
        time.sleep(2)
        _Tools.isWalking.catchScreen(30, 65, 140, 85, "position")
        time.sleep(2)
        _Tools.isWalking.catchScreen(30, 65, 140, 85, "position0")
        degree = _Tools.isWalking.similarPicture("position", "position0")
        if (degree == 0):
            time.sleep(1)
            pyautogui.moveTo(180 + random.randint(0, 2), 240 + random.randint(0, 2), 1, pyautogui.easeInQuad)
            pyautogui.click()
    except OSError:
        pyautogui.moveTo(182, 242 + random.randint(0, 2), 1, pyautogui.easeInQuad)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(33, 257 + random.randint(0, 2), 1, pyautogui.easeInQuad)
        pyautogui.click()
def click(x, y):
    time.sleep(1)
    pyautogui.moveTo(x, y, 1, pyautogui.easeInQuad)
    pyautogui.click()
def XLstartTask(times):
    # 获取焦点
    pyautogui.moveTo(75 + random.randint(0, 5), 45 + random.randint(0, 5), 2, pyautogui.easeInQuad)
    pyautogui.click()

    for i in range(1, times):
        if i ==1:
            time.sleep(0.5)
            click(113, 609)
            time.sleep(0.5)
            keyBoard('ctrl', 'tab')
            time.sleep(0.5)
            click(113, 609)
            time.sleep(0.5)
            keyBoard('ctrl', 'tab')
            time.sleep(0.5)
            click(113, 609)
            time.sleep(0.5)
            keyBoard('ctrl', 'tab')
            time.sleep(0.5)
            click(113, 609)
            time.sleep(0.5)
            keyBoard('ctrl', 'tab')
            time.sleep(0.5)
            click(113, 609)
            time.sleep(0.5)
            keyBoard('ctrl', 'tab')
        print("------第"+str(i)+"次修罗------")
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        # 打开点图
        pyautogui.keyDown('alt')
        pyautogui.keyDown('1')
        pyautogui.keyUp('1')
        pyautogui.keyUp('alt')
        # 移动到任务人
        pyautogui.moveTo(417, 303, 1, pyautogui.easeInQuad)
        pyautogui.click()
        time.sleep(1)
        _Tools.isWalking.isWalking()
        pyautogui.moveTo(377, 301, 1, pyautogui.easeInQuad)
        pyautogui.click()
        _Tools.isWalking.isWalking()
        # 关闭地图
        pyautogui.keyDown('alt')
        pyautogui.keyDown('1')
        pyautogui.keyUp('1')
        pyautogui.keyUp('alt')
        time.sleep(1)
        # 屏蔽周围的人
        pyautogui.keyDown('alt')
        pyautogui.keyDown('5')
        pyautogui.keyUp('5')
        pyautogui.keyUp('alt')
        time.sleep(1)
        pyautogui.moveTo(349,341)
        pyautogui.click()
        # 点击任务
        while True:
            time.sleep(1.5)
            _Tools.getCutPicture.window_capture()
            time.sleep(1.5)
            location = pyautogui.locateCenterOnScreen("E:\\dh2\\xiuluo\\0.PNG")
            if location != None:
                pyautogui.moveTo(location[0],location[1]-50)
                pyautogui.click()
                time.sleep(1)
                _Tools.getCutPicture.window_capture()
                location_1 = pyautogui.locateCenterOnScreen("E:\\dh2\\xiuluo\\0_1.PNG")
                if location_1 != None:
                    break

        # 点击帮忙
        time.sleep(1)
        pyautogui.moveTo(227 + random.randint(0, 5), 364 + random.randint(0, 5), 1, pyautogui.easeInQuad)
        pyautogui.click()
        time.sleep(2)
        pyautogui.click()

        # 飞起来
        time.sleep(1)
        # pyautogui.keyDown('alt')
        # pyautogui.keyDown('c')
        # pyautogui.keyUp('c')
        # pyautogui.keyUp('alt')
        findNPC()
        time.sleep(40)
        # 判断是否找到NPC
        while True:
            time.sleep(1.5)
            _Tools.getCutPicture.window_capture()
            time.sleep(1.5)
            xiuluo_location = _Tools.getLocation.getPictureLocation("E:\\dh2\\xiuluo\\2.PNG",0.99)
            if(xiuluo_location!=0):
                pyautogui.moveTo(169, 331, 1, pyautogui.easeInQuad)
                time.sleep(1)
                pyautogui.click()
                break
            else:
                findNPC(0)
        # 战斗自动开始
        print("战斗开始")
        time.sleep(0.5)
        doing_fighting(i)
        _Tools.getFighting.isFight(i)
        # 返回
        print("返回")
        time.sleep(2)
        return_location = pyautogui.locateCenterOnScreen("E:\\dh2\\xiuluo\\4.PNG")
        if (return_location != None):
            pyautogui.moveTo(return_location[0] + random.randint(0, 5), return_location[1] + random.randint(0, 2), 1,
                             pyautogui.easeInQuad)
            pyautogui.click()
        # 判断是否掉进了冰窟里
        ice()
        time.sleep(3)
        # 是否需要巫医
        if (i % 10) == 0:
            pyautogui.keyDown('alt')
            pyautogui.keyDown('1')
            pyautogui.keyUp('1')
            pyautogui.keyUp('alt')
            time.sleep(1)
            pyautogui.moveTo(287, 199, 1,pyautogui.easeInQuad)
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(199, 311, 1, pyautogui.easeInQuad)
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(402, 346, 1, pyautogui.easeInQuad)
            pyautogui.click()
            time.sleep(1)
            list = [75, 250, 400, 545, 700]
            for x in list:
                pyautogui.moveTo(x + random.randint(0, 5), 45 + random.randint(0, 5), 1, pyautogui.easeInQuad)
                pyautogui.click()
                time.sleep(1)
                if x ==75:
                    while True:
                        time.sleep(1)
                        _Tools.getCutPicture.window_capture()
                        time.sleep(1)
                        wuyi_location = _Tools.getLocation.getPictureLocation("E:\\dh2\\xiuluo\\8.PNG", 0.9)
                        if wuyi_location!=0:

                            pyautogui.moveTo(332 + random.randint(0, 5), 364 + random.randint(0, 5), 1, pyautogui.easeInQuad)
                            pyautogui.click()
                            break
                else:
                    time.sleep(1)
                    pyautogui.moveTo(332 + random.randint(0, 5), 364 + random.randint(0, 5), 1, pyautogui.easeInQuad)
                    pyautogui.click()
                time.sleep(1)
            pyautogui.moveTo(75 + random.randint(0, 5), 45 + random.randint(0, 5), 1, pyautogui.easeInQuad)
            pyautogui.click()
            time.sleep(1)
            pyautogui.keyDown('alt')
            pyautogui.keyDown('1')
            pyautogui.keyUp('1')
            pyautogui.keyUp('alt')
        #  判断是否有人死了
        time.sleep(1)
        _Tools.getFighting.death()

# XLstartTask(60)







