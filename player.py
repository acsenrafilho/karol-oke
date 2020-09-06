import os

import cv2
#import numpy as np
from ffpyplayer.player import MediaPlayer
from general_config import WND_NAME
from tools import fill_code_space


def start_video(video_path, monitor):
    video = cv2.VideoCapture(video_path)
    fps = int(video.get(cv2.CAP_PROP_FPS))
    player = MediaPlayer(video_path)
    while True:
        grabbed, frame = video.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(fps) & 0xFF == ord("q"):
            break
        _frame_stream(frame, monitor)
        if val != 'eof' and audio_frame is not None:
            # audio
            img, t = audio_frame
    video.release()
    cv2.destroyAllWindows()


def choose_music(code, database):
    code = fill_code_space(code)
    return os.path.join(database, code + ".mp4")


def _frame_stream(frame, monitor):
    #frame = _set_player_layers(frame, monitor)
    cv2.namedWindow(WND_NAME, cv2.WND_PROP_FULLSCREEN)
    cv2.moveWindow(WND_NAME, monitor.x - 1, monitor.y - 1)
    cv2.setWindowProperty(WND_NAME, cv2.WND_PROP_FULLSCREEN,
                          cv2.WINDOW_FULLSCREEN)
    cv2.imshow(WND_NAME, frame)


# def _set_player_layers(frame, monitor):
#     bar = cv2.imread(MUSIC_BAR, cv2.IMREAD_COLOR)
#     mw, mh = monitor.width, monitor.height
#     _, fh, _ = frame.shape
#     _, ih, _ = bar.shape
#     sc_fh, sc_bh = (mh * 0.8) / fh, (mh * 0.2) / fh
#     sc_frame = cv2.resize(frame, (0, 0), None, fy=sc_fh)
#     sc_bar = cv2.resize(bar, (0, 0), None, fy=sc_bh)
#     return _stack_layers([np.zeros((mw, mh, 3)), sc_frame, sc_bar])


# def _stack_layers(layers, reference=0):
#     corr_layers = []
#     higher_w = layers[0].shape[1]
#     for layer in layers:
#         if layer.shape[1] > higher_w:
#             higher_w = layer.shape[1]

#     for layer in layers:
#         padding = higher_w - layer.shape[1]
#         corr_layers.append(cv2.copyMakeBorder(
#             layer, 0, 0, 0, padding, value=[0, 0, 0]))

#     ref_layer = corr_layers[reference]
#     for layer, idx in zip(corr_layers, range(corr_layers)):
#         if not idx == reference:
#             ref_layer = np.add(ref_layer, layer)
