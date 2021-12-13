import os
from collections import defaultdict

from libraries.helpers import get_input


def convert_string_to_binary(binary_str):
    sum = 0
    for pos in range(len(binary_str)):
        if int(binary_str[-1 * (pos + 1)]):
            sum += pow(2, pos * int(binary_str[-1 * (pos + 1)]))
    
    return sum



def get_common_bits(content):
    agg = defaultdict(int)
    for code in content:
        for idx, digit in enumerate(code):
            agg[idx] += int(digit)
    
    most_common = ''
    least_common = ''
    for val in agg.values():
        if val > len(content) / 2:
            most_common += '1'
            least_common += '0'
        else:
            most_common += '0'
            least_common += '1'

    return most_common, least_common


if __name__ == "__main__":
    content = get_input(path_to_file=os.getcwd() + "/input.txt")
    most_common, least_common = get_common_bits(content)

    print(convert_string_to_binary(most_common) * convert_string_to_binary(least_common))
