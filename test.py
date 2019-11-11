import cv2 as cv
import numpy as np


def template_image():
    target = cv.imread("D:\\dh2\\system\\0.PNG")
    tpl = cv.imread("D:\\dh2\\game\\jiefang\\1.PNG")
    methods = [cv.TM_SQDIFF_NORMED, cv.TM_CCORR_NORMED, cv.TM_CCOEFF_NORMED]
    th, tw = tpl.shape[:2]
    for md in methods:
        result = cv.matchTemplate(target, tpl, md)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0] + tw, tl[1] + th)
        print(br)
        cv.rectangle(target, tl, br, [0, 0, 0])
        # cv.imshow("pipei" + np.str(md), target)


template_image()
# cv.waitKey(0)
# cv.destroyAllWindows()


