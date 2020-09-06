import cv2
from menu import music_selection

import player
import monitors

MUSIC_DB = "./music_list"

monitor = monitors.select_best_monitor()

while True:
    music_code = music_selection(monitor)
    if music_code:
        video_path = player.choose_music(music_code, MUSIC_DB)
        player.play_video(video_path, monitor)

    if cv2.waitKey(28) & 0xFF == ord("q"):
        break
