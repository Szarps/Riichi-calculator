#!/usr/bin/env python

# Currently not up to date with calculate_fu.py, testing is rather invalid
# results don't reflect valid tests cases for the amount of fu

# =====Libs=====
import unittest
import random

# =====Imports=====
# Tests run from the root folder so the relative path must be noted
from src.application.calculate_fu import *

##################################################
A: list = [2, 2, 2]
B: list = [9, 9, 9]
C: list = [3, 4, 5]
D: list = [1, 1]
E: list = ["CHUN", "CHUN", "CHUN"]
# maybe each list can have a bool for open or closed, making it simple
hand: list = [A, B, C, D, E]

meld_closed = True

# tiles: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

seats: tuple = ("TON", "NAN", "SHAA", "PEI")

valid_seat = random.choice(seats)

player = Player(valid_seat)
##################################################

class TestCalcuateFu(unittest.TestCase):
    def test_valid_fu(self):
        self.assertEqual(calc_fu(hand, player, meld_closed:=True), True)
        # 1, 1, 2, 2, 3, 3, 4, 5, 5, 5, 6, 7, 8, 9 # 1 1 2 2 3 3 / 4 5 5 5 6 / 7 8 9
    def test_invalid_fu(self):
        # Verify the amount of fu is correct
        self.assertEqual(calc_fu(hand, player, meld_closed:=True), False)

if __name__ == '__main__':
    # player: object = Player("SHAA")
    # result: int = calc_fu(hand, player, meld_closed:=True)
    # print(f"{result} fu")
    pass
