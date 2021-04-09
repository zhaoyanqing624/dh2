import pyautogui
import random
import time
import _Tools.getCutPicture
import _Tools.getWalking
import _Tools.getFighting
import _Tools.getLocation
import _Tools.isWalking


def doing_fighting():
    # 203 334
    for i in range(0, 5):
        if i == 0:
            time.sleep(1.5)
        else:
            time.sleep(0.5)
        if i==0 or i==1 or i==2:
            pyautogui.keyDown('f5')
            pyautogui.keyUp('f5')
            click_fast(203, 334)
            if i == 2:
                keyBoard('alt', 's', 0.5)
                click_fast(203, 334)
                keyBoard('alt', '8', 0.5)
            else:
                keyBoard('alt', 'd', 0.5)
                keyBoard('alt', '8', 0.5)
        else:
            keyBoard('alt', 'd', 0.5)
            keyBoard('alt', 'd', 0.5)
            keyBoard('alt', '8', 0.5)
        keyBoard('ctrl', 'tab', 0.5)

def click(x, y):
    time.sleep(1)
    pyautogui.moveTo(x, y, 1, pyautogui.easeInQuad)
    pyautogui.click()

def click_fast(x, y):
    pyautogui.moveTo(x, y, 0.5, pyautogui.easeInQuad)
    pyautogui.click()

def keyBoard(str, str2, time_=1):
    time.sleep(time_)
    pyautogui.keyDown(str)
    pyautogui.keyDown(str2)
    pyautogui.keyUp(str2)
    pyautogui.keyUp(str)

# 400 333
# def find_monkey():

def hz_start(i_):
    time.sleep(1)
    keyBoard('alt', '2')
    time.sleep(1)
    click(325, 406)
    time.sleep(1)
    click(547, 445)
    time.sleep(15)
    a = 0
    while True:
        a += 1
        time.sleep(1)
        _Tools.getCutPicture.window_capture()
        time.sleep(1)
        loca = _Tools.getLocation.getPictureLocation("C:\\dh2\\houzi\\1.png", 0.6)
        if loca == 0:
            if a < 15:
                pyautogui.moveTo(412, 132)
            elif a >= 15 and a < 29:
                pyautogui.moveTo(282, 586)
            elif a >= 29 and a < 44:
                pyautogui.moveTo(412, 132)
            elif a >= 44 and a < 58:
                pyautogui.moveTo(282, 586)
            elif a >= 58 and a < 73:
                pyautogui.moveTo(412, 132)
            else:
                break
            pyautogui.rightClick()
        else:
            if 100 < loca[0] < 800 and 120 < loca[1] < 700:
                pyautogui.moveTo(loca[0] + 70, loca[1] + 70)
                pyautogui.rightClick()
                time.sleep(2)
                flag = False
                locationx = 0
                locationy = 0
                for i in range(0, 50):
                    time.sleep(0.5)
                    _Tools.getCutPicture.window_capture()
                    time.sleep(0.5)
                    loca22 = _Tools.getLocation.getPictureLocation("C:\\dh2\\houzi\\1.png", 0.7)
                    if loca22 != 0:
                        locationx = loca22[0]
                        locationy = loca22[1]
                        pyautogui.moveTo(loca22[0], loca22[1] - 40)
                        pyautogui.click()
                        time.sleep(0.5)
                        _Tools.getCutPicture.window_capture()
                        time.sleep(0.5)
                        location = _Tools.getLocation.getPictureLocation("C:\\dh2\\houzi\\2.png", 0.6)
                        if location != 0:
                            flag = True
                            break
                    else:
                        pyautogui.moveTo(locationx+random.randint(10,20), locationy+random.randint(10,20))
                        pyautogui.click()

                if flag == True:
                    click(307, 348)
                    if i_ == 0:
                        time.sleep(2)
                        # doing_fighting()
                    time.sleep(8)
                    _Tools.getFighting.isFight(i_)

                    # 返回长安
                    keyBoard('alt', '2')
                    time.sleep(1)
                    click(502, 421)
                    time.sleep(1)
                    click(466, 209)
                    time.sleep(1)
                    time.sleep(10)
                    cicle('3')
                    click(202, 395)
                    time.sleep(1)
                    break
            else:
                if a < 14:
                    pyautogui.moveTo(412, 132)
                elif a >= 14 and a < 28:
                    pyautogui.moveTo(282, 586)
                elif a >= 28 and a < 43:
                    pyautogui.moveTo(412, 132)
                elif a >= 43 and a < 58:
                    pyautogui.moveTo(282, 586)
                elif a >= 58 and a < 73:
                    pyautogui.moveTo(412, 132)
                else:
                    break
                pyautogui.rightClick()
                time.sleep(1)


def cicle(x):
    while True:
        pyautogui.moveTo(412 + random.randint(0, 5), 590 + random.randint(0, 5), 1, pyautogui.easeInQuad)
        time.sleep(1)
        _Tools.getCutPicture.window_capture()
        time.sleep(1)
        location = _Tools.getLocation.getPictureLocation("C:\\dh2\\houzi\\" + x + ".png", 0.9)
        if location != 0:
            break


def HZstartTask(times):
    click(75, 45)
    time.sleep(1)
    click(181, 196)
    for i in range(0, times):
        if i != 0 and i % 10 == 0:
            time.sleep(0.5)
            click(46, 611)
            time.sleep(0.5)
            keyBoard('ctrl', 'tab')
            time.sleep(0.5)
            click(46, 611)
            time.sleep(0.5)
            keyBoard('ctrl', 'tab')
            time.sleep(0.5)
            click(46, 611)
            time.sleep(0.5)
            keyBoard('ctrl', 'tab')
            time.sleep(0.5)
            click(46, 611)
            time.sleep(0.5)
            keyBoard('ctrl', 'tab')
            time.sleep(0.5)
            click(46, 611)
            time.sleep(0.5)
            keyBoard('ctrl', 'tab')
        hz_start(i)
    time.sleep(1)
    click(13, 211)
    time.sleep(1)
    keyBoard('alt', '2')
    time.sleep(1)
    click(410, 163)
    time.sleep(0.5)
    click(400, 330)
    time.sleep(40)
    keyBoard('alt', 'c')
# if __name__ == '__main__':
#     HZstartTask(30)
# HZstartTask(30)