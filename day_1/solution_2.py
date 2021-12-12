from solution_1 import get_input


def get_slice_sum(array, start_idx, offset):
    sum = 0
    for i in range(start_idx - offset, start_idx):
        sum += array[i]

    return sum + array[start_idx]

if __name__ == "__main__":
    content = get_input()
    increase_freq = 0

    for idx, val in enumerate(content):
        # Only start when idx is 3 or more
        if idx < 2:
            continue
        
        if get_slice_sum(content, idx-1, 2) < get_slice_sum(content, idx, 2):
            increase_freq += 1
    
    print(f"Number of increases: {increase_freq}")
