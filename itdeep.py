import puzzle8 as p8
from typing import List
import time

solution = p8.solution()


def iterative_deepening_search(state: int) -> List[int]:
    """Finds path to solution via iterative deepening. Returns a list of
    squares that the blank moves to in order to get to solution.
    """
    i = 0
    while (True):
        result = depth_limited_search(state, i, [])
        if result != None:
            return result
        i += 1


def depth_limited_search(currentState, depth, path):
    if currentState == solution:
        return path
    # If we pass the depth, return
    if depth <= 0:
        return None
    blank_space_square = p8.blank_square(currentState)
    neighbors = p8.neighbors(blank_space_square)
    # Calculate all the neighbors of blank square
    for neighbor in neighbors:
        temp = path.copy()
        temp.append(neighbor)
        newState = p8.move_blank(currentState, neighbor)
        result = depth_limited_search(newState, depth-1, temp.copy())
        if result != None:
            return result


def timeTest(state):
    depth = len(iterative_deepening_search(state))
    # Start time
    startTime = time.time()
    depth_limited_search(state, depth, [])
    # Finish Time
    finishTime = time.time()
    print("For solution has the length of " + str(depth) +
          ", Time taken to run the last iteration", finishTime-startTime)

    # Start time
    startTime = time.time()
    iterative_deepening_search(state)
    # Finish Time
    finishTime = time.time()
    print("For solution has the length of " + str(depth) +
          ", Time taken to run full", finishTime-startTime)


# Test Time, Uncomment to test
# timeTest(247860748)
# timeTest(253206748)
# timeTest(253780508)
# timeTest(152293420)
# timeTest(300501380)
