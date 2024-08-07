# Tic-Tac-Toe w/ Minimax Algorithm

## Introduction
Tic-Tac-Toe is a classic game that many of us played growing up. It's simple, fun, and a great way to pass the time. As a child, I often found myself wishing there was a way to play the game even when I was by myself.
This project brings that childhood wish to life by implementing a Tic-Tac-Toe game that you can play against an AI opponent. The AI uses the Minimax algorithm, a decision-making algorithm that ensures the computer always makes the optimal move. This means you're not just playing against a random opponent, but against a strategically thinking adversary that will challenge your skills and potentially help you improve your own gameplay.
Whether you're looking to practice your Tic-Tac-Toe strategy, explore the basics of game AI, or simply enjoy a game against a tireless opponent, this implementation has got you covered. Let's dive into how it works and how you can play!

## Minimax Algorithm
The Minimax algorithm is a decision-making algorithm used in two-player games, particularly in zero-sum games like Tic-Tac-Toe, Chess, and Go. It's designed to find the optimal move for a player, assuming that the opponent also plays optimally. 

## How Minimax Works
**Tree Representation**:

- The game is represented as a tree, where each node is a game state.
- Branches represent possible moves from that state.
- Leaf nodes are terminal states (win, lose, or draw).

**Recursive Exploration**:

- The algorithm recursively explores all possible moves from the current game state.
- It continues until it reaches a terminal state or a predetermined depth.

**Evaluation**:
Terminal states are assigned values:

- Win for AI: +10
- Win for opponent: -10
- Draw: 0

Non-terminal states are evaluated based on their children.

**Minimax Principle**:

- The AI player aims to maximize its score.
- The opponent is assumed to minimize the AI's score (maximize their own).
- Levels alternate between maximizing and minimizing as the algorithm moves up the tree.

**Backpropagation**:

- The algorithm propagates values up the tree.
- At maximizing levels, it chooses the highest value among children.
- At minimizing levels, it chooses the lowest value.

**Move Selection**:

- The AI selects the move leading to the highest-valued immediate child of the current state.

**Other Optimization**:
- Techniques like Alpha-Beta Pruning can be used to reduce the number of evaluated nodes by eliminating branches that cannot possibly influence the final decision.

## How To Play The Game
1. **Run the Python script** to start the game.
2. The game board is displayed as a 3x3 grid
3. Players take turns placing their symbol (X or O) on the board
4. To make a move, click the desired tile on the board
5. The AI will automatically make its move after the player
6. The game ends when a player wins by forming a line (vertical, horizontal, or diagnal) of same three symbols or when the board is full (draw)

## Reference
Python tic-tac-toe implementation inspiration

[https://realpython.com/tic-tac-toe-python/](https://realpython.com/tic-tac-toe-python/)

For more information about minimax algorithm:

[https://en.wikipedia.org/wiki/Minimax](https://en.wikipedia.org/wiki/Minimax)
[https://www.neverstopbuilding.com/blog/minimax](https://www.neverstopbuilding.com/blog/minimax)