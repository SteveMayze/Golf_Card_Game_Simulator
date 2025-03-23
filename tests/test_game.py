import unittest
from src.game import Game
from src.card import Card
from src.deck import Deck
from src.player import Player
from copy import deepcopy


class TestGame(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("Alice")
        self.player2 = Player("Bob")
        self.game = Game([self.player1, self.player2])

    def test_start_game(self):
        self.game.start_game()
        self.assertEqual( sum(len(x) for x in self.player1.hand), 6)
        self.assertEqual( sum(len(x) for x in self.player2.hand), 6)

    def test_calculate_score(self):
        # Assuming the cards have been dealt and we can calculate the score
        self.player1.hand = [[Card('Hearts', '2'), Card('Diamonds', '3'), Card('Clubs', '4')], [Card('Spades', '5'), Card('Hearts', '6'), Card('Clubs', '7')]]
        self.player2.hand = [[Card('Hearts', '8'), Card('Diamonds', '6'), Card('Clubs', 'J')], [Card('Diamonds', '8'), Card('Hearts', '9'), Card('Clubs', '10')]]
        self.assertEqual(self.game.calculate_score()[self.player1], 0)  # Example score
        self.assertEqual(self.game.calculate_score()[self.player2], 0)  # Example score
        for row in range(2):
            for col in range(3):
                self.player1.hand[row][col].reveal()
                self.player2.hand[row][col].reveal()
        self.assertEqual(self.game.calculate_score()[self.player1], 23)  # Example score
        self.assertEqual(self.game.calculate_score()[self.player2], 25)  # Example score

    def test_reveal_card(self):
        self.game.start_game()
        revealed_card = self.game.reveal_card(self.player1, 0, 0)
        self.assertIsInstance(revealed_card, Card)

    def test_play_turn(self):
        self.game.start_game()
        ## initial_hand = self.player1.hand[:]
        initial_hand = deepcopy(self.player1.hand)
        self.game.play_turn(self.player1, (0,0), take_from_deck=True)
        self.assertNotEqual(self.player1.hand, initial_hand)
        self.assertEqual( sum(len(x) for x in self.player1.hand), 6)

    def test_play_turn_with_random_selection(self):
        self.game.start_game()
        initial_hand = deepcopy(self.player1.hand)
        self.game.play_turn(self.player1, take_from_deck=True)
        self.assertNotEqual(self.player1.hand, initial_hand)
        self.assertEqual( sum(len(x) for x in self.player1.hand), 6)

if __name__ == '__main__':
    unittest.main()