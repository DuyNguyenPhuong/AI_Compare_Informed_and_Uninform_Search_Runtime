from typing import List
import puzzle8 as p8
from collections import deque
# help(puzzle8)


def breadth_first_search(state: int) -> List[int]:
    """Finds path to solution via breadth-first search. Returns a list of
    squares that the blank moves to in order to get to solution.
    """

    solution = p8._goal

    blank_space_goal = p8.blank_square(solution)

    blank_space_location = p8.blank_square(state)

    if (solution == state):
        return []

    queue = []
    queue.append((blank_space_location, state, []))

    while queue:
        space, currentState, path = queue.pop(0)
        neigbors = p8.neighbors(space)
        for neigbor in neigbors:
            newState = p8.move_blank(currentState, neigbor)
            temp = path.copy()
            temp.append(neigbor)
            if newState == solution:
                return temp.copy()
            queue.append((neigbor, newState, temp.copy()))
    return None
