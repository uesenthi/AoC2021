import os

from libraries.helpers import get_input
from day_4.solution_1 import get_winning_number_sets, calculate_board_score


def check_boards_for_winners(picks, all_winning_rows):
    winning_boards = set()
    for idx, row in enumerate(all_winning_rows):
        if len(row.intersection(set(picks))) == 5:
            winning_boards.add(idx//10)
    return list(winning_boards) if len(winning_boards) > 0 else None


def play_bingo(boards, pick_order):
    picks = pick_order[0:5]
    all_winning_rows = []

    winning_boards = []
    winning_picks = []

    for board in boards:
        all_winning_rows += board
    
    for new_pick in pick_order[5:]:
        picks.append(new_pick)
        winning_board_idx = check_boards_for_winners(picks, all_winning_rows)   
        if isinstance(winning_board_idx, list):
            for board in winning_board_idx:
                winning_boards.append(boards[board])
                winning_picks.append(picks.copy())
            
            # Reset winning rows and remove winning boards
            all_winning_rows.clear()
            boards = [
                board
                for idx, board in enumerate(boards)
                if idx not in winning_board_idx
            ]
            for board in boards:
                all_winning_rows += board
    return winning_boards[-1], winning_picks[-1]


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

    winning_board, winning_numbers = play_bingo(boards, pick_order)
    return calculate_board_score(winning_board, winning_numbers)


def check_test_case():
    content = get_input(path_to_file=os.getcwd() + "/input_test.txt")
    if get_bingo_result(content) == 1924:
        print("test case Passed")
        return True
    else:
        raise Exception("Test case failed")
        return False


if __name__ == "__main__":
    if check_test_case():
        content = get_input(path_to_file=os.getcwd() + "/input.txt")
        print(get_bingo_result(content))