

def get_input():
    fs_content = []
    with open("input.txt") as file:
        for line in file:
            try:
                value = int(line)
                fs_content.append(value)
            except TypeError:
                continue
    if len(fs_content) != 2000:
        raise Exception("Failed to parse all of input")
    return fs_content

if __name__ == "__main__":
    content = get_input()
    increase_freq = 0
    for idx, _ in enumerate(content):
        if idx == 0:
            continue
        elif content[idx] > content[idx-1]:
            increase_freq += 1
    print(f"Number of increases: {increase_freq}")
