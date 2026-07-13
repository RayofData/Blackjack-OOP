# Blackjack OOP

A command-line Blackjack game built independently in Python to practice object-oriented programming, inheritance, polymorphism, and separation of responsibilities.

The application supports human and computer-controlled players, betting, dealer behavior, hand evaluation, insurance, double down, payouts, and multiple rounds of gameplay.

## Screenshots

### Game Setup

![Blackjack game setup](assets/start-game.png)

### Gameplay

![Blackjack gameplay](assets/gameplay.png)

## Features

* Human and NPC players
* Multiple players at one table
* Player balance and betting system
* Hit and stand actions
* Double down
* Insurance
* Blackjack detection
* Automatic Ace value adjustment
* Dealer behavior based on standard Blackjack rules
* Win, loss, push, and Blackjack payout handling
* Colored terminal output
* Final player results when leaving the table

## Object-Oriented Design

The project separates game behavior into focused classes rather than placing all logic inside one game loop.

```text
Player
├── Dealer
└── BettingPlayer
    ├── HumanPlayer
    └── NPCPlayer
```

### Inheritance and Polymorphism

`Player` defines shared player behavior, including drawing cards, standing, counting hands, and checking for Blackjack.

`Dealer` and `BettingPlayer` extend the base `Player` class. `HumanPlayer` and `NPCPlayer` then extend `BettingPlayer` and implement their own betting and gameplay decisions.

Methods such as `action()`, `print_hand()`, and `print_seat_name()` are implemented differently depending on the player type. This allows the main game loop to work with different player objects through a shared interface.

### Separation of Responsibilities

| Class           | Responsibility                                                    |
| --------------- | ----------------------------------------------------------------- |
| `Card`          | Stores a card's rank, suit, value, and visibility                 |
| `Hand`          | Stores cards and calculates hand totals, including Ace adjustment |
| `Player`        | Defines shared player actions and Blackjack checks                |
| `BettingPlayer` | Manages balances, bets, insurance, and double down                |
| `HumanPlayer`   | Handles user input and player decisions                           |
| `NPCPlayer`     | Handles automated betting and gameplay decisions                  |
| `Dealer`        | Applies dealer-specific gameplay rules                            |
| `Table`         | Manages seats and active players                                  |
| `Room`          | Tracks players who leave and displays final results               |

The game uses composition alongside inheritance:

* A `Table` contains player objects.
* A `Player` contains one or more `Hand` objects.
* A `Hand` contains `Card` objects.

## Refactoring Experience

The original design stored cards directly on each player. During development, the project was refactored so players contain `Hand` objects instead.

This improved separation of responsibilities by moving card collection and hand-total calculations into the `Hand` class. It also created a stronger foundation for supporting multiple hands per player.

The refactor required changes throughout the game loop, player actions, hand evaluation, and payout logic. Split-hand gameplay was explored during this process but was not completed before the project was shelved.

## Project Structure

```text
Blackjack-OOP/
├── BettingPlayer.py
├── Card.py
├── Dealer.py
├── Hand.py
├── HumanPlayer.py
├── NPCPlayer.py
├── Player.py
├── Room.py
├── Table.py
├── helper.py
├── main.py
├── styling.py
├── assets/
│   ├── start-game.png
│   └── gameplay.png
└── README.md
```

## Requirements

* Python 3
* `colorama`

## Installation

Clone the repository:

```bash
git clone https://github.com/RayofData/Blackjack-OOP.git
cd Blackjack-OOP
```

Run the game:

```bash
python main.py
```


## How to Play

1. Enter the starting balance for each player.
2. Choose the number of human and NPC players.
3. Each player places a bet before cards are dealt.
4. Human players choose whether to hit, stand, or double down.
5. NPC players and the dealer take their turns automatically.
6. The game compares each player's hand against the dealer and calculates payouts.
7. Players may continue playing or leave the table after each round.

## Current Status

The primary Blackjack game loop is functional, and the project is currently shelved.

The project is not under active development, but it may be revisited for additional refactoring and gameplay improvements.

## Possible Future Improvements

* Complete split-hand action handling
* Improve NPC decision-making using Blackjack strategy rules
* Improve input validation

## Skills Demonstrated

* Object-oriented Python
* Inheritance and polymorphism
* Object composition
* Separation of responsibilities
* Multi-file project organization
* State management
* Command-line input handling
* Game-rule implementation
* Iterative refactoring