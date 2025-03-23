import unittest
from src.deck import Deck

class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_deck_initialization(self):
        self.assertEqual(len(self.deck.cards), 54)

    def test_shuffle_deck(self):
        original_order = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(original_order, self.deck.cards)

    def test_deal_card(self):
        card = self.deck.deal()
        self.assertIsNotNone(card)
        self.assertEqual(len(self.deck.cards), 53)

    def test_deal_multiple_cards(self):
        cards = self.deck.deal(5)
        self.assertEqual(len(cards), 5)
        self.assertEqual(len(self.deck.cards), 49)

    def test_deal_more_cards_than_available(self):
        cards = self.deck.deal(54)
        self.assertEqual(len(cards), 54)
        self.assertEqual(len(self.deck.cards), 0)   
        with self.assertRaises(ValueError):
            self.deck.deal(1)

if __name__ == '__main__':
    unittest.main()