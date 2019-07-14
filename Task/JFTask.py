# 街坊
import pyautogui
import random
import time
import _Tools.getCutPicture
import _Tools.getWalking
import _Tools.getFighting
import _Tools.getLocation
from PIL import Image
q = 0
def cicle(x):
    while True:
        pyautogui.moveTo(412 + random.randint(0, 5), 590 + random.randint(0, 5), 1, pyautogui.easeInQuad)
        time.sleep(1)
        _Tools.getCutPicture.window_capture()
        time.sleep(1)
        location = _Tools.getLocation.getPictureLocation("E:\\dh2\\jiefang\\"+x+".png", 0.8)
        if location != 0:
            break
def click(x, y):
    time.sleep(1)
    pyautogui.moveTo(x, y, 1, pyautogui.easeInQuad)
    pyautogui.click()
def start_0():
    # 点击祭坛
    pyautogui.moveTo(410 + random.randint(0, 5), 355 + random.randint(0, 5), 1, pyautogui.easeInQuad)
    pyautogui.click()
    # 点击领取任务
    pyautogui.moveTo(200 + random.randint(0, 5), 325, 1, pyautogui.easeInQuad)
    pyautogui.click()
    # 再点击一次 关闭任务
    time.sleep(1)
    pyautogui.click()
def start(flag):
    # 点击街坊 领取任务
    pyautogui.moveTo(760 + random.randint(0, 5), 180 + random.randint(0, 5), 1, pyautogui.easeInQuad)
    pyautogui.click()

    # 任务过程
    while True:
        start_0()
        result = taskClassify(flag)
        if result is 'ok':
            break
    # 是否战斗
    time.sleep(3)
    _Tools.getFighting.isFighting_JF()
    # 关闭任务
    pyautogui.keyDown('alt')
    pyautogui.keyDown('q')
    pyautogui.keyUp('q')
    pyautogui.keyUp('alt')
    # 回家
    pyautogui.moveTo(773 + random.randint(0, 5), 554, 2, pyautogui.easeInQuad)
    pyautogui.click()
    time.sleep(2)

def goHome():
    time.sleep(3)
    while(True):
        location = pyautogui.locateCenterOnScreen("E:\\dh2\\jiefang\\1_4.PNG", grayscale=True)
        if(location!=None):
            pyautogui.moveTo(location[0] + random.randint(0, 5), location[1], 1, pyautogui.easeInQuad)
            pyautogui.click()
def taskClassify(flag):
    global q
    pyautogui.keyDown('alt')
    pyautogui.keyDown('q')
    pyautogui.keyUp('q')
    pyautogui.keyUp('alt')
    time.sleep(1)
    _Tools.getCutPicture.window_capture()
    time.sleep(1)
    loca = _Tools.getLocation.getPictureLocation("E:\\dh2\\jiefang\\0_1.png")
    if loca == 0:
        location = _Tools.getLocation.getPictureLocation("E:\\dh2\\jiefang\\0_3.png")
        if location !=0:
            pyautogui.moveTo(location[0],location[1])
            time.sleep(1)
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(location[0], location[1]+20)
            pyautogui.click()
            time.sleep(1)
    y = ["1_1","1_2","1_3"]
    time.sleep(3)
    for x in y:
        _Tools.getCutPicture.window_capture()
        location = _Tools.getLocation.getPictureLocation("E:\\dh2\\jiefang\\"+x+".PNG")
        if(location!=0):
            if(x=="1_1"):
                print("寻找公输般")
                if flag is True:
                    clear_task()
                    return "no"
                else:
                    pyautogui.moveTo(location[0] + random.randint(0, 5), location[1], 1, pyautogui.easeInQuad)
                    pyautogui.click()
                    time.sleep(2)
                    _Tools.getWalking.isWalking_JF("1_1_1")
                    # 点击提交
                    pay_location_ = pyautogui.locateCenterOnScreen("E:\\dh2\\jiefang\\1_1_1.PNG", grayscale=True)
                    pyautogui.moveTo(pay_location_[0] + random.randint(0, 5), pay_location_[1], 1, pyautogui.easeInQuad)
                    pyautogui.click()
                    time.sleep(1)
                    pay_location = pyautogui.locateCenterOnScreen("E:\\dh2\\jiefang\\1_1_2.PNG", grayscale=True)
                    pyautogui.moveTo(pay_location[0] + random.randint(0, 5), pay_location[1], 1, pyautogui.easeInQuad)
                    pyautogui.click()
                    return "ok"
            elif(x=="1_2"):
                print("潇潇")
                pyautogui.moveTo(location[0] + random.randint(0, 5), location[1], 1, pyautogui.easeInQuad)
                pyautogui.click()
                time.sleep(1)
                result = find_npc_home()
                click(result[0], result[1])
                click(166, 330)
                time.sleep(2.5)
                _Tools.getCutPicture.window_capture()
                find = _Tools.getLocation.getPictureLocation("E:\\dh2\\jiefang\\1_2.PNG")
                if(find!=0):
                    pyautogui.moveTo(find[0], find[1], 1,pyautogui.easeInQuad)
                    pyautogui.click()
                    time.sleep(2.5)
                    cicle('1_2_2')
                    click(197, 348)
                return "ok"
                # # 探访的坐标
                # tanfang_pos = [[544,303],[483,332],[427,362],[487,391],[544,424],[606,390],[665,360],[606,327]]
                # for x in tanfang_pos:
                #     pyautogui.moveTo(x[0] + random.randint(0, 5), x[1], 1, pyautogui.easeInQuad)
                #     pyautogui.click()
                #     time.sleep(1)
                #     tanfang_location = pyautogui.locateCenterOnScreen("E:\\dh2\\jiefang\\1_2_1.PNG", grayscale=True)
                #     if(tanfang_location!=None):
                #         pyautogui.moveTo(tanfang_location[0] + random.randint(0, 5), tanfang_location[1], 1, pyautogui.easeInQuad)
                #         pyautogui.click()
                #         time.sleep(2.5)
                #         _Tools.getCutPicture.window_capture()
                #         find = _Tools.getLocation.getPictureLocation("E:\\dh2\\jiefang\\1_2.PNG")
                #         if(find!=0):
                #             pyautogui.moveTo(find[0], find[1], 1,pyautogui.easeInQuad)
                #             pyautogui.click()
                #             time.sleep(2.5)
                #             _Tools.getCutPicture.window_capture()
                #             time.sleep(1)
                #             jiefang = _Tools.getLocation.getPictureLocation("E:\\dh2\\jiefang\\1_5.PNG")
                #             if(jiefang==0):
                #                 time.sleep(1)
                #                 _Tools.getWalking.isWalking_JF("1_2_2")
                #                 # 点击提交
                #                 pyautogui.moveTo(201 + random.randint(0, 5), 345, 1, pyautogui.easeInQuad)
                #                 pyautogui.click()
                #                 break

            elif(x=="1_3"):
                print("小妖")
                pyautogui.moveTo(location[0] + random.randint(0, 5), location[1], 1, pyautogui.easeInQuad)
                pyautogui.click()
                time.sleep(1)
                result = find_npc_home()
                click(result[0], result[1])
                click(166, 330)
                time.sleep(2.5)
                _Tools.getCutPicture.window_capture()
                find = _Tools.getLocation.getPictureLocation("E:\\dh2\\jiefang\\1_3_.PNG")
                if(find!=0):
                    pyautogui.moveTo(find[0], find[1], 1,pyautogui.easeInQuad)
                    pyautogui.click()
                    time.sleep(2.5)
                    cicle('1_3_1')
                    click(188, 328)
                    time.sleep(3)
                    if q ==0:
                        do_fighting()
                        q+=1
                        time.sleep(2)
                return "ok"

                # # 探访的坐标
                # tanfang_pos = [[544,303],[483,332],[427,362],[487,391],[544,424],[606,390],[665,360],[606,327]]
                # for x in tanfang_pos:
                #     pyautogui.moveTo(x[0] + random.randint(0, 5), x[1], 1, pyautogui.easeInQuad)
                #     pyautogui.click()
                #     time.sleep(1)
                #     tanfang_location = pyautogui.locateCenterOnScreen("E:\\dh2\\jiefang\\1_2_1.PNG", grayscale=True)
                #     if(tanfang_location!=None):
                #         pyautogui.moveTo(tanfang_location[0] + random.randint(0, 5), tanfang_location[1], 1, pyautogui.easeInQuad)
                #         pyautogui.click()
                #         time.sleep(2.5)
                #         _Tools.getCutPicture.window_capture()
                #         time.sleep(1)
                #         find = _Tools.getLocation.getPictureLocation("E:\\dh2\\jiefang\\1_3.PNG")
                #         if(find!=0):
                #             pyautogui.moveTo(find[0], find[1], 1,pyautogui.easeInQuad)
                #             pyautogui.click()
                #             time.sleep(1)
                #             _Tools.getCutPicture.window_capture()
                #             time.sleep(1)
                #             jiefang = _Tools.getLocation.getPictureLocation("E:\\dh2\\jiefang\\1_5.PNG")
                #             if(jiefang==0):
                #                 time.sleep(1)
                #                 _Tools.getWalking.isWalking_JF("1_3_1")
                #                 # 点击提交
                #                 pyautogui.moveTo(191 + random.randint(0, 5), 328, 1, pyautogui.easeInQuad)
                #                 pyautogui.click()
                #                 break
def clear_task():
    time.sleep(1)
    pyautogui.moveTo(612, 521, 1, pyautogui.easeInQuad)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(170, 332, 1, pyautogui.easeInQuad)
    pyautogui.click()
    time.sleep(1)
    pyautogui.keyDown('alt')
    pyautogui.keyDown('q')
    pyautogui.keyUp('q')
    pyautogui.keyUp('alt')
def click_fast(x, y):
    pyautogui.moveTo(x, y, 0.5, pyautogui.easeInQuad)
    pyautogui.click()
def do_fighting():
    pyautogui.keyDown('f5')
    pyautogui.keyUp('f5')
    click_fast(203, 334)
    time.sleep(1.5)
    keyBoard('alt', 'a', 0.5)
    time.sleep(1)
    keyBoard('alt', '8', 0.5)
def keyBoard(str, str2, time_=1):
    time.sleep(time_)
    pyautogui.keyDown(str)
    pyautogui.keyDown(str2)
    pyautogui.keyUp(str2)
    pyautogui.keyUp(str)
def find_npc_home():
    time.sleep(3)
    result = [0,0]
    list = [[543, 307], [481, 334], [422, 366],
            [480, 396], [541, 427], [597, 395],
            [657, 362], [598, 332]]
    _Tools.getCutPicture.window_capture()
    time.sleep(1)
    im = Image.open("E:\\dh2\\system\\0.PNG")
    img_array = im.load()
    for a in list:
        for i in range(a[0]-15, a[0]+15):
            for j in range(a[1], a[1]+20):
                if img_array[i, j] == (255,0,0):
                    result = a
    return result

def JFstartTask(flag=False):
    # 75  45  250
    global q
    list = [75, 250, 400, 545, 700]
    for x in list:
        q=0
        # 获取焦点
        pyautogui.moveTo(x + random.randint(0, 5), 45 + random.randint(0, 5), 2, pyautogui.easeInQuad)
        pyautogui.click()
        for y in range(0, 10):
            try:
                start(flag)
            except:
                pass


# JFstartTask()

