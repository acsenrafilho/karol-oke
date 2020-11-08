#from player import vlc_media_player
import player_controls as pc
from general_config import ICONS_SET

import PySimpleGUI as sg


# IDEIAs para implementar: [sg.Listbox(["01001"], size=(10, None)), sg.Button("Próxima Música")]
def start_player_with_controllers(player):
    _init_player(player)

    sg.theme("LightGrey1")
    layout = [
        [sg.Button("+ Vol"), sg.Button("- Vol"), sg.Button("Pause"), sg.Button("Fechar Música")],  # noqa
        ]

    # Create the window
    window = sg.Window("Karol-Oke Controles", layout, keep_on_top=True, location=(0,0))

    event_actions = {
        "+ Vol": pc.increase_volume,
        "- Vol": pc.decrease_volume,
        "Pause": pc.pause,
        "Fechar Música": pc.stop_music,
        "Ok": pc.select_music
    }

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        event_actions[event](player, sg)
        if event == sg.WIN_CLOSED or event == "Fechar Música":
            break

    window.close()


def _init_player(player):
    player.set_fullscreen(True)
    player.play()
