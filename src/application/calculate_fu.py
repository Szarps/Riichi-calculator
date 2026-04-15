#!/usr/bin/env python

# ===Libs===

# ===Modules===
from src.application.tiles import TileTypes as Tile

##################################################

# TODO
# this player class must be separated into it's own file.
# This was created for testing purposes only
class Player:
    seat: str
    is_dealer: bool = False

    def __init__(self, seat: str):
        self.seat = seat
        if self.seat == "TON":
            self.is_dealer = True

# TODO
# need to add functionality for individual meld state (open or closed)
# right now it assumes all are closed or open
def calc_fu(meld_list: list, player, meld_closed: bool) -> int:
    if len(meld_list) != 5:
        raise Exception; print("hand is invalid, please check hand")
        exit()
    value: int = 20

    # TODO
    # need to add function to calculate for tsumo and ron
    # need to account for round wind for yakuhai
    for i in meld_list:
        if len(i) == 2:
            if player.seat in i or Tile.dragon in i: # if it's equal to seat or dragon (yakuhai) +=2
                value += 2
        if i[0] != i[1] and i[0] != i[2]:
            continue
        match len(i):
            case 3:
                if meld_closed:
                    # since we know all are equal just compare one of the group
                    if i[0] in Tile.simple:
                        value += 4
                    else:
                        value += 8

                elif i[0] in Tile.simple:
                    value += 2
                else:
                    value += 4

            case 4:
                if meld_closed:
                    if i[0] in Tile.simple:
                        value += 16
                    else:
                        value += 32

                elif i[0] in Tile.simple:
                    value += 8
                else:
                    value += 16

            case _:
                value += 0

    while value % 10 != 0:
        value += 2
    return value

if __name__ == '__main__':
    pass
