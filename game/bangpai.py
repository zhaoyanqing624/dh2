import time
from system.transform import TransForm
from game.common import Common
from system.keyboard import KeyBoard
from system.screen import Screen
from system.mouse import Mouse


class BangPai:
    def __init__(self):
        self.transform = TransForm()
        self.common = Common()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.mouse = Mouse()

    def find_bangpai_task(self):
        # 寻找NPC
        self.common.get_focus()
        self.common.clear_task()
        self.screen.cut_screen()
        result_task = self.screen.get_location_picture('E:\\dh2\\game\\system\\task\\1.png')
        self.mouse.click_element(result_task[0] + 50, result_task[1], 0.7)

        self.screen.cut_screen()
        result_task_bangpai = self.screen.get_location_picture('E:\\dh2\\game\\system\\task\\2.png')
        self.mouse.click_element(result_task_bangpai[0] + 50, result_task_bangpai[1], 0.7)
        self.mouse.click_element(428, 240)
        time.sleep(5)
        # 领取任务
        self.screen.find_ele_picture('game\\bangpai\\0', 'mouse', 223, 329)
        self.mouse.click_element(160, 350)
        self.screen.cut_screen_location(267, 136, 373, 209)
        for i in range(0, 1):
            file_name = "E:\\dh2\\game\\bangpai\\" + i + ".png"
            result = self.screen.get_location_picture(file_name, 0.8, True)
            if result != 0:
                if i == 1:
                    print("除草")
                    self.keyboard.press_shortcut_key('alt', 'q')
                    for j in range(10):
                        self.mouse.click_element_right(10, 582)
                        time.sleep(1)
                        self.mouse.click_element(787, 539)
                    self.return_bangpai_npc()
                elif i == 2:
                    print("武官")
                    self.keyboard.press_shortcut_key('alt', 'q')
                    time.sleep(25)
                    self.screen.find_ele_picture('game\\bangpai\\2_1', 'mouse', 193, 327)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    self.mouse.click_element(506, 241)
                    self.keyboard.press_shortcut_key('alt', 'q')
                    time.sleep(20)
                    self.screen.find_ele_picture('game\\bangpai\\2_2', 'mouse', 193, 327)
                    self.return_bangpai_npc()

    def return_bangpai_npc(self):
        self.keyboard.press_shortcut_key('alt', 'q')
        self.mouse.click_element(517, 239)
        self.keyboard.press_shortcut_key('alt', 'q')
        time.sleep(5)
        self.screen.find_ele_picture('game\\bangpai\\0_1', 'mouse', 193, 327)
        self.mouse.click_element(193, 327)
        time.sleep(3)
        self.mouse.click_element(460, 290)


if __name__ == '__main__':
    ba = BangPai()
    ba.find_bangpai_task()
