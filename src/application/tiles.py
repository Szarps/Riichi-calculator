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
    tile_types: tuple = ("simple", "terminal", "honor", "dragon", "wind")


class Tile:
    def __init__(self, args: str):
        self.value = args[0]
        self.tile_type: list

        if len(args) == 2:
            self.value = int(args[0])
            if self.value in [i for i in TileTypes.terminal]:
                self.kind = args[1]
                self.tile_type = TileTypes.tile_types[1]
            else:
                self.kind = args[1]
                self.tile_type = TileTypes.tile_types[0]

        elif args[0] in TileTypes.dragon:
             self.tile_type.append(TileTypes.tile_types[2]) # type honor
             self.tile_type.append(TileTypes.tile_types[3]) # type dragon

        else:
             self.tile_type.append(TileTypes.tile_types[2]) # type honor
             self.tile_type.append(TileTypes.tile_types[4]) # type wind


if __name__ == '__main__':
    tile1 = Tile("9p")
    print(tile1.value, tile1.kind if hasattr(tile1, "kind") else "", tile1.tile_type)
