# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from login_phone.login_phone import Login

if __name__ == '__main__':
    # 链接设备
    # connect_device("android:///DWT0118424000554")
    # start_app("com.netease.XY2Pocket")
    # sleep(2)

    for i in range(1, 21):
        print(i)
        Login().choose_person(number=i)








