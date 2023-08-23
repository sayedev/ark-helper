from settings import MAPS, STARTING_PORT

SERVER_PORT_SPACE = 4


def figure_map_offset(position):
    offset = 0
    while position > 0:
        offset += SERVER_PORT_SPACE
        position -= 1
    return offset


def get_game_ports_for_map(map_code):
    offset = figure_map_offset(list(MAPS.values()).index(map_code))
    return {
        "ServerPort": STARTING_PORT + offset,
        "ServerRawPort": STARTING_PORT + offset + 1,
        "QueryPort": STARTING_PORT + offset + 2,
        "RCONPort": STARTING_PORT + offset + 3,
    }
