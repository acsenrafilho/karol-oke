import glob
import os
import random

import cv2
import vlc

from karoloke.general_config import WND_NAME
from karoloke.gui import start_player_with_controllers
from karoloke.tools import fill_code_space


def start_video(vlc_player, monitor):
    return start_player_with_controllers(vlc_player, monitor)


def vlc_media_player(video_path):
    vlc_instance = vlc.Instance()
    player = vlc_instance.media_player_new()
    media = vlc_instance.media_new(video_path)
    player.set_media(media)

    return player


def choose_music(code, database):
    code = fill_code_space(code)
    video_path = os.path.join(database, code + '.mp4')
    if os.path.exists(video_path):
        return video_path
    return ''


def _frame_stream(frame, monitor):
    # frame = _set_player_layers(frame, monitor)
    cv2.namedWindow(WND_NAME, cv2.WND_PROP_FULLSCREEN)
    cv2.moveWindow(WND_NAME, monitor.x - 1, monitor.y - 1)
    cv2.setWindowProperty(
        WND_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN
    )
    cv2.imshow(WND_NAME, frame)


def random_score_video(score_database):
    videos_list = glob.glob(score_database + '/*.mp4')
    return random.choice(videos_list)
