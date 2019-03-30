import pyautogui
import _Tools.getCutPicture
import _Tools.getLocation
import time
import random
# 街坊用
# 206337
def isFighting_JF():
    while(True):
        time.sleep(1)
        _Tools.getCutPicture.window_capture()
        time.sleep(1)
        location = _Tools.getLocation.getPictureLocation("E:\\dh2\\jiefang\\0.PNG", 0.7)
        if(location==0 or location[0]<100):
            break
        # else:
        #     if a == 0:
        #         time.sleep(0.5)
        #         pyautogui.moveTo(677, 166 + random.randint(0, 2), 1, pyautogui.easeInQuad)
        #         pyautogui.click()
        #         time.sleep(1)
        #         a = 1
        #         pyautogui.keyDown('F6')
        #         pyautogui.keyUp('F6')
        #         time.sleep(0.5)
        #         pyautogui.moveTo(204, 337 + random.randint(0, 2), 1, pyautogui.easeInQuad)
        #         pyautogui.click()
        #         time.sleep(0.5)
        #         pyautogui.click()
        #         time.sleep(0.5)
        #         pyautogui.keyDown('alt')
        #         pyautogui.keyDown('8')
        #         pyautogui.keyUp('8')
        #         pyautogui.keyUp('alt')

# 一般战斗判断
def isFight(i):
    print("战斗判断")
    if(i%4==1 and i!=1):
        time.sleep(1)
        model(75)
        model(250)
        model(400)
        model(545)
        model(700)
        model(75)
    time.sleep(1)
    while True:
        time.sleep(1)
        _Tools.getCutPicture.window_capture()
        time.sleep(3)
        location = pyautogui.locateCenterOnScreen("E:\\dh2\\xiuluo\\3.PNG")
        if (location==None):
            break
def model(x):
    time.sleep(1)
    pyautogui.moveTo(x + random.randint(0, 5), 45 + random.randint(0, 5), 1, pyautogui.easeInQuad)
    pyautogui.click()
    time.sleep(1)
    pyautogui.keyDown('alt')
    pyautogui.keyDown('8')
    pyautogui.keyUp('8')
    pyautogui.keyUp('alt')

# 判断是否有人阵亡
def death():
    time.sleep(1.5)
    _Tools.getCutPicture.window_capture()
    time.sleep(1.5)
    list = [75, 250, 400, 545, 700]
    a = []
    for i in range(3, 7):
        time.sleep(0.5)
        location = _Tools.getLocation.getPictureLocation("E:\\dh2\\system\\" + str(i) + "_.png", 0.95)
        if location != 0:
            print(i)
            a.append(i)
            # 获取焦点
            time.sleep(1)
            pyautogui.moveTo(list[i-2] + random.randint(0, 5), 45 + random.randint(0, 5), 1, pyautogui.easeInQuad)
            pyautogui.click()
            # 去除提示
            time.sleep(1)
            pyautogui.moveTo(317 + random.randint(0, 5), 364 + random.randint(0, 5), 1, pyautogui.easeInQuad)
            pyautogui.click()
            # 点击加血
            time.sleep(1)
            pyautogui.moveTo(544, 608, 1, pyautogui.easeInQuad)
            pyautogui.rightClick()
            time.sleep(0.5)
            pyautogui.moveTo(578, 608, 1, pyautogui.easeInQuad)
            pyautogui.rightClick()
            # 点击归队
            time.sleep(1)
            pyautogui.moveTo(location[0] -20, location[1] +20, 1, pyautogui.easeInQuad)
            pyautogui.click()
            # 点击自动归队
            time.sleep(1)
            pyautogui.moveTo(198, 347, 1, pyautogui.easeInQuad)
            pyautogui.click()
            # 点击返回队长
            time.sleep(1)
            pyautogui.moveTo(75, 45, 1, pyautogui.easeInQuad)
            pyautogui.click()
    while True:
        time.sleep(0.5)
        pyautogui.moveTo(419, 401, 1, pyautogui.easeInQuad)
        time.sleep(1)
        _Tools.getCutPicture.window_capture()
        time.sleep(1.5)
        location2 = _Tools.getLocation.getPictureLocation("E:\\dh2\\system\\3.png", 0.95)
        time.sleep(0.5)
        location3 = _Tools.getLocation.getPictureLocation("E:\\dh2\\system\\4.png", 0.95)
        time.sleep(0.5)
        location4 = _Tools.getLocation.getPictureLocation("E:\\dh2\\system\\5.png", 0.95)
        time.sleep(0.5)
        location5 = _Tools.getLocation.getPictureLocation("E:\\dh2\\system\\6.png", 0.95)
        time.sleep(0.5)
        if location2 !=0 and location3 !=0 and location4 !=0 and location5!=0:
            break

