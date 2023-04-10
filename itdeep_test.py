import itdeep
import pytest
import time
import resource

states_and_shortest_lengths = [
    (247860748, 2),
    (253206748, 4),
    (253780508, 8),
    (152293420, 10),
    (300501380, 12)]

ids = [str(state) for (state, _) in states_and_shortest_lengths]
memory_used_per_test = []


@pytest.mark.parametrize("test_input,expected", states_and_shortest_lengths,
                         ids=ids)
def test_itdeep(test_input, expected):

    time_before = time.time()
    soln_path = itdeep.iterative_deepening_search(test_input)
    time_after = time.time()
    memory_used = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    memory_used_per_test.append(memory_used)

    print("Time to run =", time_after-time_before)
    print("Memory used, likely in kb = ", memory_used)

    assert max(memory_used_per_test) < 2*min(memory_used_per_test), (
        "Maximum memory used is more than twice minimum memory used, should be"
        " roughly constant")
    assert soln_path is not None
    assert len(soln_path) == expected
