import puzzle8 as p8
import heapq
from typing import List
import time
from bfs import *
from itdeep import *

solution = p8.solution()
solutionPosition = {}

currentPosition = {}

Square_to_Position_Solution = {}
Square_to_Position_Current = {}

# Create a dictionary that maps square to location and location to tiles of the solution


def solution_position(state):
    for i in range(9):
        solutionPosition[i] = p8.get_tile(state, i)

    for i in range(9):
        Square_to_Position_Solution[p8.get_tile(
            state, i)] = p8.xy_location(i)


solution_position(solution)


def num_wrong_tiles(state) -> int:
    """Given a puzzle, returns the number of tiles that are in the wrong
    location. Does not count the blank space.
    """
    res = 0
    for i in range(9):
        # Maps current Position to its tiles
        currentPosition[i] = p8.get_tile(state, i)
        # If the tiles are in wrong places or it is blank space
        if currentPosition[i] != 0:
            if currentPosition[i] != solutionPosition[i]:
                res += 1
    return res


def manhattan_distance(state) -> int:
    """Given a puzzle, returns the Manhattan distance to the solution state.
    Does not count the distance from blank space to its correct location as
    part of the distance.
    """
    res = 0
    # Map Current Square to its Postion
    for i in range(9):
        Square_to_Position_Current[p8.get_tile(
            state, i)] = p8.xy_location(i)

    for i in range(1, 9):
        positionCur = Square_to_Position_Current[i]
        positionSol = Square_to_Position_Solution[i]
        # Manhattan Distance
        res += abs(positionCur[0]-positionSol[0]) + \
            abs(positionCur[1]-positionSol[1])
    return res


def astar_search(state: int, heuristic) -> List[int]:
    """Finds path to solution via A* search, using the provided heuristic.
    Returns a list of squares that the blank moves to in order to get to
    solution.
    """
    heap = []
    # Add the current states
    heapq.heappush(heap, (heuristic(state), state, []))

    while (heap):
        value, currentState, path = heapq.heappop(heap)
        # If we find the solution
        if currentState == solution:
            return path

        current_blank_square = p8.blank_square(currentState)
        neighbors = p8.neighbors(current_blank_square)
        # All possible turns
        for neighbor in neighbors:
            newState = p8.move_blank(currentState, neighbor)
            newPath = path.copy()
            newPath.append(neighbor)
            # Add the real cost to the node + the heuristic from the node to finish
            heapq.heappush(
                heap, (len(newPath) + heuristic(newState), newState, newPath))

    return []


# print(astar_search(253206748, manhattan_distance))

def timeTest(state):
    length = len(astar_search(state, manhattan_distance))
    # Start time
    startTime = time.time()
    astar_search(state, num_wrong_tiles)
    # Finish Time
    finishTime = time.time()
    print(
        f"For solution of state {state} with solution's length of {length}, Time taken to run with num_wrong_tiles is", finishTime-startTime)

    # Start time
    startTime = time.time()
    astar_search(state, manhattan_distance)
    # Finish Time
    finishTime = time.time()
    print(
        f"For solution of state {state} with solution's length of {length}, Time taken to run with manhattan_distance is", finishTime-startTime)

    # Start time
    startTime = time.time()
    iterative_deepening_search(state)
    # Finish Time
    finishTime = time.time()
    print(
        f"For solution of state {state} with solution's length of {length}, Time taken to run with iterative deepening search is", finishTime-startTime)


# timeTest(247860748)
# timeTest(253206748)
# timeTest(253780508)
# timeTest(152293420)
# timeTest(300501380)
