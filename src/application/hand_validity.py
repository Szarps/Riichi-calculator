#!/usr/bin/env python

# R W G
# N S W E
# p b m
not_valid: str = "Invalid hand"
valid: str = "Valid hand"


def length(hand) -> str:
    hand = list(hand)
    # print(hand)  # debugging
    #
    total_tiles: int = len(hand)
    # print(f"There's a total of {total_tiles} tiles")  # debugging

    if total_tiles != 14:
        return not_valid
    else:
        return valid


if __name__ == '__main__':
    # Just for ease of testing
    length([1, 1, 2, 2, 3, 3, 4, 5, 5, 5, 6, 7, 8, 9])
