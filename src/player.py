import random
import logging

logger = logging.getLogger(__name__)

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = [ [None, None, None], [None, None, None] ]  # 3x2 grid
        self.is_finished = False



    def receive_one_card(self, deck, deal_count):
        # Deal 6 cards and arrange them in a 3x2 grid
        dealt_card = deck.deal(1)
        row = deal_count // 3
        col = deal_count % 3
        self.hand[row][col] = dealt_card
        
    def reveal_initial_cards(self):
        # Generate all possible positions in the 3x2 grid
        all_positions = [(row, col) for row in range(2) for col in range(3)]

        # Randomly select two unique positions
        positions_to_reveal = random.sample(all_positions, 2)

        # Reveal the two selected cards
        for row, col in positions_to_reveal:
            self.reveal_card(row, col)        


    def draw_initial_cards(self, deck):
        # Deal 6 cards and arrange them in a 3x2 grid
        dealt_cards = deck.deal(6)
        self.hand = [
            dealt_cards[:3],  # First row
            dealt_cards[3:]   # Second row
        ]

        # Generate all possible positions in the 3x2 grid
        all_positions = [(row, col) for row in range(2) for col in range(3)]

        # Randomly select two unique positions
        positions_to_reveal = random.sample(all_positions, 2)

        # Reveal the two selected cards
        for row, col in positions_to_reveal:
            self.reveal_card(row, col)
        
    def reveal_card(self, row, col):
        if 0 <= row < 2 and 0 <= col < 3:
            self.hand[row][col].reveal()
            logger.debug(f"{self.name} revealed card at position ({row}, {col}) as {self.hand[row][col]}")
            return self.hand[row][col]
        else:
            raise IndexError("Card position out of range")

    def swap_card(self, row, col, new_card):
        if 0 <= row < 2 and 0 <= col < 3:
            new_card.is_revealed = True
            old_card = self.hand[row][col]
            old_card.is_revealed = True
            self.hand[row][col] = new_card
            return old_card
        else:
            raise IndexError("Card position out of range")

    def calculate_hand_score(self):
        total_score = 0
        for col in range(3):  # Iterate over columns
            card1 = self.hand[0][col]
            card2 = self.hand[1][col]
            if card1.rank == card2.rank:  # Same rank in the column
                total_score += 0  # Net score is zero
            else:
                total_score += card1.get_value() + card2.get_value()
        return total_score

    def reveal_cards(self):
        # Return all cards in the hand
        reveald_cards = []
        for row in range(2):
            for col in range(3):
                card = self.hand[row][col]
                if card.is_revealed:
                    reveald_cards.append(card)
        return reveald_cards

    def highest_valued_card(self):
        highest_coordinates = None
        highest_card = None
        highest_value = float('-inf')  # Start with the smallest possible value

        for row in range(2):  # Iterate over rows
            for col in range(3):  # Iterate over columns
                card = self.hand[row][col]
                if card is not None:  # Ensure the card exists
                    card_value = card.get_value()
                    if card_value > 6 and card_value > highest_value:  # Only consider cards with value > 6
                        highest_value = card_value
                        highest_card = card
                        highest_coordinates = (card, row, col)  # Store the coordinates
        return highest_coordinates

    def card_in_column(self, card):
        for col in range(3):
            card1 = self.hand[0][col]
            card2 = self.hand[1][col]
            if card1.is_revealed and card2.is_revealed and card1.rank == card2.rank:
                if card1.is_revealed and card1 == card:
                    return (card2, 0, col)
                elif card2.is_revealed and card2 == card:
                    return (card1, 0, col)
        return None
    
    
    def rank_in_hand(self, card):
        for col in range(3):  # Iterate over columns
            card1 = self.hand[0][col]  # Card in the first row of the column
            card2 = self.hand[1][col]  # Card in the second row of the column
            # logger.debug(f"{self.name} rank in hand test {card} == {card1} (0, {col}) and {card2} (1, {col})")

            if card1.is_revealed and card1.is_revealed and card1.rank != card2.rank:
                if card1.rank == card.rank:  # If the rank matches the given card
                    return (self.hand[1][col], 1, col)  # Return the coordinates of the other card in the column (second row)
                elif card2.rank == card.rank:  # If the rank matches the given card
                    return (self.hand[0][col], 0, col)  # Return the coordinates of the other card in the column (first row)
            else:
                if card1.is_revealed and card1.rank == card.rank:  # If the rank matches the given card
                    return (self.hand[1][col], 1, col)  # Return the coordinates of the other card in the column (second row)
                elif card2.is_revealed and card2.rank == card.rank:  # If the rank matches the given card
                    return (self.hand[0][col], 0, col)  # Return the coordinates of the other card in the column (first row)

        # logger.debug("No matching rank found")
        return None  # Return None if no matching rank is found

    def __str__(self):
        return self.name