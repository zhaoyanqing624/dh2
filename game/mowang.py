import time
from system.transform import TransForm
from game.common import Common
from system.keyboard import KeyBoard
from system.screen import Screen
from system.mouse import Mouse
from game.walking import Walking

class MoWang:
    def __init__(self):
        self.transform = TransForm()
        self.common = Common()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.mouse = Mouse()
        self.walking = Walking()
    def start(self,index):
        for i in range(index):
            self.mouse.click_direct_element(394,347)
            time.sleep(3)
            self.mouse.click_direct_element(541, 498)
            time.sleep(1)
            self.mouse.click_direct_element(328, 404)
            time.sleep(1)

# if __name__ == '__main__':
#     MoWang().start(36)
#     while True:
#         Screen().cut_screen()
#         result1 = Screen().get_location_picture("D:\\dh2\\game\\bangpai\\9_1.png", num=0.8)
#         result2 = Screen().get_location_picture("D:\\dh2\\game\\bangpai\\9_2.png", num=0.8)
#         if result1 is not 0 or result2 is not 0:
#             print(1)
#             break