import cv2
import numpy as np
from player import _frame_stream
from tools import set_background

SCORE_BACKGROUND = "./score"


def collect_score(monitor):
    bg_img = set_background(SCORE_BACKGROUND)
    clean_bg = np.copy(bg_img)
    music_code = ""

    while True:
        print(music_code)
        _frame_stream(bg_img, monitor)
        digit = cv2.waitKey(0) & 0xFF
        #if chr(digit) in string.digits:
        #    music_code = _update_music_code(music_code, digit)

        #bg_img = _add_digit_in_image(clean_bg, music_code, monitor)