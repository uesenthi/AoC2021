import os
import functools
from libraries.helpers import get_input


def parse_broken_dial(signals, outputs):
    signal_pattern_lookup = {}

    for signal in signals:
        if len(signal) == 2:
            signal_pattern_lookup[str(sorted(signal))] = 1
        elif len(signal) == 3:
            signal_pattern_lookup[str(sorted(signal))] = 7
        elif len(signal) == 4:
            signal_pattern_lookup[str(sorted(signal))] = 4
        elif len(signal) == 7:
            signal_pattern_lookup[str(sorted(signal))] = 8
    
    easy_bit_values = 0
    x = list(signal_pattern_lookup.keys())

    for output in outputs:
        if str(sorted(output)) in x:
            easy_bit_values += 1
    
    return easy_bit_values


def get_solution(content):
    freq = 0
    for line in content:
        patterns, output = line.split(' | ')
        broken_signal_patterns = patterns.split()
        broken_output = output.split()

        freq += parse_broken_dial(
            signals=broken_signal_patterns,
            outputs=broken_output
        )

    return freq


if __name__ == "__main__":
    test_solution = get_solution(get_input(path_to_file=os.getcwd() + "/input_test.txt"))
    if test_solution == 26:
        print("TEST PASSED")
        print(get_solution(get_input(path_to_file=os.getcwd() + "/input.txt")))
    else:
        print(test_solution)
        print("Test failed")
