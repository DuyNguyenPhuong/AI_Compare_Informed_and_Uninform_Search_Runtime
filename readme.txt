Sunday April 9

To test time, uncomment the last 5 lines of the code

This my experience when testing the the 2 heuristic functions: num_wrong_tiles and manhattan_distance,
and the iterative deepening search function

The result is:

For solution of state 247860748 with solution's length of 2, Time taken to run with num_wrong_tiles is 0.00021123886108398438
For solution of state 247860748 with solution's length of 2, Time taken to run with manhattan_distance is 0.00014495849609375
For solution of state 247860748 with solution's length of 2, Time taken to run with iterative deepening search is 0.00018405914306640625
For solution of state 253206748 with solution's length of 4, Time taken to run with num_wrong_tiles is 0.0003666877746582031
For solution of state 253206748 with solution's length of 4, Time taken to run with manhattan_distance is 0.00040602684020996094
For solution of state 253206748 with solution's length of 4, Time taken to run with iterative deepening search is 0.002706766128540039
For solution of state 253780508 with solution's length of 8, Time taken to run with num_wrong_tiles is 0.0014278888702392578
For solution of state 253780508 with solution's length of 8, Time taken to run with manhattan_distance is 0.0007059574127197266
For solution of state 253780508 with solution's length of 8, Time taken to run with iterative deepening search is 0.09990310668945312
For solution of state 152293420 with solution's length of 10, Time taken to run with num_wrong_tiles is 0.030595779418945312
For solution of state 152293420 with solution's length of 10, Time taken to run with manhattan_distance is 0.003793001174926758
For solution of state 152293420 with solution's length of 10, Time taken to run with iterative deepening search is 1.8989498615264893
For solution of state 300501380 with solution's length of 12, Time taken to run with num_wrong_tiles is 0.14850306510925293
For solution of state 300501380 with solution's length of 12, Time taken to run with manhattan_distance is 0.03720998764038086
For solution of state 300501380 with solution's length of 12, Time taken to run with iterative deepening search is 7.888382911682129



Look at the results, we see that there isn't much time difference between 2 heuristic functions.
However, we note that the num_wrong_tiles function is a little bit slower than manhattan_distance

Moreover, the iterative deepening search is much slower than both astar search

Therefore, we can conclude that the iterative deepening is slower than astar search. While num_wrong_tiles are just a little
bit slower than manhattan_distance search
