import os
import functools
from collections import defaultdict

from libraries.helpers import get_input


PATHS_TO_END = []


def depth_first_search(edge_map, start_node, current_path, small_cave_visited_twice=False):
    current_node = start_node
    path = ''
    if current_node == 'end':
        PATHS_TO_END.append(current_path)
        return 'end'
    next_hops = edge_map[current_node]
    for hop in next_hops:
        can_visit_small_cave_twice = small_cave_visited_twice
        if hop in ('start', 'end') and hop in current_path:
            continue
        elif hop.lower() == hop:
            visit_frequency = current_path.count(hop)
            if visit_frequency >= 1 and can_visit_small_cave_twice:
                continue
            elif visit_frequency >= 1 and can_visit_small_cave_twice is False:
                # You can visit this small cave one more time
                can_visit_small_cave_twice = True

        next_path = current_path.copy()
        next_path.append(hop)
        path += depth_first_search(edge_map, hop, next_path, can_visit_small_cave_twice)
    return ''

def get_solution(content):
    edge_map = defaultdict(set)
    path_map = []
    # Initialize edge map
    for line in content:
        point_a, point_b = line.split('-')
        edge_map[point_a].add(point_b)
        edge_map[point_b].add(point_a)
    
    depth_first_search(edge_map, 'start', ['start'])
    # for path in PATHS_TO_END:
    #     print(path)
    return len(PATHS_TO_END)


if __name__ == "__main__":
    test_solution = get_solution(get_input(path_to_file=os.getcwd() + "/input_test.txt"))
    if test_solution == 36:
        PATHS_TO_END.clear()
        print("TEST PASSED")
        print(get_solution(get_input(path_to_file=os.getcwd() + "/input.txt")))
    else:
        print(test_solution)
        print("Test failed")






# start,b,A,c,A,b,A,end
# start,b,A,c,A,b,end


