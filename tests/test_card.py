import unittest
from src.card import Card

class TestCard(unittest.TestCase):

    def test_get_value_ace(self):
        card = Card(suit='Hearts', rank='A')
        self.assertEqual(card.get_value(), 0)
        card.is_revealed = True
        self.assertEqual(card.get_value(), 1)

    def test_get_value_two(self):
        card = Card(suit='Diamonds', rank='2')
        self.assertEqual(card.get_value(), 0)
        card.is_revealed = True
        self.assertEqual(card.get_value(), -2)

    def test_get_value_three(self):
        card = Card(suit='Clubs', rank='3')
        self.assertEqual(card.get_value(), 0)
        card.is_revealed = True
        self.assertEqual(card.get_value(), 3)

    def test_get_value_ten(self):
        card = Card(suit='Clubs', rank='10')
        self.assertEqual(card.get_value(), 0)
        card.is_revealed = True
        self.assertEqual(card.get_value(), 10)

    def test_get_value_jack(self):
        card = Card(suit='Spades', rank='J')
        self.assertEqual(card.get_value(), 0)
        card.is_revealed = True
        self.assertEqual(card.get_value(), 0)

    def test_get_value_queen(self):
        card = Card(suit='Hearts', rank='Q')
        self.assertEqual(card.get_value(), 0)
        card.is_revealed = True
        self.assertEqual(card.get_value(), 10)

    def test_get_value_king(self):
        card = Card(suit='Diamonds', rank='K')
        self.assertEqual(card.get_value(), 0)
        card.is_revealed = True
        self.assertEqual(card.get_value(), 10)

    def test_get_value_invalid_rank(self):
        card = Card(suit='Clubs', rank='Invalid')
        with self.assertRaises(ValueError) as excinfo:
            card.get_value()
        self.assertEqual(str(excinfo.exception), "Invalid rank: Invalid")

if __name__ == '__main__':
    unittest.main()