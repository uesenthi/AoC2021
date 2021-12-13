import os

from libraries.helpers import get_input

def procreate(fish):
    fishies = []
    new_count = fish - 1

    if new_count < 0:
        new_count = 6
        new_fish = 8
        fishies.append(new_fish)
    fishies.append(new_count)

    return fishies


def get_solution(content):
    lantern_fishies = list(map(lambda x: int(x), content[0].split(',')))
    final_fish_set = []
    for day in range(80):
        final_fish_set.clear()
        for fish in lantern_fishies:
            final_fish_set += procreate(fish)
        lantern_fishies = final_fish_set.copy()
    return len(lantern_fishies)

if __name__ == "__main__":
    test_solution = get_solution(get_input(path_to_file=os.getcwd() + "/input_test.txt"))
    if test_solution == 5934:
        print("TEST PASSED")
        print(get_solution(get_input(path_to_file=os.getcwd() + "/input.txt")))
    else:
        print(test_solution)
        print("Test failed")
