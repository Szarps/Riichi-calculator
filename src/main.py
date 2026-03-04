#!/usr/bin/env python

# R W G
# N S W E
# p b m
not_valid: str = "Mano invalida"
valid: str = "Mano valida"


def main(hand) -> str:
    hand = list(hand)
    print(hand)

    total_tiles: int = len(hand)
    print(f"hay un total de {total_tiles} fichas")

    if total_tiles != 14:
        return not_valid
    else:
        return valid


def order_hand() -> None:
    # hand_ordered: list = sorted(hand)
    # grp1: list = [hand_ordered[0], hand_ordered[1], hand_ordered[2]]
    # grp2: list = [hand_ordered[3], hand_ordered[4], hand_ordered[5]]
    # grp3: list = [hand_ordered[6], hand_ordered[7], hand_ordered[8]]
    # grp4: list = [hand_ordered[9], hand_ordered[10], hand_ordered[11]]
    # grp5: list = [hand_ordered[12], hand_ordered[13]]
    None


if __name__ == '__main__':
    main([1, 1, 2, 2, 3, 3, 4, 5, 5, 5, 6, 7, 8, 9])
