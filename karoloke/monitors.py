from screeninfo import get_monitors


def select_best_monitor():
    """Choose the monitor with minor resolution to be
    the host. The Karaoke video is placed on the major
    window. (It is assumed 2 monitors)
    """
    monitors = get_monitors()
    monitor_idx = 0
    best_res = monitors[0].height * monitors[0].width
    for m, idx in zip(monitors, range(len(monitors))):
        # TEST com menor resolução para manter as duas telas ativas
        if (m.height * m.width) < best_res:
            monitor_idx = idx
    return monitors[monitor_idx]
