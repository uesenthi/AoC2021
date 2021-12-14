import os

from libraries.helpers import get_input
from collections import defaultdict


def get_solution(content):
    steps = 40
    polymer_template = content[0]
    polymer_map = {}

    initial_state_polymers = defaultdict(int)

    # Get Instructions
    for line in content[2:]:
        input_polymer, output_reaction = line.split(' -> ')
        polymer_map[input_polymer] = output_reaction

    def get_polymer_ouput(chain):
        reaction = polymer_map[chain]
        return chain[0]+reaction, reaction+chain[1]
    
    # Create initial state for step 1
    for x in range(len(polymer_template)-1):
        chain = polymer_template[x:x+2]
        part_1, part_2 = get_polymer_ouput(chain)
        initial_state_polymers[part_1] += 1
        initial_state_polymers[part_2] += 1

    for step in range(steps-1):               
        new_polymer_map = defaultdict(int)
        for chain, val in initial_state_polymers.items():
            part_1, part_2 = get_polymer_ouput(chain)
            new_polymer_map[part_1] += val
            new_polymer_map[part_2] += val

        initial_state_polymers = new_polymer_map.copy()


    counter = defaultdict(int)
    # Could indiviudal polymers
    for chain, val in initial_state_polymers.items():
        part_1, part_2 = list(chain)
        counter[part_1] += val
    counter[polymer_template[-1]] += 1

    return counter[max(counter, key=counter.get)] - counter[min(counter, key=counter.get)]

if __name__ == "__main__":
    test_solution = get_solution(get_input(path_to_file=os.getcwd() + "/input_test.txt"))
    if test_solution == 2188189693529:
        print("TEST PASSED")
        print(get_solution(get_input(path_to_file=os.getcwd() + "/input.txt")))
        
    else:
        print(test_solution)
        print("Test failed")
