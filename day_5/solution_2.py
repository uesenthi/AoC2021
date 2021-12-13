import os
from collections import defaultdict

from libraries.helpers import get_input


def filter_for_horizontal_vertical_diagonal(content):
    new_set = []
    for row in content:
        pos_1, pos_2 = map(lambda x: x.split(','), row.split(' -> '))

        start = (int(pos_1[0]), int(pos_1[1]))
        end = (int(pos_2[0]), int(pos_2[1]))

        if start[0] == end[0] or start[1] == end[1] or abs(start[0] - end[0]) == abs(start[1] - end[1]):
            new_set.append((start, end))

    return new_set

def get_path_between_pair(coordinate_pair):
    
    start, end = coordinate_pair
    path = []
    # Same row
    if start[0] == end[0]:
        for x in range(
            min(start[1], end[1]), 
            max(end[1], start[1]) + 1
        ):
            path.append((start[0], x))
    
    # Same column
    elif start[1] == end[1]:
        for x in range(
            min(start[0], end[0]), 
            max(end[0], start[0]) + 1
        ):
            path.append((x, start[1]))
    
    # Same diagonal
    elif abs(start[0] - end[0]) == abs(start[1] - end[1]):
        x_dir = 1 if end[0] - start[0] > 0 else -1
        y_dir = 1 if end[1] - start[1] > 0 else -1

        for x in range(abs(start[0] - end[0])+1):
            path.append((
                start[0] + x*x_dir,
                start[1] + x*y_dir
            ))

    return path

def get_solution(content):
    coordinate_map = defaultdict(int)
    filtered_content = filter_for_horizontal_vertical_diagonal(content)
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
    test_solution = get_solution(get_input(path_to_file=os.getcwd() + "/input_test.txt"))
    if test_solution == 12:
        print("Test case passed")
        print(get_solution(get_input(path_to_file=os.getcwd() + "/input.txt")))
    else:
        print(test_solution)
        raise Exception("Test case failed")
