#!/usr/bin/env python

def length(*args) -> bool:
    total_tiles: int = len(*args)
    # print(f"There's a total of {total_tiles} tiles")  # debugging

    if total_tiles < 14:
        return False
    else:
        return True


if __name__ == '__main__':
    # Just for ease of testing
    length([1, 1, 2, 2, 3, 3, 4, 5, 5, 5, 6, 7, 8, 9])
