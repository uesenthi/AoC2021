import os
import functools

from libraries.helpers import get_input
    

def get_solution(content):
    error_symbol_map = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    symbol_pair = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }
    illegal_characters = []

    for idx, line in enumerate(content):
        open_brackets = []
        for char in line:
            if char in ('(', '[', '{', '<'):
                open_brackets.append(char)
            else:
                current_open = open_brackets.pop()
                if symbol_pair[current_open] != char:
                    illegal_characters.append(error_symbol_map[char])
                    break

    return functools.reduce(lambda x, y: x + y, illegal_characters)


if __name__ == "__main__":
    test_solution = get_solution(get_input(path_to_file=os.getcwd() + "/input_test.txt"))
    if test_solution == 26397:
        print("TEST PASSED")
        print(get_solution(get_input(path_to_file=os.getcwd() + "/input.txt")))
    else:
        print(test_solution)
        print("Test failed")
