from utils import CustomConfigParser
from os import path
from shutil import copyfile

from ports import get_game_ports_for_map
from settings import (
    ASM_DEFAULT_JSON,
    GAME_SERVER_INI,
    GAME_SERVER_USER_INI,
    INSTALLED_MODS,
    SERVER_ALIAS,
    SERVERS_PATH,
)

GAME_INI = "Game.ini"
GAME_USER_SETTINGS_INI = "GameUserSettings.ini"
GAME_USER_SETTINGS_INI_SECTIONS = [
    "SessionSettings",
    "ServerSettings",
    "ServerSettings",
]


def figure_game_ini_location(map_code, target):
    return path.join(
        SERVERS_PATH,
        map_code,
        "ShooterGame",
        "Saved",
        "Config",
        "WindowsServer",
        target,
    )


def copy_game_engine_ini(map_code):
    return copyfile(GAME_SERVER_INI, figure_game_ini_location(map_code, GAME_INI))


def create_game_user_ini_sections(config, sections):
    for section in sections:
        if not config.has_section(section):
            config.add_section(section)
    return config


def write_game_user_ini_settings(map_code):
    location = figure_game_ini_location(map_code, GAME_USER_SETTINGS_INI)
    ports = get_game_ports_for_map(map_code)

    user_settings = CustomConfigParser()
    user_settings.read(GAME_SERVER_USER_INI)

    user_settings = create_game_user_ini_sections(
        user_settings, GAME_USER_SETTINGS_INI_SECTIONS
    )

    user_settings.set(
        "SessionSettings", "SessionName", "%s %s" % (SERVER_ALIAS, map_code)
    )
    user_settings.set("SessionSettings", "Port", str(ports["ServerPort"]))
    user_settings.set("SessionSettings", "QueryPort", str(ports["QueryPort"]))
    user_settings.set("ServerSettings", "RCONPort", str(ports["RCONPort"]))
    user_settings.set("ServerSettings", "activemods", INSTALLED_MODS)
    user_settings.set(
        "ServerSettings", "serverpassword", ASM_DEFAULT_JSON["ServerPassword"]
    )
    user_settings.set(
        "ServerSettings", "serveradminpassword", ASM_DEFAULT_JSON["AdminPassword"]
    )

    with open(location, mode="w+", encoding="utf-8") as game_user_ini:
        user_settings.write(game_user_ini, space_around_delimiters=False)
    return
