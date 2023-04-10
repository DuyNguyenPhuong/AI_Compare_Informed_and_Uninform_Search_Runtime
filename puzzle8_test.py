from puzzle8 import (
    state, get_tile, blank_square, move_blank, neighbors, solution, xy_location,
    random_state)
import random


def test_state():
    assert state([1, 2, 3, 8, 0, 4, 7, 6, 5]) == 247893796


def test_get_tile():
    assert get_tile(247893796, 0) == 1
    assert get_tile(247893796, 3) == 8


def test_blank_square():
    assert blank_square(247893796) == 4


def test_move_blank():
    state1 = state([1, 2, 3, 8, 0, 4, 7, 6, 5])
    state2 = state([1, 0, 3, 8, 2, 4, 7, 6, 5])
    assert move_blank(state1, 1) == state2


def test_neighbors():
    assert set(neighbors(4)) == set([1, 3, 7, 5])


def test_solution():
    assert state([1, 2, 3, 8, 0, 4, 7, 6, 5]) == solution()


def test_xy_location():
    assert xy_location(5) == (2, 1)


def test_random_state():
    assert random_state(0) == solution()
    random.seed(12345)
    assert random_state(1) == state([1, 2, 3, 8, 6, 4, 7, 0, 5])
    random.seed(12345)
    assert random_state(100) == 108261756
