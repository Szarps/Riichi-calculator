#!/usr/bin/env python

# ===Libs===

# ===Modules===

##################################################
A: list = [2, 2, 2]
B: list = [9, 9, 9]
C: list = [3, 4, 5]
D: list = [1, 1]
E: list = ["R", "R", "R"]
hand: list = [A, B, C, D, E]

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

# TODO: Separete the above since it is for testing purposes only
##################################################
def calc_fu(meld: list):
    value: int = 20
    for i in meld:
        if not i[0] is i[1] and not i[0] is i[2]:
            continue
        match len(i):
            case 3:
                if not meld_closed:
                    if all(item in Tile.simple for item in i):
                        value += 2
                    else:
                        value += 4

                if all(item in Tile.simple for item in i):
                    value += 4
                else:
                    print(i)
                    value += 8

            case 4:
                if meld_closed:
                    if all(item in Tile.simple for item in i): # assuming all are simples
                        value += 16
                    else:
                        value += 32

                elif all(item in Tile.simple for item in i): # value is half if open
                    value += 8
                else:
                    value += 16

            case 2:
                if all(item in Tile.simple for item in i) or player.seat in i: # if it's honor (yakuhai) +=2
                    value += 2
                else:
                    value += 0

            case _:
                value += 0

        print(value)
    return value

if __name__ == '__main__':
    player: object = Player("W")
    result: int = calc_fu(hand)
    print(f"{result} fu")
