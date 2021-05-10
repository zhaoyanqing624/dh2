# -*- coding: utf-8 -*-
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
from yitiao.digong import DiGong
from yitiao.guzhu import GuZhu
from yitiao.dayanta import DaYanTa
from yitiao.huaku import HuaKu
from yitiao.qinlin import QinLin

import pyautogui
import datetime
import configparser

class YiTiaoTask():
    def __init__(self):
        cf = configparser.ConfigParser()
        cf.read('task.ini', encoding='utf-8')
        self.team = '3_1'
        self.transform = TransForm()
        self.common = Common()
        self.keyboard = KeyBoard()
        self.screen = Screen()
        self.mouse = Mouse()
        self.digong_level = cf.getint(self.team, 'digong')
        self.dayanta_num = cf.getint(self.team, 'dayanta_num')
        self.dayanta_level = cf.get(self.team, 'dayanta_level').split('@')
        self.guzhu_level = cf.get(self.team, 'guzhu_level').split('@')
        self.huaku_num = cf.getint(self.team, 'huaku_num')
        self.huaku_level = cf.get(self.team, 'huaku_level').split('@')
        self.qinlin_num = cf.getint(self.team, 'qinlin_num')
        self.qinlin_level = cf.get(self.team, 'qinlin_level').split('@')

    def task_classify(self):
        today = datetime.datetime.now().weekday() + 1
        if today is 1:
            print("星期一")
            DiGong().start_task(self.digong_level)
            DaYanTa().start_task(num=self.dayanta_num, level=self.dayanta_level)
            self.common.go_jiudian_wuyi(jiudian=None, wuyi=True)
            HuaKu().start_task(num=self.huaku_num, level=self.huaku_level)

        elif today is 2:
            print("星期二")
            GuZhu().start_task(level=self.guzhu_level)
            self.common.go_jiudian_wuyi(jiudian=None, wuyi=True)
            DaYanTa().start_task(num=self.dayanta_num, level=self.dayanta_level)
            self.common.go_jiudian_wuyi(jiudian=None, wuyi=True)
            self.keyboard.press_shortcut_key('alt', 'c')
            QinLin().start_task(num=self.qinlin_num, level=self.qinlin_level)

        elif today is 3:
            print("星期三")
            DiGong().start_task(self.digong_level)
            HuaKu().start_task(num=self.huaku_num, level=self.huaku_level)
            self.keyboard.press_shortcut_key('alt', 'c')
            QinLin().start_task(num=self.qinlin_num, level=self.qinlin_level)

        elif today is 4:
            print("星期四")
            DiGong().start_task(self.digong_level)
            GuZhu().start_task(level=self.guzhu_level)
            self.common.go_jiudian_wuyi(jiudian=None, wuyi=True)
            DaYanTa().start_task(num=self.dayanta_num, level=self.dayanta_level)

        elif today is 5:
            print("星期五")
            DiGong().start_task(self.digong_level)
            HuaKu().start_task(num=self.huaku_num, level=self.huaku_level)
            self.keyboard.press_shortcut_key('alt', 'c')
            QinLin().start_task(num=self.qinlin_num, level=self.qinlin_level)

        elif today is 6:
            print("星期六")
            GuZhu().start_task(level=self.guzhu_level)
            self.common.go_jiudian_wuyi(jiudian=None, wuyi=True)
            HuaKu().start_task(num=self.huaku_num, level=self.huaku_level)
            self.keyboard.press_shortcut_key('alt', 'c')
            QinLin().start_task(num=self.qinlin_num, level=self.qinlin_level)

        elif today is 7:
            print("星期天")
            DiGong().start_task(self.digong_level)
            GuZhu().start_task(level=self.guzhu_level)
            self.common.go_jiudian_wuyi(jiudian=None, wuyi=True)
            DaYanTa().start_task(num=self.dayanta_num, level=self.dayanta_level)

    def task_start(self):
        self.common.get_focus()
        # 切换宝宝
        for i in range(5):
            self.common.change_dog(1)
            time.sleep(1)
            self.common.change_teamer(times=0.3)
        self.common.make_group()
        self.common.first_operate()
        self.task_classify()



if __name__ == '__main__':
    #     0简单 1难
    YiTiaoTask().task_start()





