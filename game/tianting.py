import time
from system.transform import TransForm
from game.common import Common
from system.keyboard import KeyBoard
from system.screen import Screen
from system.mouse import Mouse
import _Tools.getFighting

class TianTing():
    def __init__(self):
        pass

    def task_start(self,i):
        Screen().cut_screen()
        time.sleep(1.5)
        lijing = Screen().get_location_picture('D:\\dh2\\game\\tianting\\0.png')
        if lijing is not 0:
            Mouse().click_element(184, 396)
        time.sleep(1)
        Common().capation_eat_xiang()
        list = [(108, 239), (163, 240), (46, 256), (100, 255)]
        # 第一只怪
        for j in list:
            Mouse().click_element(j[0], j[1])
            time.sleep(5)
            Screen().find_ele_picture('game\\tianting\\1', 'mouse', 197, 355)
            for i in range(5):
                time.sleep(2)
                KeyBoard().press_shortcut_key('alt', '8')
                Common().change_teamer()
                Mouse().click_element(412, 429)
                if i is 4:
                    pass
                else:
                    Common().score_for_shifu()
            time.sleep(5)
            while True:
                Screen().cut_screen()
                time.sleep(2)
                zidong = Screen().get_location_picture('D:\\dh2\\game\\tianting\\2.png')
                if zidong is 0 or zidong[0]<100:
                    break

        Mouse().click_element(212, 350)
        Mouse().click_element(29, 268)

        time.sleep(10)
        while True:
            Screen().cut_screen()
            time.sleep(2)
            lijing = Screen().get_location_picture('D:\\dh2\\game\\tianting\\0.png',0.9)
            if lijing is not 0:
                # Mouse().click_element(184, 396)
                break
        # _Tools.getFighting.death2()



if __name__ == '__main__':
    for i in range(70):
        print(i)
        TianTing().task_start(i)
