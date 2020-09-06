from screeninfo import get_monitors


def select_best_monitor():
    """Choose the best monitor base on the maximum
    resolution
    """
    monitors = get_monitors()
    monitor_idx = 0
    best_res = 0
    for m, idx in zip(monitors, range(len(monitors))):
        if (m.height * m.width) > best_res:
            monitor_idx = idx
    return monitors[monitor_idx]
