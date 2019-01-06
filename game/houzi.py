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

if __name__ == '__main__':
    img = io.imread('E:\\dh2\\system\\0.png')
    io.imshow(img)
    io.show()