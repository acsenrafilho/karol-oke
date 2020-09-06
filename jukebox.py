import cv2
from menu import music_selection

import player
import monitors
from general_config import MUSIC_DB


monitor = monitors.select_best_monitor()

while True:
    music_code = music_selection(monitor)
    if music_code:
        video_path = player.choose_music(music_code, MUSIC_DB)
        player.start_video(video_path, monitor)

    if cv2.waitKey(0) & 0xFF == ord("q") or music_code is None:
        break
