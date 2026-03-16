# =====Libs=====
import unittest
import random

# =====Imports=====
# Tests run from the root folder so the relative path must be noted
from src.application.hand_length import length

tiles: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

valid = random.choices(tiles, k=14)
not_valid = random.choices(tiles, k=13)


class TestHand(unittest.TestCase):
    def test_valid_hand(self):
        self.assertEqual(length(valid), True)
        # 1, 1, 2, 2, 3, 3, 4, 5, 5, 5, 6, 7, 8, 9
        # 1 1 2 2 3 3 4 5 5 5 6 7 8 9

    def test_invalid_hand(self):
        # Verificamos que la mano sea invalida
        self.assertEqual(length(not_valid), False)
