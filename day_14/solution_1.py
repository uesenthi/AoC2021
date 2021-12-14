import os

from libraries.helpers import get_input




def get_solution(content):
    steps = 10
    polymer_template = content[0]
    polymer_map = {}

    for line in content[2:]:
        input_polymer, output_reaction = line.split(' -> ')
        polymer_map[input_polymer] = output_reaction
    
    for step in range(steps):
        new_template = [None]
        for x in range(len(polymer_template)-1):
            chain = polymer_template[x:x+2]
            reaction = polymer_map[chain]
            new_template.pop()
            new_template.extend([chain[0], reaction, chain[1]])

        polymer_template = ''.join(new_template)
    


    counter = {
        polymer: polymer_template.count(polymer)
        for polymer in set(list(polymer_template))
    }

    return counter[max(counter, key=counter.get)] - counter[min(counter, key=counter.get)]

if __name__ == "__main__":
    test_solution = get_solution(get_input(path_to_file=os.getcwd() + "/input_test.txt"))
    if test_solution == 1588:
        print("TEST PASSED")
        print(get_solution(get_input(path_to_file=os.getcwd() + "/input.txt")))
    else:
        print(test_solution)
        print("Test failed")
