
import random
from src.card import Card


class Deck:
    def __init__(self):
        # Create standard cards
        self.cards = [Card(suit, rank) for suit in Card.SUITS for rank in Card.RANKS]
        # Add two Jokers
        self.cards.append(Card(rank='Joker'))
        self.cards.append(Card(rank='Joker'))
        self.discard_pile = []
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards=1):
        if num_cards > len(self.cards):
            raise ValueError("Not enough cards in the deck to deal")   
        dealt_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        if num_cards == 1:
            return dealt_cards[0]
        else:
            return dealt_cards

    def draw_card(self):
        card = self.deal(1)
        card.reveal()
        return card
    
    def remaining_cards(self):
        return len(self.cards)
    
    def add_to_discard_pile(self, old_card):
        self.discard_pile.append(old_card)
        
    def draw_from_discard_pile_card(self):
        drawn_card = self.discard_pile[:1]
        self.discard_pile = self.discard_pile[1:]
        return drawn_card[0]

    def see_top_discard_pile_card(self):
        return self.discard_pile[0] if self.discard_pile else None
    
    def open_top_card(self):
        top_card = self.draw_card()
        top_card.reveal()
        self.add_to_discard_pile(top_card)
        return top_card