def increase_volume(player, gui=None):
    audio_step = 10 if player.audio_get_volume() < 100 else 0
    player.audio_set_volume(player.audio_get_volume() + audio_step)


def decrease_volume(player, gui=None):
    audio_step = 10 if player.audio_get_volume() > 0 else 0
    player.audio_set_volume(player.audio_get_volume() - audio_step)


def pause(player, gui=None):
    player.pause()


def stop_music(player, gui=None):
    player.stop()


def select_music(player, gui=None):
    player.set_media()
