import cv2
import time
import pyautogui
import _Tools.getCutPicture
import aircv as ac
def getPictureLocation(filename,num=0.5):
    imsrc = ac.imread('D:\\dh2\\system\\0.png')
    imobj = ac.imread(filename)
    # find the match position
    pos = ac.find_template(imsrc, imobj,num)
    if pos == None:
        return 0
    else:
        return pos['result']

# if __name__ == '__main__':
#         _Tools.getCutPicture.window_capture()
#         loca = getPictureLocation("D:\\dh2\\system\\3\\6_.png",0.98)
#         print(loca)
#         # if loca!=0 and loca[0]>200 and loca[1]>5140:
#         #     pyautogui.moveTo(loca[0], loca[1]-40)
#         #     pyautogui.click()

