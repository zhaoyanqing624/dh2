import sys
import os
current_dir = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(current_dir)[0]
sys.path.append(rootPath)
import time
from game.common import Common
from system.transform import TransForm
from system.keyboard import KeyBoard
from system.screen import Screen
from system.mouse import Mouse
import pyautogui

class Login():
    def __init__(self):
        self.transform = TransForm()
        self.common = Common()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.mouse = Mouse()
    def start(self):
        list2 = [198,373,550,720]
        self.common.get_focus()
        user = ['zhaoyq7752857016','zhaoyq7752857017','zhaoyq7752857018','zhaoyq7752857019','zhaoyq7752857020']
        # user = ['liudd87705648011','liudd87705648012','liudd87705648013','liudd87705648014','liudd87705648015']
        pwd = 'zyq19920826'
        for n in range(5):
            self.mouse.click_element(303, 296)
            for i in user[n]:
                self.keyboard.press_key(i)
            self.keyboard.press_key('enter')
            for j in pwd:
                self.keyboard.press_key(j)
            self.mouse.click_element(389, 416)
            time.sleep(3)
            self.mouse.click_element(420, 574)
            time.sleep(5)
            self.mouse.click_element(420, 574)
            time.sleep(3)
            if n <4:
                self.mouse.click_element(list2[n], 40)
                time.sleep(5)
if __name__ == '__main__':
    Login().start()




