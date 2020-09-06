import os
import random

import cv2


def set_background(database):
    bg_list = os.listdir(database)
    selected_bg = bg_list[random.randrange(0, len(bg_list))]
    bg_path = os.path.join(database, selected_bg)
    bg_img = cv2.imread(bg_path, cv2.IMREAD_COLOR)

    return bg_img


def set_number_position(monitor):
    mw, mh = monitor.width, monitor.height
    return int(0.5 * mh), int(0.425 * mw)


def fill_code_space(code):
    final_code = code
    fill_length = 5 - len(code)
    if fill_length > 0:
        final_code = "0"*fill_length + code
    return final_code
