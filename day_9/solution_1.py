import os
import functools

from libraries.helpers import get_input


def get_min_in_area(content, x, y):
    valid_spots = []
    steps = [
        (0, 0),
        (-1, 0),
        (1, 0),
        (0, 1),
        (0, -1),
    ]
    for step in steps:
        pos = get_pos_at_index(content, x+step[0], y+step[1])
        if pos is not None:
            valid_spots.append(pos)
    
    filtered_set = list(filter(lambda x: x == min(valid_spots), valid_spots))
    return min(valid_spots) if len(filtered_set) == 1 else None

def get_pos_at_index(content, x, y):
    # If outside range, return None
    if x < 0 or y < 0:
        return None
    try:
        pos = int(content[x][y])
        return pos
    except IndexError:
        return None

def get_solution(content):
    x_grid = len(content)
    y_grid = len(content[0])
    shortest_heights = []

    for x in range(x_grid):
        for y in range(y_grid):
            pos = int(content[x][y])
            if pos == get_min_in_area(content, x, y):
                shortest_heights.append(pos)

    sum = 0
    for x in shortest_heights:
        sum += x + 1
    return sum

if __name__ == "__main__":
    test_solution = get_solution(get_input(path_to_file=os.getcwd() + "/input_test.txt"))
    if test_solution == 15:
        print("TEST PASSED")
        print(get_solution(get_input(path_to_file=os.getcwd() + "/input.txt")))
    else:
        print(test_solution)
        print("Test failed")
