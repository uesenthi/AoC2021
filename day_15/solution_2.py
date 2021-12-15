import math
import os

from libraries.helpers import get_input
from collections import defaultdict

def get_coordinate_map(content):
    coordinate = {
        x: []
        for x in range(len(content)*5)
    }
    
    for idx, line in enumerate(content):
        for i in range(5):
            row = list(map(lambda x: increment(int(x), i), list(line)))
            coordinate[idx].extend(row)
    
    for y in range(len(content)):
        for i in range(1,5):
            row = list(map(lambda x: increment(int(x), i), coordinate[y]))
            coordinate[y + len(content)*i].extend(row)

    return coordinate

def increment(val, step):
    sum = val + step
    if sum >= 10:
        sum = sum - 10 + 1
    return sum

def get_density_at_pos(content, y, x):
    try:
        val = content[y][x]
        return val
    
    except (KeyError,IndexError):
        # print("index errpr", y,x)
        return None

def build_shortest_path_map(coordinate_map, shortest_path):
    new_shortest_paths = shortest_path.copy()
    for y in range(len(coordinate_map)):
        for x in range(len(coordinate_map[0])):
            current_position = str([y,x])
            # All possible neighbors
            possible_neighors = [
                [y-1,x],
                [y,x-1],
                [y+1,x],
                [y,x+1],
            ]
            actual_neighbors = list(filter(lambda neighbor: isinstance(get_density_at_pos(coordinate_map, neighbor[0], neighbor[1]), int), possible_neighors))

            for neighbor in actual_neighbors:
                density_to_neighber = get_density_at_pos(coordinate_map, neighbor[0], neighbor[1])
                new_shortest_paths[str(neighbor)] = min(new_shortest_paths.get(str(neighbor), math.inf), new_shortest_paths[current_position] + density_to_neighber)
    return new_shortest_paths

def get_solution(content):
    # STarting position is never "entered", so don't count it
    coordinate_map = get_coordinate_map(content)
    start_position = [0,0]
    end_position = [len(coordinate_map[0])-1, len(coordinate_map) - 1]

    shortest_path = build_shortest_path_map(
        coordinate_map,
        {str(start_position): 0}
    )

    initial_path_to_end = shortest_path[str(end_position)]
    while True:
        shortest_path = build_shortest_path_map(
            coordinate_map,
            shortest_path
        )
        new_path_to_end = shortest_path[str(end_position)]
        if new_path_to_end != initial_path_to_end:
            initial_path_to_end = new_path_to_end
            continue
        else:
            break
        


    return initial_path_to_end    


if __name__ == "__main__":
    test_solution = get_solution(get_input(path_to_file=os.getcwd() + "/input_test.txt"))
    if test_solution == 315:
        print("TEST PASSED")
        print(get_solution(get_input(path_to_file=os.getcwd() + "/input.txt")))
        
    else:
        print(test_solution)
        print("Test failed")
