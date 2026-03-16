#!/usr/bin/env python

# ===Libs===
import application.hand_length as length

# ===Modules===

#####################################
A: list = [2, 2, 2]
B: list = [9, 9, 9]
C: list = [1, 1, 1, 1]
D: list = [3, 4, 5]
E: list = ["R", "R", "R"]
meld_list: list = [A, B, C, D, E]

simple: tuple = (2, 3, 4, 5, 6, 7, 8)
terminal: tuple = (1, 9)
honor: tuple = ("R", "H", "G")
wind: tuple = ("E", "S", "W", "N")
tile_type: tuple = ("simple", "terminal", "honor", "wind")

def length(hand):
    None


def calc_fu(meld):
    for i in meld:
        match len(meld[i]):
            case 3:
                if not meld_closed:
                    if meld[i] == tile_type[0]: # asumimos son todas simples por valor 0
                        return 2
                    else:
                        return 4
                if meld[i] == tile_type[0]:
                    return 4
                return 8

            case 4:
                if meld[i] != tile_type[0]: # asumimos son todas NO simples
                    if not meld_closed: # si es abierto es la mitad
                        return 16
                    return 32
                elif not meld_closed:
                    return 8
                else:
                    return 16

            case 2:
                if meld[i] == tile_type[2] or player.seat == tile_type[1]: # si es honor (yakuhai) +=2
                    return 2
                else:
                    return 0

            case _:
                return 0


if __name__ == '__main__':
    if not length(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13):
        raise "Invalid hand"
    calc_fu(meld_list)
