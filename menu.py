import string

import cv2
import numpy as np

from general_config import MENU_BACKGROUND_DB
from player import _frame_stream
from tools import set_background, set_number_position


def music_selection(monitor):
    bg_img = set_background(MENU_BACKGROUND_DB)
    clean_bg = np.copy(bg_img)
    music_code = ''

    while True:
        print(music_code)
        _frame_stream(bg_img, monitor)
        digit = cv2.waitKey(0) & 0xFF
        if chr(digit) in string.digits:
            music_code = _update_music_code(music_code, digit)

        bg_img = _add_digit_in_image(clean_bg, music_code, monitor)

        if chr(digit) == 'q':  # wait for ESC key to exit
            cv2.destroyAllWindows()
            return None

        if chr(digit) == '\r':
            cv2.destroyAllWindows()
            return music_code


def _update_music_code(code, digit):
    final_code = code
    if chr(digit) in string.digits and len(final_code) < 5:
        final_code = final_code + chr(digit)
        return final_code
    return ''


def _add_digit_in_image(image, music_code, monitor):
    img_txt = np.copy(image)
    position = set_number_position(monitor)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img_txt, music_code, position, font, 2, (255, 0, 0), 5)
    return img_txt
