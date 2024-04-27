# Dijkstra-s-algorithm
Shortest Path in Maze using Dijkstra's algorithm. 

# Shortest Path in Maze Solver

This repository contains a Python solution for finding the shortest path through a maze using Dijkstra's algorithm. The program is designed to handle multiple test cases, efficiently navigating through mazes of varying complexity and size.

## Overview

The maze solver reads from an input file, calculates the shortest path using Dijkstra’s algorithm, and outputs the path to a designated file. It showcases a robust implementation of the MinHeap class and demonstrates how to apply it within Dijkstra's to handle graph traversal problems.

## Features

- **Load Test Cases**: A function to load maze configurations, start positions, and destinations from an input file.
  
- **MinHeap Class**: A custom min-heap data structure to support the priority queue required by Dijkstra's algorithm.
  
- **Dijkstra's Shortest Path**: The core algorithm that calculates the shortest path from the start to the destination in the maze.
  
- **Input/Output Handling**: Structured I/O to accept formatted mazes and output the shortest path to an output file.

## How It Works

The code includes several key components:

- **`Load_testcases(filename)`:** Parses input file into test cases.
  
- **`MinHeap`:** Implements heap operations crucial for the performance of Dijkstra's algorithm.
  
- **`getShortestPath(maze, start, destination)`:** Computes the shortest path using the algorithm.
  
- An alternate method suggests the possibility of using Python's built-in `heapq` for heap operations.

## Test Cases

Test cases provided in the input file include:

- Simple mazes with clear paths.
  
- More complex mazes with multiple routes.

Each test case consists of the maze matrix and start-destination coordinates, and the output is the ordered list of coordinates from the start to the destination.

## Input and Output Format

### Sample Input
```python

A) maze = [[1, 3, 2],

           [4, 0, 6],

           [1, 2, 5]]

   start = (0, 0)

   destination = (2, 2)
```

### Sample Output
```
A) Shortest path: [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]
```

## Execution

Upon execution, the solver processes each test case, computes the shortest path, and writes the solution to `outputPS05.txt`, detailing the path for each maze ID.

## Complexity Analysis

The solution ensures an optimal time complexity of O(E log V), where E is the number of edges and V is the number of vertices, indicative of a highly efficient algorithm for pathfinding in mazes.

---

This project is an excellent demonstration of algorithmic efficiency and problem-solving skills in Python, with real-world applicability in pathfinding scenarios such as GPS navigation and robotics.
