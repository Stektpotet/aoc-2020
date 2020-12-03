import fileinput
from functools import reduce
from operator import mul

slope_params = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
lines = list(enumerate([line[:-1] for line in fileinput.input()]))

def count_trees(right_step: int, down_step: int):
    return sum((1 - (y % down_step)) * (line[((y // down_step) * right_step) % len(line)] == '#') for y, line in lines)

print(count_trees(3, 1))
print(reduce(mul, (count_trees(r, d) for r, d in slope_params), 1))
