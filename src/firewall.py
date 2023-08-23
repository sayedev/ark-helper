import ctypes
import subprocess
from os import path

from settings import NAME, SERVERS_PATH, say


def figure_game_exe_location(map_code):
    return path.join(
        SERVERS_PATH,
        map_code,
        "ShooterGame",
        "Binaries",
        "Win64",
        "ShooterGameServer.exe",
    )


def user_is_admin():
    return ctypes.windll.shell32.IsUserAnAdmin() != 0


def allow_server_exe_through_filewall(map_code):
    if not user_is_admin():
        return say("Please run as admin to change firewall settings.")

    command = (
        'netsh advfirewall firewall add rule name="%s: %s" dir=in action=allow program="%s" enable=yes'
        % (NAME, map_code, figure_game_exe_location(map_code))
    )
    return subprocess.call(command, shell=True)
