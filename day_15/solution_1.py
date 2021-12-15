import math
import os

from libraries.helpers import get_input
from collections import defaultdict

def get_coordinate_map(content):
    coordinate = {
        x: []
        for x in range(len(content))
    }

    for idx, line in enumerate(content):
        coordinate[idx] =  list(map(lambda x: int(x), list(line)))

    # for y in coordinate:
    #     print(','.join(list(map(lambda x: str(x), coordinate[y]))))
    return coordinate

def get_density_at_pos(content, y, x):
    if x < 0 or y < 0:
        # print("less than 0 errpr", y,x)
        return None
    try:
        val = content[y][x]
        return val
    
    except (KeyError,IndexError):
        # print("index errpr", y,x)
        return None


def get_solution(content):
    # STarting position is never "entered", so don't count it
    coordinate_map = get_coordinate_map(content)
    start_position = [0,0]
    end_position = [len(coordinate_map[0])-1, len(coordinate_map) - 1]

    # Weight of 0 from the start
    shortest_path = {
        str(start_position): 0
    }
    shortest_journey = {
        str(start_position): [start_position]
    }

    shortest_journey = defaultdict(list)

    # Do this x times, so that all the risk values "stabilize"
    for a in range(5):
        for y in range(len(coordinate_map)):
            for x in range(len(coordinate_map[0])):
                # All possible neighbors
                possible_neighors = [
                    [y-1, x],
                    [y, x+1],
                    [y+1, x],
                    [y, x-1],
                ]
                actual_neighbors = list(filter(lambda neighbor: isinstance(get_density_at_pos(coordinate_map, neighbor[0], neighbor[1]), int), possible_neighors))
                for neighbor in actual_neighbors:
                    density_to_neighber = get_density_at_pos(coordinate_map, neighbor[0], neighbor[1])
                    current_path_neighbor = shortest_path.get(str(neighbor),math.inf)
                    new_path = shortest_path[str([y,x])] + density_to_neighber

                    if new_path < current_path_neighbor:
                        shortest_journey[str(neighbor)] = shortest_journey[str([y,x])] + [neighbor]

                    shortest_path.update({
                        str(neighbor): min(shortest_path.get(str(neighbor),math.inf), shortest_path[str([y,x])] + density_to_neighber)
                    })

    path = shortest_path[str(end_position)]
    return path    


if __name__ == "__main__":
    test_solution = get_solution(get_input(path_to_file=os.getcwd() + "/input_test.txt"))
    if test_solution == 40:
        print("TEST PASSED")
        print(get_solution(get_input(path_to_file=os.getcwd() + "/input.txt")))
        
    else:
        print(test_solution)
        print("Test failed")
