import time
from PIL import ImageGrab
import cv2
import numpy as np
import win32ui,win32con,win32api
import pyautogui
def click(x, y):
    time.sleep(1)
    pyautogui.moveTo(x, y, 1, pyautogui.easeInQuad)
    pyautogui.click()
def isWalking():
    time.sleep(2)
    a = 0
    # 判断是否走到NPC面前
    while True:
        # 截取左上地图坐标
        time.sleep(2)
        if(a % 2)==0:
            time.sleep(1)
            catchScreen(30, 65, 140, 85, "position")
        else:
            time.sleep(1)
            catchScreen(30, 65, 140, 85, "position0")
        degree = similarPicture("position", "position0")
        if (degree == 0):
            break
        a += 1
def grab_screen_1(left,top,right,bottom,addr):
    im = ImageGrab.grabclipboard()
    while True:
        win32api.keybd_event(win32con.VK_SNAPSHOT, 0, 0, 0)
        time.sleep(1)
        win32api.keybd_event(win32con.VK_SNAPSHOT, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(5)
        im = ImageGrab.grabclipboard()
        if im is None:
            print()
        else:
            break
    rect = (left, top, right, bottom)
    im = im.crop(rect)
    # im.show()
    im.save("E:\\dh2\\system\\"+addr+".png")
    # return im

def catchScreen(x,y,w,h,addr):
    bbox = (x, y, w, h)
    im = ImageGrab.grab(bbox)
    im.save("E:\\dh2\\system\\"+addr+".png")


# 计算图片的相似度
def similarPicture(attr1,attr2):
    img1 = cv2.imread("E:\\dh2\\system\\"+attr1+".png")
    img2 = cv2.imread("E:\\dh2\\system\\"+attr2+".png")
    return classify_pHash(img1,img2)
# 平均哈希算法计算
def classify_pHash(image1,image2):
    image1 = cv2.resize(image1,(32,32))
    image2 = cv2.resize(image2,(32,32))
    gray1 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
    # 将灰度图转为浮点型，再进行dct变换
    dct1 = cv2.dct(np.float32(gray1))
    dct2 = cv2.dct(np.float32(gray2))
    # 取左上角的8*8，这些代表图片的最低频率
    # 这个操作等价于c++中利用opencv实现的掩码操作
    # 在python中进行掩码操作，可以直接这样取出图像矩阵的某一部分
    dct1_roi = dct1[0:8,0:8]
    dct2_roi = dct2[0:8,0:8]
    hash1 = getHash(dct1_roi)
    hash2 = getHash(dct2_roi)
    return Hamming_distance(hash1,hash2)
# 输入灰度图，返回hash
def getHash(image):
    avreage = np.mean(image)
    hash = []
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i,j] > avreage:
                hash.append(1)
            else:
                hash.append(0)
    return hash
# 计算汉明距离
def Hamming_distance(hash1,hash2):
    num = 0
    for index in range(len(hash1)):
        if hash1[index] != hash2[index]:
            num += 1
    return num


# while True:
#
# grab_screen_1(30, 65, 140, 85, "position")
# click(616, 140)
# grab_screen_1(50, 65, 140, 85, "position0")
# click(616, 140)


