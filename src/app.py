from asm import read_asm_profile, write_asm_profile
from firewall import allow_server_exe_through_filewall
from game import copy_game_engine_ini, write_game_user_ini_settings
from settings import ENABLED_MAPS, say

if __name__ == "__main__":
    say("Env Loaded")
    say("Working for:", ENABLED_MAPS)

    for map_code in ENABLED_MAPS:
        say(map_code)
        existing_profile = read_asm_profile(map_code)
        say("ASM")
        write_asm_profile(map_code, existing_profile)
        say("GameEngine")
        copy_game_engine_ini(map_code)
        say("GameUserSettings")
        write_game_user_ini_settings(map_code)
        say("FireWall")
        allow_server_exe_through_filewall(map_code)
    say("Finished.")
    exit(0)
