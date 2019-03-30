from Task.JFTask import JFstartTask as jf_start
from Task.BPTask import BPstartTask as bp_start
from Task.XLTask import XLstartTask as xl_start
from Task.HZTask import HZstartTask as hz_start
from game.bangpai import BangPai
import time
if __name__ == '__main__':
    try:
        jf_start()
        time.sleep(3)
        BangPai().bangpai_start()
    except:
        pass
    # # time.sleep(039223)
    # # bp_start()
    #

    # hz_start(60)
    # # time.sleep(3)
    # xl_start(150)
