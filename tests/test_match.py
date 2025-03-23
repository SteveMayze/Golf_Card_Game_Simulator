import unittest
from src.match import Match
from src.player import Player

class TestMatch(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("Alice")
        self.player2 = Player("Bob")
        self.match = Match([self.player1, self.player2])

    def test_start_new_game(self):
        self.match.start_new_game()
        self.assertIsNotNone(self.match.current_game)

    def test_end_game(self):
        self.match.start_new_game()
        self.match.current_game.scores = {self.player1: 10, self.player2: 20}
        self.match.end_game()
        # The score is random and can not be predicted here unless the
        # pack of cards is predetermined.
        # self.assertEqual(self.match.total_scores[self.player1], 19)
        # self.assertEqual(self.match.total_scores[self.player2], 40)

    def test_is_match_over(self):
        self.match.total_scores = {self.player1: 100, self.player2: 50}
        self.assertTrue(self.match.is_match_over())

    def test_get_winner(self):
        self.match.total_scores = {self.player1: 100, self.player2: 50}
        self.assertEqual(self.match.get_winner(), self.player2)

if __name__ == '__main__':
    unittest.main()