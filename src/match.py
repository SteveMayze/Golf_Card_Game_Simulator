import logging
from src.game import Game
from src.player import Player

# Configure logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class Match:
    def __init__(self, players):
        self.players = players
        self.total_scores = {player: 0 for player in players}
        self.current_game = None
        self.round = 0

    def start_new_game(self):
        self.current_game = Game(self.players)
        self.current_game.start_game()

    def end_game(self):
        game_scores = self.current_game.calculate_score()
        for player, score in game_scores.items():
            self.total_scores[player] += score

    def is_match_over(self):
        return any(score >= 100 for score in self.total_scores.values())

    def get_winner(self):
        if not self.is_match_over():
            return None
        if all(score >= 100 for score in self.total_scores.values()):
            return None  # Match is a draw if all players have scores over 100
        return min(self.total_scores, key=self.total_scores.get)

    def play_match(self):
        logger.info("Starting a new match!")
        next_dealer = self.players[:1][0]
        self.players = self.players[1:]
        self.players.append(next_dealer)
        while not self.is_match_over():
            self.round +=1
            logger.info(f"Starting a new game {self.round} with {next_dealer} dealing")
            self.start_new_game()

            while not self.current_game.is_game_over():
                
                current_player = self.players[self.current_game.current_turn]
                logger.info(f"{current_player.name}'s hand: {current_player.hand}, score: {current_player.calculate_hand_score()} - Discard pile: {self.current_game.see_card_on_discard_pile()}")

                # Simulate a turn (you can replace this with actual player input logic)
                
                # The options available to the player:
                # Note, a high card is considered anything above 6
                # 1. If the card on the discard pile has the same rank as a card in the player's hand, 
                #    the player can swap the card on the discard pile with the other card in the column so that the
                #    column has two cards of the same rank.
                # 2. Swap a high valued, revealed card with a lower value card on the discard pile
                # 3. Swap a high value card with a card from th deck
                # 4. Select a random card from the turned-down cards
                # 5. Do not swap any cards in the hand that the player to the left has unless there is no other choice.
                
                # We need to set card_index_to_swap:tuple and take_from_deck:boolean based on 
                # the options above. We will simulate the first option here.
                
                last_discarded = self.current_game.see_card_on_discard_pile()
                take_from_deck = True

                # Option 1. Try to match the rank of a column
                column_match = current_player.rank_in_hand( last_discarded)
                
                # Get the next player
                next_player_index = (self.current_game.current_turn + 1) % len(self.players)
                next_player = self.players[next_player_index]

                # Initialize variables for the card to discard
                card_to_discard = None
                swap_card = None
                
                if column_match is not None:
                    take_from_deck = False
                    card_to_discard, row, col = column_match
                    swap_card = (row, col)
                    logger.debug(f"{current_player.name} is trying to match a column by swapping {card_to_discard} {swap_card} with the discard pile {last_discarded} card ")
                else:
                    # Option 2. Swap a high value card with a lower value card on the discard pile
                    swap_card = None
                    highest_card = current_player.highest_valued_card()
                    
                    # is the highest card part of a column match?
                    if highest_card is not None:
                        column_match = current_player.card_in_column( highest_card[0])
                        if column_match is not None:
                            logger.debug(f"{current_player.name} is avoiding swapping a high value card ({highest_card[0]}) as it will break a column match.")
                            highest_card = None
                    
                    if highest_card is not None and highest_card[0].get_value() > last_discarded.get_value():
                        # only swap when the highest card is higher than the card on the discard pile
                        card_to_discard, row, col = highest_card
                        swap_card = (row, col)
                        if last_discarded is not None and card_to_discard.get_value() > last_discarded.get_value():
                            logger.debug(f"{current_player.name} would like to swap the high value card ({card_to_discard}) with the {last_discarded} on the discard pile")
                            take_from_deck = False
                        else:
                            # Option 3. Swap a high value card with a card from the deck
                            logger.debug(f"{current_player.name} would like to swap the high value card ({card_to_discard}) with a card from the deck")
                    else:
                        # Option 4. Select a random card from the turned-down cards
                        logger.debug(f"{current_player.name} is swapping a random, hidden card")
                        swap_card = None
                        
                # Check if the card_to_discard would help the next player
                # If th current player also has a column match, then we can decide to help our neightbor.
                if card_to_discard is not None and card_to_discard.is_revealed and self.current_game.would_help_next_player(next_player, card_to_discard):
                    if  column_match is None:
                        logger.debug(f"{current_player.name} avoids discarding {card_to_discard} as it would help {next_player.name} complete a column.")
                        take_from_deck = True
                        swap_card = None  # Avoid discarding the card
                    else:
                        logger.debug(f"{current_player.name} discards {card_to_discard} even though it would help {next_player.name} complete a column.")
                    
                self.current_game.play_turn(current_player, swap_card, take_from_deck)

                logger.info(f"End of {current_player.name}'s turn! - {current_player.hand}, score: {current_player.calculate_hand_score()}")
            self.end_game()
            logger.info("Game over! Current total scores:")
            for player, score in self.total_scores.items():
                logger.info(f"{player.name}: {score}")
            logger.info(f"===================================================")
            
            next_dealer = self.players[:1][0]
            self.players = self.players[1:]
            self.players.append(next_dealer)

        winner = self.get_winner()
        if winner is None:
            logger.info(f"Match over in {self.round} games! - D R A W !")
        else:
            logger.info(f"Match over in {self.round} games! - The winner is {winner.name} with a total score of {self.total_scores[winner]}!")


if __name__ == "__main__":
    # Create four players
    players = [Player(name) for name in ["Alice", "Bob", "Charlie", "Diana"]]

    # Start the match
    match = Match(players)
    match.play_match()

