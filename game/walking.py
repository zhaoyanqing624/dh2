import cv2, time
import numpy as np
from system.screen import Screen


class Walking():
    # 差值感知算法
    def dHash(self, img):
        # 缩放8*8
        img = cv2.resize(img, (9, 8), interpolation=cv2.INTER_CUBIC)
        # 转换灰度图
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        hash_str = ''
        # 每行前一个像素大于后一个像素为1，相反为0，生成哈希
        for i in range(8):
            for j in range(8):
                if gray[i, j] > gray[i, j + 1]:
                    hash_str = hash_str + '1'
                else:
                    hash_str = hash_str + '0'
        return hash_str

    # Hash值对比
    def cmpHash(self, hash1, hash2):
        n = 0
        # hash长度不同则返回-1代表传参出错
        if len(hash1) != len(hash2):
            return -1
        # 遍历判断
        for i in range(len(hash1)):
            # 不相等则n计数+1，n最终为相似度
            if hash1[i] != hash2[i]:
                n = n + 1
        return n

    def iswalking(self):
        screen = Screen()
        screen.cut_screen_by_PIL(30, 65, 140, 85, "E:\\dh2\\system\\2.png")
        time.sleep(3)
        screen.cut_screen_by_PIL(30, 65, 140, 85, "E:\\dh2\\system\\2_.png")
        img1 = cv2.imread('E:\\dh2\\system\\2.png')
        img2 = cv2.imread('E:\\dh2\\system\\2_.png')
        hash1 = self.dHash(img1)
        hash2 = self.dHash(img2)
        n = self.cmpHash(hash1, hash2)
        return n


