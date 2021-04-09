# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from system.screen import Screen

auto_setup(__file__)
class Login():
    # 选择登录人物
    def choose_person(self, number):
        wait(Template(r"tpl1611227252342.png", record_pos=(0.0, 0.086), resolution=(2340, 1079)))
        touch(Template(r"tpl1611409089212.png", record_pos=(0.142, -0.001), resolution=(2340, 1079)))
        sleep(1)
        self.find_person(number)
        touch(Template(r"tpl1611227252342.png", record_pos=(0.0, 0.086), resolution=(2340, 1079)))
        touch(wait(Template(r"tpl1611232699336.png", record_pos=(-0.072, 0.067), resolution=(2340, 1079)), timeout=30,
                   interval=1))
        touch(wait(Template(r"tpl1611232723833.png", record_pos=(0.092, 0.067), resolution=(2340, 1079)), timeout=30,
                   interval=1))
        touch(wait(Template(r"tpl1611278087320.png", record_pos=(-0.0, -0.189), resolution=(1079, 2340)), timeout=30,
                   interval=1))


    # 选择登录人物—递归查找人物
    def find_person(self, number):
        snapshot("screen.png")
        sleep(1)
        result = Screen().get_deal_locations_picture(str(number)+".png", "screen.png", 0.91)
        if result is None or len(result) is 0:
            swipe((1500, 800), (2000, 220), duration=2.5)
            return self.find_person(number)
        else:
            touch(result[0]['result'])

    # 选择退出人物
    def exit(self):
        touch(Template(r"tpl1611677116509.png", record_pos=(0.421, 0.207), resolution=(2340, 1079)))
        sleep(1)
        touch(Template(r"tpl1611677161418.png", record_pos=(0.356, 0.209), resolution=(2340, 1079)))
        sleep(1)
        touch(Template(r"tpl1611677188190.png", record_pos=(0.238, 0.148), resolution=(2340, 1079)))
        sleep(1)
        touch(Template(r"tpl1611677206493.png", record_pos=(0.093, 0.066), resolution=(2340, 1079)))

if __name__ == '__main__':
    connect_device("android:///DWT0118424000554")
    start_app("com.netease.XY2Pocket")
    sleep(2)
    for i in range(1, 21):
        Login().choose_person(number=i)
        print("执行任务")
        sleep(10)
        Login().exit()









