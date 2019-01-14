import time
from system.transform import TransForm
from game.common import Common
from system.keyboard import KeyBoard
from system.screen import Screen
from system.mouse import Mouse


class XiaoGui():
    def __init__(self):
        pass

    def task_start(self):
        time.sleep(2)
        KeyBoard().press_shortcut_key('alt', '1')
        time.sleep(1)
        Mouse().click_element(321, 273)
        time.sleep(3)
        Mouse().click_element(262, 269)
        time.sleep(0.5)
        KeyBoard().press_shortcut_key('alt', '1')
        time.sleep(3)
        KeyBoard().press_shortcut_key('alt', '5')
        time.sleep(1.5)
        Screen().cut_screen()
        time.sleep(1.5)
        zhongkui = Screen().get_location_picture('E:\\dh2\\game\\xiaogui\\0.png')
        if zhongkui is not 0:
            Mouse().click_element(zhongkui[0] - 5, zhongkui[1] - 30)
        Mouse().click_element(237, 399)
        time.sleep(0.5)
        Mouse().click_element(237, 399)

        Mouse().click_element(27, 256)
        time.sleep(1)
        if Common().iswalking() is False:
            Mouse().click_element(zhongkui[0] - 5, zhongkui[1] - 30)
            Mouse().click_element(237, 399)
            time.sleep(0.5)
            Mouse().click_element(237, 399)
            Mouse().click_element(27, 256)
        Common().capation_eat_xiang()
        time.sleep(15)
        Screen().find_ele_picture('game\\xiaogui\\1', 'mouse', 207, 355)
        for i in range(5):
            KeyBoard().press_shortcut_key('alt', '8')
            Common().change_teamer()
            Mouse().click_element(183, 355)
            if i is 4:
                pass
            else:
                Common().score_for_shifu()
        Screen().find_ele_picture('game\\xiaogui\\2', 'mouse', myself=True)
        time.sleep(1)
        Screen().cut_screen()
        box_result = Screen().get_location_picture('E:\\dh2\\game\\xiaogui\\3.png',0.8)
        if box_result is not 0:
            Mouse().click_element(327, 535)
        Common().score_for_shifu()


if __name__ == '__main__':
    Common().get_focus()
    for i in range(60):
        print("第 "+str(i+1)+" 次")
        XiaoGui().task_start()

