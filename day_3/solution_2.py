import os

from libraries.helpers import get_input
from day_3.solution_1 import convert_string_to_binary


def filter_common_bits(content, pos=0, find_most_common=True):
    if len(content) == 1:
        return content.pop()
    common_sum = 0
    # Grab only at position 0
    for code in content:
        common_sum += int(code[pos])
    
    if find_most_common:
        most_common = '1' if common_sum >= len(content) / 2 else '0'
        filtered_most_common_content = [
            code for code in content if code[pos] == most_common
        ]

        return filter_common_bits(filtered_most_common_content, pos + 1, find_most_common)
    else:
        least_common = '1' if common_sum < len(content) / 2 else '0'
        filtered_least_common_content = [
            code for code in content if code[pos] == least_common
        ]

        return filter_common_bits(filtered_least_common_content, pos + 1, find_most_common)

if __name__ == "__main__":
    content = get_input(path_to_file=os.getcwd() + "/input.txt")
    oxygen_generator_rating = filter_common_bits(content, 0, True)
    co2_scrubber_rating = filter_common_bits(content, 0, False)
    print(convert_string_to_binary(oxygen_generator_rating) * convert_string_to_binary(co2_scrubber_rating))
