import win32gui, win32ui, win32con, win32api
from PIL import Image
import pyautogui
import random, time
import aircv as ac
from system.keyboard import KeyBoard
from system.mouse import Mouse
import cv2 as cv
import numpy as np
from PIL import ImageGrab

class Screen:
    def __init__(self):
        self.keyboard = KeyBoard()
        self.mouse = Mouse()
        pass

    def cut_screen(self):
        hwnd = 0
        hwndDC = win32gui.GetWindowDC(hwnd)
        mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()
        saveBitMap = win32ui.CreateBitmap()
        MoniterDev = win32api.EnumDisplayMonitors(None, None)
        w = MoniterDev[0][2][2]
        h = MoniterDev[0][2][3]
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
        saveDC.SelectObject(saveBitMap)
        saveDC.BitBlt((0, 0), (820, 650), mfcDC, (0, 0), win32con.SRCCOPY)
        saveBitMap.SaveBitmapFile(saveDC, "E:\\dh2\\system\\0.PNG")

    def cut_screen_by_PIL(self, x, y, w, h, file_path):
        bbox = (x, y, w, h)
        im = ImageGrab.grab(bbox)
        im.save(file_path)

    def cut_screen_location(self, width, height, x, y, file_path="E:\\dh2\\system\\1.PNG"):
        try:
            hwnd = 0
            hwndDC = win32gui.GetWindowDC(hwnd)
            mfcDC = win32ui.CreateDCFromHandle(hwndDC)
            saveDC = mfcDC.CreateCompatibleDC()
            saveBitMap = win32ui.CreateBitmap()
            MoniterDev = win32api.EnumDisplayMonitors(None, None)
            w = MoniterDev[0][2][2]
            h = MoniterDev[0][2][3]
            saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
            saveDC.SelectObject(saveBitMap)
            saveDC.BitBlt((0, 0), (width, height), mfcDC, (x, y), win32con.SRCCOPY)
            saveBitMap.SaveBitmapFile(saveDC, file_path)
        except:
            pass

    def find_color_ele(self, x, y, x_offset, y_offset, r1, r2, g1, g2, b1, b2, cut_zone=None):
        if cut_zone == None:
            im = Image.open("E:\\dh2\\system\\0.PNG")
        else:
            im = Image.open("E:\\dh2\\system\\1.PNG")
        img_array = im.load()
        result = None
        for i in range(x - x_offset, x + x_offset):
            for j in range(y - y_offset, y + y_offset):
                if r1 <= img_array[i, j][0] <= r2 and g1 <= img_array[i, j][1] <= g2 and b1 <= img_array[i, j][2] <= b2:
                    result = x, y
        return result

    def get_location_picture(self, filename, num=0.5, cut_zone=None):
        if cut_zone == None:
            imsrc = ac.imread('E:\\dh2\\system\\0.png')
        else:
            imsrc = ac.imread('E:\\dh2\\system\\1.png')
        imobj = ac.imread(filename)
        # find the match position
        pos = ac.find_template(imsrc, imobj, num)
        if pos == None:
            return 0
        else:
            return pos['result']

    def get_locations_picture(self, filename, num=0.5, cut_zone=None):
        if cut_zone == None:
            imsrc = ac.imread('E:\\dh2\\system\\0.png')
        else:
            imsrc = ac.imread('E:\\dh2\\system\\1.png')
        imobj = ac.imread(filename)
        # find the match position
        pos = ac.find_all_template(imsrc, imobj, num)
        if pos == None:
            return 0
        else:
            return pos

    def get_deal_locations_picture(self, filename, mubiao_file,num=0.5):
        imsrc = ac.imread(mubiao_file)
        imobj = ac.imread(filename)
        pos = ac.find_all_template(imsrc, imobj, num)
        if pos == None:
            return 0
        else:
            return pos

    def find_ele_picture(self, file_path, handle=None, k1=None, k2=None):
        while True:
            pyautogui.moveTo(412 + random.randint(0, 5), 590 + random.randint(0, 5), 1, pyautogui.easeInQuad)
            time.sleep(1)
            self.cut_screen()
            time.sleep(1)
            location = self.get_location_picture("E:\\dh2\\" + file_path + ".png", 0.8)
            if location != 0:
                if handle == 'keyboard':
                    self.keyboard.press_shortcut_key(k1, k2)
                elif handle == 'mouse':
                    self.mouse.click_element(k1, k2)
                break

    def template_image(self, file_path, dir_path="E:\\dh2\\system\\0.PNG"):
        list = []
        target = cv.imread(dir_path)
        tpl = cv.imread(file_path)
        methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]
        th, tw = tpl.shape[:2]
        for md in methods:
            result = cv.matchTemplate(target, tpl, md)
            min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
            if md == cv.TM_SQDIFF_NORMED:
                tl = min_loc
            else:
                tl = max_loc
            br = (tl[0] + tw, tl[1] + th)
            list.append(br)
            cv.rectangle(target, tl, br, [0, 0, 0])
        return list

# if __name__ == '__main__':
#     # Screen().cut_screen()
#     # time.sleep(1)
#     print(Screen().get_location_picture("E:\\dh2\\game\\shimen\\1.png",num=0.8))

