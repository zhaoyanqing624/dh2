from win32api import GetSystemMetrics


class TransForm:
    def get_screen_size(self):
        width = GetSystemMetrics(0)
        height = GetSystemMetrics(1)
        return width, height

    def trans_location(self, x, flag):
        size = self.get_screen_size()
        x_ = 0
        if flag == 0:
            x_ = x / 1366 * size[0]
        else:
            x_ = x / 768 * size[1]
        return x_

# if __name__ == '__main__':
#     trn = Transform()
#     print(trn.get_screen_size())
