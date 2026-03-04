# =====Libs=====
import unittest
import random

# =====Imports=====
# Como vas a correr esto desde la raíz, usamos la ruta desde src
from src.main import main

tiles: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

valid = random.choices(tiles, k=14)
not_valid = random.choices(tiles, k=13)


class TestHand(unittest.TestCase):
    def test_valid_hand(self):
        self.assertEqual(main(valid), "Valid hand")
        # 1, 1, 2, 2, 3, 3, 4, 5, 5, 5, 6, 7, 8, 9
        # 1 1 2 2 3 3 4 5 5 5 6 7 8 9

    def test_invalid_hand(self):
        # Verificamos que la mano sea invalida
        self.assertEqual(main(random.choices(not_valid)), "Invalid hand")


# if __name__ == "__main__":
#     unittest.main()
