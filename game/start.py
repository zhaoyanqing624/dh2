import sys
import os
current_dir = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(current_dir)[0]
sys.path.append(rootPath)
from game.jiefang import JieFang
from game.shimen import ShiMen
from game.bangpai import BangPai
from game.wuhuan import WuHuan
from game.guiwang import GuiWang
from game.houzi import HouZi
from game.xiuluo import XiuLuo

import time,datetime


class Start:
    def __init__(self):
        pass
    def jsyx(self):
        aa1="00:00:00"
        aa2="00:10:00"
        while True:
            jssj=datetime.datetime.strptime(str(datetime.date.today()+datetime.timedelta(days=1))+" 05:48:00",'%Y-%m-%d %H:%M:%S')
            aa=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
            jssj1=datetime.datetime.strptime(str(datetime.date.today())+" {0}".format(aa1),'%Y-%m-%d %H:%M:%S')
            jssj2=datetime.datetime.strptime(str(datetime.date.today())+" {0}".format(aa2),'%Y-%m-%d %H:%M:%S')
            time.sleep(10)
            if aa > str(jssj1) and aa < str(jssj2):
                return True

if __name__ == '__main__':

    fmt = '%Y-%m-%d %a %H:%M:%S'  # 定义时间显示格式
 
    # JieFang().task_start()
    #ShiMen().task_start()
    #BangPai().task_start()
    #Start().jsyx()
    print(time.strftime(fmt, time.localtime(time.time())))
    #XiuLuo().task_start(True)
    #GuiWang().task_start(40)

    list_wangshou = [[530,432],[560,413],[566,370],[512,378],[522,323],[562,271],[520,252],[470,300],[444,328],[415,319],[409,349],[386,396],[382,461],[343,475],[307,461],[270,476],[280,400],[286,375],[270,348],[274,296],[270,247],[370,255],[530,432],[560,413],[566,370],[512,378],[522,323],[562,271],[520,252],[470,300],[444,328],[415,319],[409,349],[386,396],[382,461],[343,475],[307,461],[270,476],[280,400],[286,375],[270,348],[274,296],[270,247],[370,255]]
    HouZi().houzi_task(list_wangshou)
    # WuHuan().task_start(type=1)
    print(time.strftime(fmt, time.localtime(time.time())))
