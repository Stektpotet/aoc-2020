import numpy as np
import itertools

def summing_generator(input: np.ndarray, num_factors: int, res: int = 2020):
    return (np.prod(factors) for factors in itertools.combinations(input, num_factors) if sum(factors) == res)

if __name__ == '__main__':
    input = np.fromfile("input", dtype=np.int32, sep='\n')
    for r in summing_generator(input, 2):
        print(r)
    for r in summing_generator(input, 3):
        print(r)
