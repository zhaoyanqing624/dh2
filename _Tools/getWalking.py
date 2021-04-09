import pyautogui
import time
import _Tools.getCutPicture
def isWalking_JF(filename):
    while(True):
        location = pyautogui.locateCenterOnScreen("C:\\dh2\\jiefang\\"+filename+".PNG", grayscale=True)
        if(location!=None):
            break

def isWalking_BP(filename):
    time.sleep(2)
    _Tools.getCutPicture.window_capture()
    time.sleep(1)
    while(True):
        location = pyautogui.locateCenterOnScreen("C:\\dh2\\bangpai\\"+filename+".PNG")
        if(location!=None):
            break
if __name__ == '__main__':
    _Tools.getCutPicture.window_capture()