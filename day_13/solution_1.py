import os

from libraries.helpers import get_input


def get_coordinate_map(content):
    x_points = []
    y_points = []
    folds = []
    coordinate_map = {}
    for line in content:
        if not line:
            continue
        if 'fold' in line:
            folds.append(line.split(' along ')[-1])
            continue
        x, y = line.split(',')
        x_points.append(int(x))
        y_points.append(int(y))

    coordinate_map = {
        y: ['.'] * (max(x_points) + 1)
        for y in range(max(y_points) + 1)
    }

    for coordinate in zip(x_points, y_points):
        coordinate_map[coordinate[1]][coordinate[0]] = 'x'

    return coordinate_map, folds

def get_visible_dots(coordinate_map):
    count = 0
    for y in range(len(coordinate_map)):
        for x in range(len(coordinate_map[0])):
            if coordinate_map[y][x] == 'x':
                count += 1
    return count

def fold_map(coordinate_map, fold_axis, fold_position):
    current_state = coordinate_map.copy()
    part_1 = {
        y: current_state[y]
        for y in range(len(current_state))
        if y < fold_position
    } if fold_axis == 'y' else \
        {
            y: current_state[y][:fold_position]
            for y in range(len(current_state))
        }
    part_2 = {
        y - fold_position - 1: current_state[y]
        for y in range(len(current_state))
        if y > fold_position
    } if fold_axis == 'y' else \
        {
            y: current_state[y][fold_position+1:]
            for y in range(len(current_state))
        }
    
    new_state = merge_parts(part_1, part_2, fold_axis)
    return new_state

def merge_parts(part_1, part_2, fold_axis):
    folded_coordinate = part_1.copy()
    if fold_axis == 'y':
        for y in range(len(part_2)):
            part_1_key = len(part_1) - 1 - y
            for idx, val in enumerate(zip(part_2[y], part_1[part_1_key])):
                if val[0] == 'x' or val[1] == 'x':
                    folded_coordinate[part_1_key][idx] = 'x'
    else:
        for y in range(len((part_1))):
            for x in range(len(part_2[y])):
                if part_2[y][x] == 'x' or part_1[y][-(x+1)] == 'x':
                    folded_coordinate[y][-(x+1)] = 'x'
    return folded_coordinate


def visualize_current_state(coordinate_map):
    for row in coordinate_map.values():
        print(row)

def get_solution(content):
    coordinate_map, folds = get_coordinate_map(content)

    for fold in folds:
        axis, position = fold.split('=')
        position = int(position)

        coordinate_map = fold_map(coordinate_map, axis, position)
        break

    return get_visible_dots(coordinate_map)


if __name__ == "__main__":
    test_solution = get_solution(get_input(path_to_file=os.getcwd() + "/input_test.txt"))
    if test_solution == 17:
        print("TEST PASSED")
        print(get_solution(get_input(path_to_file=os.getcwd() + "/input.txt")))
    else:
        print(test_solution)
        print("Test failed")
