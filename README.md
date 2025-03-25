# Golf Card Game

## Overview
Golf is a fun and engaging card game that can be played with 2 to 4 players. The objective of the game is to have the lowest score at the end of nine holes (rounds). Each player tries to swap their high-value cards for low-value cards to minimize their score. This 
is only a simulator that works through a match by playing a series of games. In each game, the first player to reveal all their hidden
cards stops the game were by the other players are able to have one more turn each. The winner of the game is the payer with the lowest
score. The match is completed when one player exceeds a total score of 100. The winner of the match is the player with the lowest total
score. Should all players exceed 100 by the end of the final game, then the match is considered a draw with no winners.

## Project Structure
The project is organized into the following directories and files:

- `src/`: Contains the main game logic and classes.
  - `match.py`: Manages the overall match logic, including tracking the scores between the games.
  - `game.py`: Manages the overall game logic, including dealing cards and tracking scores.
  - `card.py`: Represents a playing card with properties like suit, rank, and value.
  - `deck.py`: Represents a deck of cards, including methods for shuffling and dealing.
  - `player.py`: Represents a player in the game, managing their hand and actions.

- `tests/`: Contains unit tests for the game components.
  - `test_match.py`: Tests for the Match class.
  - `test_game.py`: Tests for the Game class.
  - `test_card.py`: Tests for the Card class.
  - `test_deck.py`: Tests for the Deck class.
  - `test_player.py`: Tests for the Player class.

- `requirements.txt`: Lists the dependencies required for the project.

## Setup Instructions
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using:
   ```
   pip install -r requirements.txt
   ```

## Running the Simulator
To run the game simulator, execute the following command in your terminal:
```
python -m src.match
```

## Running Tests
To run the unit tests, use the following command:
```
pytest tests/
```

