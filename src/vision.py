import cv2
import mss
import numpy as np


def get_screen():
    with mss.MSS() as sct:
        return cv2.cvtColor(np.array(sct.grab(sct.monitors[1])), cv2.COLOR_BGRA2BGR)


def get_region(image, x, y, width, height):
    return image[y:y + height, x:x + width]


def compare_images(image, template):
    result = cv2.matchTemplate(
        image,
        template,
        cv2.TM_CCOEFF_NORMED
    )

    _, max_value, _, _ = cv2.minMaxLoc(result)

    return max_value
