#!/usr/bin/env python

# ===Libs===

# ===Modules===
# from dataclasses import dataclass

########################################

class TileTypes:
    simple: tuple = (2, 3, 4, 5, 6, 7, 8)
    terminal: tuple = (1, 9)
    kind: tuple = ("b", "m", "p")
    dragon: tuple = ("R", "H", "G")
    wind: tuple = ("E", "S", "W", "N")
    tile_type: dict = {"simple": False, "terminal": False, "honor": False, "wind": False, "dragon": False}


class Tile:
    def __init__(self, args: list):
        self.value = args[0]

        if len(args) == 2:
            if args[0] in TileTypes.terminal:
                self.kind = args[1]
                self.tile_type = "terminal"
                print("terminal")
            else:
                self.kind = args[1]
                self.tile_type = "simple"
                print("simple")

        elif args[0] in TileTypes.dragon:
             self.tile_type = {"dragon": True, "honor": True}

        else:
             self.tile_type = {"wind": True, "honor": True}


if __name__ == '__main__':
    tile1 = Tile(["R"])
    print(tile1.value, tile1.kind if tile1.tile_type == False else "", tile1.tile_type)
