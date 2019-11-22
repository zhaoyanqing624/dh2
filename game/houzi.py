import time
from system.transform import TransForm
from game.common import Common
from system.keyboard import KeyBoard
from system.screen import Screen
from system.mouse import Mouse
from skimage import io
class HouZi:
    def __init__(self):
        self.transform = TransForm()
        self.common = Common()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.mouse = Mouse()
    def houzi_task(self,place):
        while True:
            self.screen.cut_screen()
            time.sleep(1)
            loc = self.screen.get_location_picture("D:\\dh2\\houzi\\1.png", num=0.7)
            if loc is not 0:
                print(loc)
# if __name__ == '__main__':
#     # 万寿
#     list_wangshou = [[530,432],[520,252],[470,300],[409,349],[382,461],[280,461],[270,339],[270,247]]
#     HouZi().houzi_task(list_wangshou)