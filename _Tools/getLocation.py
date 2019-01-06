import cv2
import time
import pyautogui
import _Tools.getCutPicture
import aircv as ac
def getPictureLocation(filename,num=0.5):
    imsrc = ac.imread('E:\\dh2\\system\\0.png')
    imobj = ac.imread(filename)
    # find the match position
    pos = ac.find_template(imsrc, imobj,num)
    if pos == None:
        return 0
    else:
        return pos['result']

# if __name__ == '__main__':
# #     # for a in range(0,200):
#         _Tools.getCutPicture.window_capture()
#         loca = getPictureLocation("E:\\dh2\\houzi\\1.png")
#         print(loca)
#         if loca!=0 and loca[0]>200 and loca[1]>140:
#             pyautogui.moveTo(loca[0], loca[1]-40)
#             pyautogui.click()

