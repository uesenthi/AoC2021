import os
from libraries.helpers import get_input


def get_solution(content):
    crab_positions = list(map(lambda x: int(x), content[0].split(',')))
    grid_length = sorted(crab_positions)

    min_range = grid_length[0]
    max_range = grid_length[-1]

    converge_position = {
        x: 0
        for x in range(min_range, max_range+1)
    }

    for key in converge_position.keys():
        for crab in crab_positions:
            converge_position[key] += abs(crab - key)
    
    return converge_position[min(converge_position, key=converge_position.get)]
    

if __name__ == "__main__":
    test_solution = get_solution(get_input(path_to_file=os.getcwd() + "/input_test.txt"))
    if test_solution == 37:
        print("TEST PASSED")
        print(get_solution(get_input(path_to_file=os.getcwd() + "/input.txt")))
    else:
        print(test_solution)
        print("Test failed")
