import cv2
import numpy as np


def button_info():
    im = cv2.imread("test.png")

    blue = [255, 0, 0]

    y, x = np.where(np.all(im == blue, axis=2))

    unx = np.unique(x)
    uny = np.unique(y)

    button2x = [unx[0]]
    button1x = []
    start = unx[0]
    for i in unx[1:]:
        if start + 1 == i:
            button2x.append(i)
            start = i
        else:
            button1x.append(i)

    button1y = [uny[0]]
    button2y = []
    start = uny[0]
    for i in uny[1:]:
        if start + 1 == i:
            button1y.append(i)
            start = i
        else:
            button2y.append(i)

    return button1x, button1y, button2x, button2y
