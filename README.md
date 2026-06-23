8 Puzzle Solver using Breadth First Search (BFS)

Project Overview
This project solves the classic 8-puzzle problem using the Breadth First Search (BFS) algorithm in Python.
The program explores puzzle states level by level and finds the shortest path from the initial state to the goal state.

Problem Statement
The objective of the 8-puzzle problem is to move the blank tile (represented by 0) to reach the desired goal state.
The blank tile can move:

* Up
* Down
* Left
* Right

The program avoids repeated states and finds the shortest solution using BFS.

Objectives
* Represent the puzzle as a 3×3 board.
* Find the blank tile.
* Generate valid moves.
* Generate child states.
* Implement Breadth First Search.
* Track visited states.
* Reconstruct the solution path.

Algorithm Used

**Breadth First Search (BFS)**
BFS explores the state space level by level and guarantees the shortest solution path.

Dependencies
* Python 3.x
* collections.deque

Project Files
* main.py
* README.md

Features
* Board visualization
* Blank tile detection
* Valid move generation
* Child state generation
* BFS implementation
* Goal state detection
* Solution path reconstruction
