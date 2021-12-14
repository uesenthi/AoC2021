import os
import functools

from libraries.helpers import get_input
    

def get_solution(content):
    proper_symbol_map = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
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
    corrupted_lines = []

    # Use old code to get corrupted lines
    for idx, line in enumerate(content):
        open_brackets = []
        for char in line:
            if char in ('(', '[', '{', '<'):
                open_brackets.append(char)
            else:
                current_open = open_brackets.pop()
                if symbol_pair[current_open] != char:
                    illegal_characters.append(error_symbol_map[char])
                    corrupted_lines.append(line)
                    break
    
    
    # Get finishing syntax string
    scores = []
    for line in content:
        if line in corrupted_lines:
            continue
        
        open_brackets = []
        for char in line:
            if char in ('(', '[', '{', '<'):
                open_brackets.append(char)
            else:
                current_open = open_brackets.pop()
        
        ending_string = ''
        score = 0
        for x in range(len(open_brackets)):
            current_open = open_brackets.pop()
            ending_string += symbol_pair[current_open]
            score = (5*score) + proper_symbol_map[symbol_pair[current_open]]
        
        scores.append(score)

    sorted_scores = sorted(scores)
    
    if len(sorted_scores) % 2 == 1:
        return sorted_scores[len(sorted_scores) // 2]
    else:
        return sorted_scores[len(sorted_scores)/2]

if __name__ == "__main__":
    test_solution = get_solution(get_input(path_to_file=os.getcwd() + "/input_test.txt"))
    if test_solution == 288957:
        print("TEST PASSED")
        print(get_solution(get_input(path_to_file=os.getcwd() + "/input.txt")))
    else:
        print(test_solution)
        print("Test failed")
