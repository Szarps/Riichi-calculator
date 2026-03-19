#!/usr/bin/env python

# ===Libs===

# ===Modules===
import application.hand_length as valid

#####################################
# TODO:
# need to find a way to structure a hand and group tiles together.
# it needs to understand sequences
#
# brute force all combinations, store them in a list and pick higher?
#   group tiles by kind first to watchout for valid paths
#   filter if a group of tiles is a meld or a sequence
#   missing an adjacent number in both directions check for grouping else -> invalid
#####################################
A: list = [2, 2, 2]
B: list = [9, 9, 9]
C: list = [3, 4, 5]
D: list = [1, 1]
E: list = ["R", "R", "R"]
meld_list: list = [A, B, C, D, E]

class Tile:
    simple: tuple = (2, 3, 4, 5, 6, 7, 8)
    terminal: tuple = (1, 9)
    kind: tuple = ("b", "m", "p")
    honor: tuple = ("R", "H", "G")
    wind: tuple = ("E", "S", "W", "N")
    tile_type: tuple = ("simple", "terminal", "honor", "wind", "dragon")
    group_closed: bool

    def __init__(self, tile: str):
        self = tile

meld_closed = True

class Player:
    seat: str
    is_dealer: bool = False

    def __init__(self, seat: str):
        self.seat = seat
        if self.seat == "E":
            self.is_dealer = True


def calc_fu(meld: list):
    for i in meld:
        match len(meld[i]):
            case 3:
                if not meld_closed:
                    if meld[i] in Tile.simple:
                        return 2
                    else: # <- this else is redundant but makes it more readable
                        return 4
                if meld[i] in Tile.simple:
                    return 4
                else:
                    return 8

            case 4:
                if meld[i] not in Tile.simple: # asumimos son todas NO simples
                    if not meld_closed: # si es abierto es la mitad
                        return 16
                    return 32
                elif not meld_closed:
                    return 8
                else:
                    return 16

            case 2:
                if meld[i] in Tile.honor or meld[i] in player.seat: # si es honor (yakuhai) +=2
                    return 2
                else:
                    return 0

            case _:
                return 0


if __name__ == '__main__':
    # if len(*argv) < 14:
    #     raise Exception("Invalid hand")
    player: object = Player("W")
    # calc_fu(meld_list)
    # print(len(meld_list[3]))
