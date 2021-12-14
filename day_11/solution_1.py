import os
import functools
from typing import Coroutine

from libraries.helpers import get_input
    

def cascade_energy_burst(state_table, epicentre, burst_octopus):
    new_bursts = []
    adjacent_steps = [
        (1,0),
        (-1, 0),
        (-1, 1),
        (1, -1),
        (0, 1),
        (0, -1),
        (-1, -1),
        (1, 1),
    ]

    x, y = list(map(lambda x: int(x), epicentre))

    for step in adjacent_steps:
        key = f'{x+step[0]}{y+step[-1]}'

        if key in burst_octopus:
            continue
        octo_power_level = get_octo_at_position(state_table, key)
        if not isinstance(octo_power_level, int):
            continue
        elif octo_power_level < 9:
            state_table[key] = state_table[key] + 1 if state_table[key] else 1
        else:
            new_bursts.append(key)
    return state_table, new_bursts

    
def get_octo_at_position(state_table, key):
    try:
        power_level = state_table[key]
        if power_level == None:
            return 1
        elif isinstance(power_level, int):
            return power_level

    except KeyError:
        return None

def get_solution(content):
    steps = 100
    start_state = content.copy()
    
    octo_map = {
        f'{x}{y}': int(content[x][y])
        for y in range(len(start_state[0]))
        for x in range(len(start_state))
    }
    num_bursts = 0

    for step in range(steps):
        burst_octopus = []
        octopus_ready = list(octo_map.keys())

        while len(octopus_ready) > 0:
            coordinate = octopus_ready.pop()
            if coordinate in burst_octopus:
                continue

            if octo_map[coordinate] == None:
                octo_map[coordinate] = 1
            elif octo_map[coordinate] and octo_map[coordinate] < 9:
                octo_map[coordinate] += 1
            else:
                burst_octopus.append(coordinate)
                num_bursts += 1
                octo_map[coordinate] = None
                octo_map, new_bursts = cascade_energy_burst(octo_map, coordinate, burst_octopus)
                for burst_octo in new_bursts:
                    octopus_ready.append(burst_octo)
    
    return num_bursts

if __name__ == "__main__":
    test_solution = get_solution(get_input(path_to_file=os.getcwd() + "/input_test.txt"))
    if test_solution == 1656:
        print("TEST PASSED")
        print(get_solution(get_input(path_to_file=os.getcwd() + "/input.txt")))
    else:
        print(test_solution)
        print("Test failed")
