import math
import os

from libraries.helpers import get_input


def convert_to_value(bin_string):
    sum = 0
    for idx in range(len(bin_string)):
        bit_flag = bin_string[len(bin_string)-1-idx]
        sum += (math.pow(2, idx))*int(bit_flag)
    return int(sum)
    
def parse_bin_string(bin_string):
    version = convert_to_value(bin_string[:3])
    type = bin_string[3:6]


    if convert_to_value(type) == 4:
        packet = list(bin_string[6:])
        # Ignore padding 0s for now
        # while len(packet) // 4 != 0 and packet[0] != '1':
        #     packet.pop(0)
        packet_bin_string = ''
        while len(packet) > 0:
            packet_prefix = packet.pop(0)
            group = packet[0:4]
            packet_bin_string += ''.join(group)
            packet = packet[4:]
            if packet_prefix == '0':
                break
            
        return version, packet_bin_string, packet
        
    else:
        length_id = bin_string[6]
        if length_id == '0':
            # Next 15 bits are total length
            length = convert_to_value(bin_string[7:22])
            packets = bin_string[22:(22+length)]
            parsed_packets = []

            while packets != len(packets) > 0: # Check if its just trailing 0s
                subpacket_version, packet_bin_string, packets = parse_bin_string(packets)
                if packet_bin_string:
                    parsed_packets.append(packet_bin_string)
                    version += subpacket_version
            
            return version, parsed_packets, bin_string[22+length:]


        else:
            # Next 11 are number of packets
            num_packets = convert_to_value(bin_string[7:18])
            packets = bin_string[18:]
            parsed_packets = []
            for x in range(num_packets):
                subpacket_version, packet_bin_string, packets = parse_bin_string(packets)
                if packet_bin_string:
                    parsed_packets.append(packet_bin_string)
                    version += subpacket_version
            return version, parsed_packets, packets


def get_solution(content):
    BITS_transmission = content[0]
    hex_map = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }

    bin_string = ''
    for char in BITS_transmission:
        bin_string += hex_map[char]

    version, *args = parse_bin_string(bin_string)

    return version


if __name__ == "__main__":
    test_solution = get_solution(get_input(path_to_file=os.getcwd() + "/input_test.txt"))
    if test_solution == 31:
        print("TEST PASSED")
        print(get_solution(get_input(path_to_file=os.getcwd() + "/input.txt")))
        
    else:
        print(test_solution)
        print("Test failed")
