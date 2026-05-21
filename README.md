# Sea Battle Game in Python

## Project Overview

This project is a two-player console-based Sea Battle game developed in Python.  
The game simulates a turn-based naval battle where players place ships randomly and use different actions to destroy the opponent’s fleet.

Special abilities such as **Nuke** and **Submarine** add strategic depth to the classic Sea Battle rules.

## Features

- Two-player turn-based gameplay
- Random ship placement (no manual setup required)
- Standard shooting system (hit / miss / sunk)
- Special abilities:
  - **Nuke** - destroys a 4x4 area
  - **Submarine** - attacks an entire row
- Persistent statistics (wins, player history)
- Game logs system
- Clean console-based UI with menu system

## Project Architecture

The project follows a modular OOP structure:
core/
├── game.py # Main game loop and game logic
├── player.py # Player class and player state
├── board.py # Game board logic and mechanics
├── ship.py # Ship model and hit tracking

utils/
├── persistence.py # Saves/loads logs and statistics
├── decorators.py # Logging decorator system
├── validators.py # Input validation utilities

## OOP Design

The system is built using Object-Oriented Programming principles:

### Core Classes:
- **Game** - controls game flow and turns
- **Player** - stores player state, board, and abilities
- **Board** - manages grid, shots, and ship placement
- **Ship** - tracks ship coordinates and damage

### OOP Principles Used:
- Encapsulation (board and player data hidden inside classes)
- Association (Game manages two Player objects)
- Polymorphism (ability system via different action methods)
- Composition (Board contains multiple Ship objects)

## Game Flow

1. Start game from main menu
2. Enter player names
3. Ships are placed automatically
4. Players take turns:
   - Shot
   - Nuclear strike
   - Submarine sweep
5. Board updates after each action
6. Game ends when all ships of a player are destroyed
7. Winner is recorded in persistent stats

## Data Storage

The game uses file-based persistence:

- **JSON/CSV files** store:
  - Match history
  - Win statistics
  - Game logs

Implemented via:
- `PersistenceManager` class

## Testing

The project includes unit testing using Python `unittest`.

Tests cover:
- Board logic (ship placement, hits, misses)
- Game state transitions
- Input validation
- Win condition detection
- Ability effects (nuke, submarine)

## Functional Programming Usage

The project also includes functional programming elements:

- `lambda` functions for simple transformations
- `map()` for coordinate processing
- `filter()` for filtering ship states or logs

## Iterators / Generators

Custom iterators/generators are used for:
- Processing large board data efficiently
- Iterating over ship coordinates
- Handling game logs

## Input Validation

All user inputs are validated using:
- Regex (`re` module)
- Custom validation functions

Ensures correct coordinate format and prevents crashes.

## How to Run

```bash
py main.py
```

## Group Contribution:

### Anuar:
- core/
- data/
### Nurbakyt:
- utils/
- tests/
