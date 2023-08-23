from os import makedirs, path

from ports import get_game_ports_for_map
from settings import (
    ASM_CURRENT_CLUSTER_JSON,
    ASM_DEFAULT_JSON,
    ASM_PROFILE_PATH,
    ENABLED_MAPS,
    SERVER_ALIAS,
    SERVERS_PATH,
    say,
    to_dict,
    to_json,
)


def get_asm_profile_name(map_code):
    return path.join(ASM_PROFILE_PATH, "id%s.profile" % map_code)


def read_asm_profile(map_code):
    asm_profile = get_asm_profile_name(map_code)

    if not path.exists(asm_profile):
        say("File not in system:", asm_profile)
        return {}

    content = {}
    with open(asm_profile, mode="r", encoding="utf-8") as profile:
        if not profile.readable():
            say("File is not readable", asm_profile)
            return

        try:
            content = to_dict(profile.read())
        except Exception:
            say("File found but not in json format, ignoring..", asm_profile)

    return content


def write_asm_profile(map_code, content):
    profile_content = content
    default_settings = ASM_DEFAULT_JSON.copy()
    enabled_map_settings = ASM_CURRENT_CLUSTER_JSON.copy()
    ports = get_game_ports_for_map(map_code)

    # Create folder
    install_directory = SERVERS_PATH + map_code
    if not path.exists(install_directory):
        say("Creating Directory:", install_directory)
        makedirs(install_directory)

    # Change the base settings for the profile
    default_settings.update(
        {
            "ProfileID": "id%s" % map_code,
            "ProfileName": map_code.lower(),
            "InstallDirectory": install_directory,
            "ServerName": "%s %s" % (SERVER_ALIAS, map_code),
            "DiscordAlias": map_code.upper(),
            "ServerMap": map_code,
            "ServerPort": ports["ServerPort"],
            "QueryPort": ports["QueryPort"],
            "RCONPort": ports["RCONPort"],
        }
    )

    # Change custom settings
    if map_code in ENABLED_MAPS:
        say("Map has special settings, Adding to profile.")
        default_settings.update(enabled_map_settings)

    # Override the profile content
    profile_content.update(default_settings)
    asm_profile = get_asm_profile_name(map_code)
    with open(asm_profile, mode="w+", encoding="utf-8") as profile:
        profile.write(to_json(profile_content, indent=2))
        say("Wrote Profile for:", asm_profile)
