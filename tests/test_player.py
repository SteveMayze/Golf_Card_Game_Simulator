import unittest
from src.player import Player
from src.card import Card

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Test Player")
        self.card1 = Card("Hearts", "5")
        self.card2 = Card("Diamonds", "10")
        self.card3 = Card("Hearts", "2")
        self.card4 = Card("Diamonds", "3")
        self.card5 = Card("Spades", "8")
        self.card6 = Card("Spades", "J")
        self.player.hand = [ [self.card1, self.card2, self.card3], 
                            [self.card4, self.card5, self.card6] ]

    def test_reveal_cards(self):
        self.player.hand[0][0].reveal()
        self.player.hand[0][1].reveal() 
        self.player.hand[1][1].reveal() 
        self.player.hand[1][2].reveal() 
        revealed_cards = self.player.reveal_cards()
        
        self.assertEqual(revealed_cards, [self.card1, self.card2, self.card5, self.card6])

    def test_swap_card(self):
        new_card = Card("Clubs", "3")
        self.player.swap_card(0, 0, new_card)
        self.assertEqual(self.player.hand[0][0], new_card)

    def test_initial_hand(self):
        self.assertEqual(len(self.player.hand), 2)
        
        
    def test_card_in_column(self):
        #  self.card1 = Card("Hearts", "5")
        #  self.card2 = Card("Diamonds", "10")
        #  self.card3 = Card("Hearts", "2")
        #  self.card4 = Card("Diamonds", "3")
        #  self.card5 = Card("Spades", "8")
        #  self.card6 = Card("Spades", "J")
        
        self.cardx = Card("Hearts", "10")
        self.cardx.reveal()

        self.assertIsNone(self.player.card_in_column(self.cardx))

        self.player.hand = [ [self.card1, self.card2, self.card3], 
                            [self.card4, self.cardx, self.card6] ]

        self.assertIsNone(self.player.card_in_column(self.cardx))

        self.card2.reveal()

        self.assertEqual(self.player.card_in_column(self.cardx), (self.card2, 0, 1))

if __name__ == '__main__':
    unittest.main()