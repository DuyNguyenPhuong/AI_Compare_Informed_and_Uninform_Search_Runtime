import puzzle8 as p8
import astar
import pytest
import random
import itertools
import time

off_two_puzzle = p8.state([3, 4, 5, 2, 0, 6, 1, 8, 7])

test_puzzle1 = p8.state([8, 7, 6, 5, 4, 3, 2, 1, 0])
test_puzzle2 = p8.state([1, 2, 3, 4, 5, 6, 7, 8, 0])


def test1_num_wrong_tiles_m():
    random.seed(12345)
    assert astar.num_wrong_tiles(p8.solution()) == 0
    assert astar.num_wrong_tiles(p8.random_state(1)) == 1
    assert astar.num_wrong_tiles(off_two_puzzle) == 8


def test2_num_wrong_tiles_e():
    assert astar.num_wrong_tiles(test_puzzle2) == 4
    assert astar.num_wrong_tiles(test_puzzle1) == 8


def test3_manhattan_distance_m():
    random.seed(12345)
    assert astar.manhattan_distance(p8.solution()) == 0
    assert astar.manhattan_distance(p8.random_state(1)) == 1
    assert astar.manhattan_distance(off_two_puzzle) == 16


def test4_manhattan_distance_e():
    assert astar.manhattan_distance(test_puzzle1) == 18
    assert astar.manhattan_distance(test_puzzle2) == 8


states_and_shortest_lengths = [
    (247860748, 2),
    (253206748, 4),
    (253780508, 8),
    (152293420, 10),
    (300501380, 12),
    (108306836, 16),
]

heuristics = [astar.num_wrong_tiles, astar.manhattan_distance]

puzzles_and_heuristics = list(itertools.product(states_and_shortest_lengths,
                                                heuristics))

ids = [str(state) + " " + heuristic.__name__ \
       for ((state, steps), heuristic) in puzzles_and_heuristics]


@pytest.mark.parametrize("test_input_pair,heuristic", puzzles_and_heuristics, ids=ids)
def test_astar(test_input_pair, heuristic):
    (test_input, expected) = test_input_pair

    time_before = time.time()
    soln_path = astar.astar_search(test_input, heuristic)
    time_after = time.time()
    print("Time to run =", time_after-time_before)
    assert soln_path is not None
    assert len(soln_path) == expected
