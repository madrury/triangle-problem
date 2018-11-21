def max_path(triangle):
    current_maximums = triangle[0]
    for i, row in enumerate(triangle[1:], start=1):
        current_maximums = _update_maximums(row, current_maximums)
    return max(current_maximums)

def _update_maximums(current_row, current_maximums):
    assert len(current_row) == len(current_maximums) + 1
    new_maximums = [None] * len(current_row)
    for i, n in enumerate(current_row):
        above_idxs = _above_idxs(i, len(current_row))
        new_maximums[i] = max(n + current_maximums[idx] for idx in above_idxs)
    return new_maximums

def _above_idxs(idx, row_idx):
    if idx == 0:
        yield 0
    elif idx == row_idx - 1:
        yield idx - 1
    else:
        yield idx - 1
        yield idx
