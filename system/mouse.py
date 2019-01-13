import pyautogui
import time

class Mouse:
    # 点击元素
    def click_element(self, x, y, times=1, right=None):
        time.sleep(0.5)
        pyautogui.moveTo(x, y, times, pyautogui.easeInQuad)
        time.sleep(0.5)
        if right is not None:
            pyautogui.rightClick()
        else:
            pyautogui.click()

    def click_element_right(self, x, y, times=1):
        time.sleep(times)
        pyautogui.moveTo(x, y, times, pyautogui.easeInQuad)
        time.sleep(0.5)
        pyautogui.rightClick()

    def click_direct_element(self, x, y):
        time.sleep(0.5)
        pyautogui.moveTo(x, y)
        pyautogui.click()

    def mouse_scroll(self, x):
        time.sleep(0.5)
        pyautogui.scroll(x)

if __name__ == '__main__':
    mouse = Mouse()
    mouse.click_element(280,265)
    time.sleep(3)
    mouse.mouse_scroll(-10)
