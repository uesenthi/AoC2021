import os
from collections import defaultdict
import functools

from libraries.helpers import get_input


def get_solution(content):
    days = 256
    initial_fish = list(map(lambda x: int(x), content[0].split(',')))
    fish_count_at_life_cycle = defaultdict(int)
    # populate initial set
    for fish in initial_fish:
        fish_count_at_life_cycle[fish] += 1

    for day in range(days):
        new_fish_count_lifecycle = {}
        for key, val in fish_count_at_life_cycle.items():
            if key == 0:
                new_fish_count_lifecycle[6] = new_fish_count_lifecycle.get(6, 0) + val
                new_fish_count_lifecycle[8] = val
            else:
                new_fish_count_lifecycle[key - 1] = new_fish_count_lifecycle.get(key-1, 0) + val
        fish_count_at_life_cycle = new_fish_count_lifecycle.copy() 
    
    return functools.reduce(lambda a, b: a+b, fish_count_at_life_cycle.values())
    

if __name__ == "__main__":
    test_solution = get_solution(get_input(path_to_file=os.getcwd() + "/input_test.txt"))
    if test_solution == 26984457539:
        print("TEST PASSED")
        print(get_solution(get_input(path_to_file=os.getcwd() + "/input.txt")))
    else:
        print(test_solution)
        print("Test failed")
