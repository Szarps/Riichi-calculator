#!/usr/bin/env python

# R W G
# p b m
# N S W E

grp1: list = [2, 3, 4]
grp2: list = [5, 4, 3]
grp3: list = [6, 5, 4]
grp4: list = [7, 6, 8]
grp5: list = [2, 2

hand: list = grp1 + grp2 + grp3 + grp4 + grp5
# hand = hand(grp1, grp2, grp3, grp4, grp5)

total_tiles: int = len(hand)

if total_tiles != 14:
    print("Mano invalida")
else:
    print("Mano valida")

print(hand)
