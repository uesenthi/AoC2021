import os

from libraries.helpers import get_input

if __name__ == "__main__":
    content = get_input(path_to_file=os.getcwd() + "/input.txt")

    position = [0, 0, 0] # horizontal, depth, aim
    for line in content:
        direction, distance = line.split()
        if direction == "forward":
            position[0] += int(distance)
            position[1] += position[2] * int(distance)
        elif direction == "down":
            position[2] += int(distance)
        elif direction == "up":
            position[2] -= int(distance)
    
    print(f"X:{position[0]}, Y:{position[1]}")
    print(f"Product: {position[0] * position[1]}")
