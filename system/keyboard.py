import pyautogui
import time


class KeyBoard:
    # 单个键位
    def press_key(self,key,times=0.5):
        time.sleep(times)
        pyautogui.keyDown(key)
        pyautogui.keyUp(key)
    # 组合快捷键
    def press_shortcut_key(self, key1, key2, times=0.5):
        time.sleep(times)
        pyautogui.keyDown(key1)
        pyautogui.keyDown(key2)
        pyautogui.keyUp(key2)
        pyautogui.keyUp(key1)
