import os
import functools
from collections import defaultdict

from libraries.helpers import get_input


def analyze_signal_positions(signal_lookup, unknown_signals):
    signal_1 = set(signal_lookup[1])
    signal_7 = set(signal_lookup[7])
    signal_4 = set(signal_lookup[4])
    signal_8 = set(signal_lookup[8])


    signal_0 = set()
    signal_2 = set()
    signal_3 = set()
    signal_5 = set()
    signal_6 = set()
    signal_9 = set()


    # Empty state
    position_0 = signal_7 - signal_1
    position_1 = set()
    position_2 = set()
    position_3 = set()
    position_4 = set()
    position_5 = set()
    position_6 = set()


    # interim positions
    position_1_3 = signal_4 - signal_1
    position_2_5 = signal_7.intersection(signal_1)
    position_4_6 = (signal_8 - signal_4) - position_0

    for code in unknown_signals[5]:
        code_set = set(code)
        if len(code_set - signal_4 - position_0) == 1:
            position_6 = code_set - signal_4 - position_0
            position_4 = position_4_6 - position_6
            break
    for code in unknown_signals[5]:
        code_set = set(code)
        if len(code_set - signal_7 - position_6) == 1:
            position_3 = code_set - signal_7 - position_6
            position_1 = position_1_3 - position_3
            break
    for code in unknown_signals[5]:
        code_set = set(code)
        if len(code_set - position_0 - position_1 - position_3 - position_6) == 1:
            position_5 = code_set - position_0 - position_1 - position_3 - position_6
            position_2 = position_2_5 - position_5
            break

    for code in unknown_signals[5]:
        code_set = set(code)
        remaining_bits = signal_8 - code_set

        if not ((remaining_bits - position_1) - position_5):
            signal_2 = code_set
        elif not ((remaining_bits - position_1) - position_4):
            signal_3 = code_set
        elif not ((remaining_bits - position_4) - position_2):
            signal_5 = code_set
    
    for code in unknown_signals[6]:
        code_set = set(code)
        remaining_bits = signal_8 - code_set

        if not (remaining_bits - position_2):
            signal_6 = code_set
        elif not (remaining_bits - position_4):
            signal_9 = code_set
        elif not (remaining_bits - position_3):
            signal_0 = code_set
    
    return {
        ''.join(sorted(list(signal_0))): 0,
        ''.join(sorted(list(signal_1))): 1,
        ''.join(sorted(list(signal_2))): 2,
        ''.join(sorted(list(signal_3))): 3,
        ''.join(sorted(list(signal_4))): 4,
        ''.join(sorted(list(signal_5))): 5,
        ''.join(sorted(list(signal_6))): 6,
        ''.join(sorted(list(signal_7))): 7,
        ''.join(sorted(list(signal_8))): 8,
        ''.join(sorted(list(signal_9))): 9,
    }

    # print(signal_0)
    # print(signal_1)
    # print(signal_2)
    # print(signal_3)
    # print(signal_4)
    # print(signal_5)
    # print(signal_6)
    # print(signal_7)
    # print(signal_8)
    # print(signal_9)


def parse_broken_dial(signals, outputs):
    signal_pattern_lookup = {}
    signal_pattern_reverse_lookup = {}
    mystery_signals = defaultdict(list)

    for signal in signals:
        if len(signal) == 2:
            signal_pattern_lookup[str(sorted(signal))] = 1
            signal_pattern_reverse_lookup[1] = sorted(signal)
        elif len(signal) == 3:
            signal_pattern_lookup[str(sorted(signal))] = 7
            signal_pattern_reverse_lookup[7] = sorted(signal)
        elif len(signal) == 4:
            signal_pattern_lookup[str(sorted(signal))] = 4
            signal_pattern_reverse_lookup[4] = sorted(signal)
        elif len(signal) == 7:
            signal_pattern_lookup[str(sorted(signal))] = 8
            signal_pattern_reverse_lookup[8] = sorted(signal)
        else:
            mystery_signals[len(signal)].append(signal)
    

    signal_positions = analyze_signal_positions(signal_pattern_reverse_lookup, mystery_signals)

    bit_string = ''
    for output in outputs:
        parsed_output = ''.join(sorted(output))
        bit_string += str(signal_positions[parsed_output])
    
    return int(bit_string)


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
    if test_solution == 61229:
        print("TEST PASSED")
        print(get_solution(get_input(path_to_file=os.getcwd() + "/input.txt")))
    else:
        print(test_solution)
        print("Test failed")
