from json import dumps as to_json
from json import loads as to_dict
from os import getenv

from dotenv import load_dotenv

load_dotenv()


# -------------
# CONSTANTS
# -------------
VERSION = 0.1
NAME = "[ArkUtil]"
MAPS = {
    "The Island": "TheIsland",
    "The Center": "TheCenter",
    "Scorched Earth": "ScorchedEarth_P",
    "Ragnarok": "Ragnarok",
    "Aberration": "Aberration_P",
    "Extinction": "Extinction",
    "Valguero": "Valguero_P",
    "Genesis: Part 1": "Genesis",
    "Crystal Isles": "CrystalIsles",
    "Genesis: Part 2": "Gen2",
    "Lost Island": "LostIsland",
    "Fjordur": "Fjordur",
}
# -------------
# Config
# Used to make the options in the .INI unique cause configParser is not ready to handle the ARK
# -------------
UNIQUE_CHAR_OPTION = getenv("SERVERS_PATH", "&")
# -------------
# PATHs
# -------------
SERVERS_PATH = getenv("SERVERS_PATH", "")
ASM_PROFILE_PATH = getenv("ASM_PROFILE_PATH", "")
GAME_SERVER_INI = getenv("GAME_SERVER_INI_PATH", "")
GAME_SERVER_USER_INI = getenv("GAME_SERVER_USER_INI_PATH", "")
ASM_DEFAULT_JSON = to_dict(
    open(getenv("ASM_DEFAULT_JSON_PATH", ""), mode="r", encoding="utf-8").read()
)
ASM_CURRENT_CLUSTER_JSON = to_dict(
    open(getenv("ASM_CURRENT_CLUSTER_JSON_PATH", ""), mode="r", encoding="utf-8").read()
)
# -------------
# SERVER
# -------------
SERVER_ALIAS = getenv("SERVER_ALIAS", "")
INSTALLED_MODS = getenv("SERVER_MODS", "")
ASM_SERVER_IP = getenv("ASM_SERVER_IP", "")
# -------------
# ASM JSON Read from env
# -------------
ASM_DEFAULT_JSON.update(
    {
        "ServerPassword": getenv("SERVER_JOIN_PASSWORD", ""),
        "AdminPassword": getenv("SERVER_ADMIN_PASSWORD", ""),
        "ServerModIds": INSTALLED_MODS,
        "CrossArkClusterId": getenv("SERVER_CLUSTER_CODE", ""),
        "DiscordChannelId": getenv("DISCORD_CHANNEL_ID", ""),
    }
)
# -------------
# ArkUtil
# -------------
ENABLED_MAPS = getenv("ENABLED_MAPS", "TheIsland,Ragnarok").split(",")
STARTING_PORT = int(getenv("GAME_STARTING_PORT", 4444))
