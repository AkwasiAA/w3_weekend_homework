import unittest

from models.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Lily", "paper")

    def test_player_has_name(self):
        expected = "Lily"
        actual = self.player.name
        self.assertEqual(expected, actual)

    def test_player_has_choice(self):
        expected = "paper"
        actual = self.player.choice
        self.assertEqual(expected,actual)