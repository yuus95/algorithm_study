from collections import deque


def solution(board):

    """
    >>> solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    900
    """

    n_rows, n_cols = len(board), len(board[0])

    COST_TURN = 500
    COST_MOVE = 100

    def is_valid_state(state):
        row, col, _ = state
        return 0 <= row < n_rows and 0 <= col < n_cols and not board[row][col]

    def get_next_cost_states(cost, state):
        row, col, is_horizontal = state
        valid_deltas = [(1, 0), (-1, 0)] if is_horizontal else [(0, 1), (0, -1)]
        next_states_turn = [(cost + COST_TURN, (row, col, not is_horizontal))]
        next_states_move_all = [
            (row + drow, col + dcol, is_horizontal) for drow, dcol in valid_deltas
        ]
        next_states_move = [
            (cost + COST_MOVE, s) for s in next_states_move_all if is_valid_state(s)
        ]
        return next_states_turn + next_states_move

    # Cost cache to prevent infinite loop
    map_cost_from_state = {}

    # BFS search
    # (cost, (row, col, is_horizontal))
    next_states = deque([(0, (0, 0, True)), (0, (0, 0, False))])
    while next_states:
        cost, state = next_states.popleft()
        cost_known = map_cost_from_state.get(state, float("inf"))
        if cost >= cost_known:
            continue
        map_cost_from_state[state] = cost
        next_states.extend(get_next_cost_states(cost, state))

    return min(
        map_cost_from_state[(n_rows - 1, n_cols - 1, True)],
        map_cost_from_state[(n_rows - 1, n_cols - 1, False)],
    )

if __name__ == "__main__":
    import doctest
    doctest.testmod()
