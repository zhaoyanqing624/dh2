import time
from game.common import Common
from system.transform import TransForm
from system.keyboard import KeyBoard
from system.screen import Screen
from system.mouse import Mouse
import _Tools.getFighting
class BiDou():
    def __init__(self):
        self.transform = TransForm()
        self.common = Common()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.mouse = Mouse()

    def task_start(self):
        print("任务开始")
        self.common.get_focus()
        self.keyboard.press_shortcut_key('alt', 'o')
        self.mouse.click_element(248, 385)
        self.mouse.click_element(547, 420)
