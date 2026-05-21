import unittest

from core.board import Board
from utils.validators import validate_coordinate

class TestGame(unittest.TestCase):
    def test_ship_placement(self):
        board = Board()
        self.assertTrue(board.place_ship(0, 0, 3, True))

    def test_invalid_overlap(self):
        board = Board()
        board.place_ship(0, 0, 3, True)
        self.assertFalse(board.place_ship(0, 1, 2, True))

    def test_hit(self):
        board = Board()
        board.place_ship(0, 0, 1, True)
        self.assertEqual(board.receive_shot(0, 0), "sunk")

    def test_miss(self):
        board = Board()
        self.assertEqual(board.receive_shot(5, 5), "miss")

    def test_regex(self):
        self.assertTrue(validate_coordinate("2x5"))

if __name__ == "__main__":
    unittest.main()