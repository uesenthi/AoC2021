import os
from collections import defaultdict

from libraries.helpers import get_input


def filter_for_horizontal_vertical(content):
    new_set = []
    for row in content:
        start, end = map(lambda x: x.split(','), row.split(' -> '))
        if start[0] == end[0] or start[1] == end[1]:
            new_set.append((start, end))
    return new_set

def get_path_between_pair(coordinate_pair):
    start, end = coordinate_pair
    path = []
    # Same row
    if start[0] == end[0]:
        for x in range(
            min(int(start[1]), int(end[1])), 
            max(int(end[1]), int(start[1])) + 1
        ):
            path.append((start[0], str(x)))
    
    # Same column
    elif start[1] == end[1]:
        for x in range(
            min(int(start[0]), int(end[0])), 
            max(int(end[0]), int(start[0])) + 1
        ):
            path.append((str(x), start[1]))

    return path

def get_solution(content):
    coordinate_map = defaultdict(int)
    filtered_content = filter_for_horizontal_vertical(content)
    for pair in filtered_content:
        path = get_path_between_pair(pair)
        for coordinate in path:
            coordinate_map[str(coordinate)] += 1
    
    return len(
        [
            key
            for key, val in coordinate_map.items()
            if val >= 2
        ]
    )


if __name__ == "__main__":
    if get_solution(get_input(path_to_file=os.getcwd() + "/input_test.txt")) == 5:
        print("Test case passed")
        print(get_solution(get_input(path_to_file=os.getcwd() + "/input.txt")))
    else:
        raise Exception("Test case failed")
