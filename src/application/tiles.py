#!/usr/bin/env python

# ===Libs===

# ===Modules===

# The class TileTypes might be unnecesary and could benefit of becoming a list
########################################

class TileTypes:
    simple: tuple = (2, 3, 4, 5, 6, 7, 8)
    terminal: tuple = (1, 9)
    kind: tuple = ("BAMBOO", "MAN", "PIN")
    dragon: tuple = ("CHUN", "HAKU", "HATSU")
    wind: tuple = ("TON", "NAN", "SHAA", "PEI")
    tile_type: dict = {"simple": False, "terminal": False, "honor": False, "wind": False, "dragon": False}


class Tile:
    def __init__(self, args: str):
        self.value = args[0]

        if len(args) == 2:
            self.value = int(args[0])
            if self.value in [i for i in TileTypes.terminal]:
                self.kind = args[1]
                self.tile_type = {"terminal": True}
            else:
                self.kind = args[1]
                self.tile_type = {"simple": True}

        elif args[0] in TileTypes.dragon:
             self.tile_type = {"dragon": True, "honor": True}

        else:
             self.tile_type = {"wind": True, "honor": True}


if __name__ == '__main__':
    tile1 = Tile("9p")
    print(tile1.value, tile1.kind if hasattr(tile1, "kind") else "", tile1.tile_type)
