import os
import functools

from libraries.helpers import get_input


def get_winning_number_sets(board):
    winner_sets = []
    for row in board:
        winner_sets.append(set(row))
    for i in range(len(board[0])):
        bingo_set = [
            int(row[i])
            for row in board
        ]
        winner_sets.append(set(bingo_set))
    
    return winner_sets


def check_boards_for_winners(picks, all_winning_rows):
    for idx, row in enumerate(all_winning_rows):
        if len(row.intersection(set(picks))) == 5:
            print("bingo!")
            print(f"Board winner: {(idx // 10)}")
            return idx // 10


def play_bingo(boards, pick_order):
    picks = pick_order[0:5]
    print(f"First picks: {picks}")
    all_winning_rows = []
    for board in boards:
        all_winning_rows += board
    
    for new_pick in pick_order[5:]:
        print(f"New pick: {new_pick}")
        picks.append(new_pick)
        winning_board = check_boards_for_winners(picks, all_winning_rows)        
        if winning_board:
            return winning_board, picks

def calculate_board_score(board, picks):
    unchecked_sum = 0
    final_set = set()
    for row in board:
        final_set = final_set.union(row-set(picks))
        
    unchecked_sum += functools.reduce(lambda a, b: a+b, list(final_set))

    print(f"Board score: {unchecked_sum * picks[-1]}")
    return unchecked_sum * picks[-1]

def get_bingo_result(content):
    pick_order = list(map(lambda x: int(x), content[0].split(',')))
    board_rows = [line for line in content[1:] if line]
    boards = []

    for x in range(len(board_rows)//5):
        board = [
            list(map(lambda x: int(x), row.split()))
            for row in board_rows[x*5:(x+1)*5]
        ]
        bingo_sets = get_winning_number_sets(board)
        boards.append(bingo_sets)

    winning_board_idx, winning_numbers = play_bingo(boards, pick_order)
    return calculate_board_score(boards[winning_board_idx], winning_numbers)


def check_test_case():
    content = get_input(path_to_file=os.getcwd() + "/input_test.txt")
    if get_bingo_result(content) == 4512:
        print("test case Passed")
        return True
    else:
        return False


if __name__ == "__main__":
    if check_test_case():
        content = get_input(path_to_file=os.getcwd() + "/input.txt")
        print(get_bingo_result(content))