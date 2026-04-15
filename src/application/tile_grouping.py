#!/usr/bin/env python

# ===Libs===


# ===Modules===
from itertools import permutations

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
E: list = ["CHUN", "HAKU", "HATSU"]
hand: list = [A, B, C, D, E]


def tile_grouping(hand_sorted) -> None:
    # grp1: list = [hand_sorted[0], hand_sorted[1], hand_sorted[2]]
    # grp2: list = [hand_sorted[3], hand_sorted[4], hand_sorted[5]]
    # grp3: list = [hand_sorted[6], hand_sorted[7], hand_sorted[8]]
    # grp4: list = [hand_sorted[9], hand_sorted[10], hand_sorted[11]]
    # grp5: list = [hand_sorted[12], hand_sorted[13]]
    return None

if __name__ == "__main__":
    tile_grouping(hand)
