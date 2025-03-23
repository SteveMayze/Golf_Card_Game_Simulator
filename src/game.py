import logging
import random
from src.deck import Deck


logger = logging.getLogger(__name__)

class Game:
    def __init__(self, players):
        self.players = players
        self.deck = None
        self.current_turn = 0
        self.scores = {player: 0 for player in players}
        self.first_player_done = None  # Tracks the first player to finish

    def start_game(self):
        self.deck = Deck()
        self.deck.shuffle()
        for deal_count in range(6): ## 6 cards per player
            for player in self.players:
                player.receive_one_card(self.deck, deal_count)
        for player in self.players:
            player.reveal_initial_cards()
        opening_card = self.deck.open_top_card()
        logger.debug(f"Opening card on the discard pile: {opening_card}")

    def reveal_card(self, player, row, col):
        card = player.reveal_card(row, col)
        return card

    def calculate_score(self):
        for player in self.players:
            self.scores[player] = player.calculate_hand_score()
        return self.scores

    def next_turn(self):
        self.current_turn = (self.current_turn + 1) % len(self.players)

    def is_game_over(self):
        # The game ends when all players have had one turn after the first player finishes
        if self.first_player_done is not None:
            return self.current_turn == self.first_player_done
        return False

    def get_turned_down_cards(self, player):
        turned_down_cards =  []
        for row in range(2):
            for col in range(3):
                if not player.hand[row][col].is_revealed:
                    turned_down_cards.append((row, col))
        return turned_down_cards


    def see_card_on_discard_pile(self):
        return self.deck.see_top_discard_pile_card()
    
    def play_turn(self, player, card_index_to_swap=None, take_from_deck=True):
        
        if take_from_deck:
            new_card = self.deck.draw_card()
            new_card.reveal()
            logger.debug(f"{player.name} drew {new_card} from the deck")
        else:
            new_card = self.deck.draw_from_discard_pile_card()
            logger.debug(f"{player.name} drew {new_card} from the discard pile")
            
        row, col = 0, 0
        if card_index_to_swap is None:
            turned_down_cards = self.get_turned_down_cards(player)
            if turned_down_cards:
                row, col = random.choice(turned_down_cards)
            else:
                # If no turned-down cards remain, mark the player as done
                if self.first_player_done is None:
                    self.first_player_done = self.current_turn
                return  # Skip the rest of the turn logic
            player.hand[row][col].reveal()
            logger.debug(f"{player.name} is swapping a random card at ({row}, {col}) - {player.hand[row][col]}")
        else:
            row, col = card_index_to_swap
            player.hand[row][col].reveal()
            logger.debug(f"{player.name} is swapping a specific card at {card_index_to_swap} - {player.hand[row][col]}")
            
        old_card = player.swap_card(row, col, new_card)
        self.deck.add_to_discard_pile(old_card)

        turned_down_cards = self.get_turned_down_cards(player)
        if len(turned_down_cards) == 0:
            logger.debug(f"{player.name} has finished")
            if self.first_player_done is None:
                self.first_player_done = self.current_turn
                return

        if self.is_game_over():
            logger.debug("Game over!")
            for row, col in turned_down_cards:
                player.hand[row][col].card.reveal()
            return
        self.next_turn()


    def rank_in_hand(self, player, card):
        for col in range(3):  # Iterate over columns
            card1 = player.hand[0][col]  # Card in the first row of the column
            card2 = player.hand[1][col]  # Card in the second row of the column

            if card1.is_revealed and card1.is_revealed and card1.rank != card2.rank:
                if card1.rank == card.rank:  # If the rank matches the given card
                    return (player.hand[1][col], 1, col)  # Return the coordinates of the other card in the column (second row)
                elif card2.rank == card.rank:  # If the rank matches the given card
                    return (player.hand[0][col], 0, col)  # Return the coordinates of the other card in the column (first row)
            else:
                if card1.is_revealed and card1.rank == card.rank:  # If the rank matches the given card
                    return (player.hand[1][col], 1, col)  # Return the coordinates of the other card in the column (second row)
                elif card2.is_revealed and card2.rank == card.rank:  # If the rank matches the given card
                    return (player.hand[0][col], 0, col)  # Return the coordinates of the other card in the column (first row)

        return None  # Return None if no matching rank is found
    
    def would_help_next_player(self, next_player, card):
        """
        Check if the given card would help the next player complete a column of same-ranked cards.
        """
        for revealed_card in next_player.reveal_cards():
            if revealed_card.get_value() == card.get_value():
                return True
        return False