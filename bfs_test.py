import bfs
import pytest
import time

states_and_shortest_lengths = [
    (247860748, 2),
    (253206748, 4),
    (253780508, 8),
    (152293420, 10)]


@pytest.mark.parametrize("test_input,expected", states_and_shortest_lengths)
def test_bfs(test_input, expected):
    time_before = time.time()
    soln_path = bfs.breadth_first_search(test_input)
    time_after = time.time()
    print("Time to run =", time_after-time_before)
    assert soln_path is not None
    assert len(soln_path) == expected
