import os
import random

import cv2


def set_background(database):
    bg_list = os.listdir(database)
    selected_bg = bg_list[random.randrange(0, len(bg_list))]
    bg_path = os.path.join(database, selected_bg)
    bg_img = cv2.imread(bg_path, cv2.IMREAD_COLOR)

    return bg_img
