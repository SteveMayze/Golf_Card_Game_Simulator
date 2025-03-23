# Golf Card Game

## Overview
Golf is a fun and engaging card game that can be played with 2 to 4 players. The objective of the game is to have the lowest score at the end of nine holes (rounds). Each player tries to swap their high-value cards for low-value cards to minimize their score.

## Project Structure
The project is organized into the following directories and files:

- `src/`: Contains the main game logic and classes.
  - `game.py`: Manages the overall game logic, including dealing cards and tracking scores.
  - `card.py`: Represents a playing card with properties like suit, rank, and value.
  - `deck.py`: Represents a deck of cards, including methods for shuffling and dealing.
  - `player.py`: Represents a player in the game, managing their hand and actions.

- `tests/`: Contains unit tests for the game components.
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

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.