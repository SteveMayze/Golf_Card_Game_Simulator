class Card:
    SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    VALUES = {
        '2': -2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
        'J': 0, 'Q': 10, 'K': 10, 'A': 1, 'Joker': 0
    }

    def __init__(self, suit=None, rank=None):
        if rank == 'Joker':
            self.suit = None  # Jokers do not have a suit
        else:
            self.suit = suit
        self.rank = rank
        self.is_revealed = False

    def get_value(self):
        if self.rank not in self.VALUES:
            raise ValueError(f"Invalid rank: {self.rank}")
        if self.is_revealed:
            return self.VALUES[self.rank]
        else:
            return 0

    def reveal(self):
        self.is_revealed = True
        
    def is_revealed(self):
        return self.is_revealed

    def __str__(self):
        if self.is_revealed:
            return f"{self.rank} of {self.suit}" if self.suit else f"{self.rank}"
        else:
            return "***"

    def __repr__(self):
        if self.is_revealed:
            return f"{self.rank} of {self.suit}" if self.suit else f"{self.rank}"
        else:
            return "***"

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank
    
    