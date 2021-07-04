import unittest

from models.player import Player
from models.game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("Akwasi", "rock")
        self.player_2 = Player("Grace", "scissors")
        self.player_3 = Player("John", "rock")

        self.game_1 = Game(self.player_1, self.player_2)
        self.game_2 = Game(self.player_1, self.player_3)

    def test_game_1_winner(self):
        expected = "Player 1 wins!"
        actual = self.game_1.single_game(self.player_1, self.player_2)
        self.assertEqual(expected, actual)

    def test_game_2_returns_none(self):
        expected = None
        actual = self.game_2.single_game(self.player_1, self.player_3)
        self.assertEqual(expected, actual)