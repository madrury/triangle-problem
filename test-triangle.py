from triangle import max_path

def test_one_row():
    triangle = [[1]]
    assert max_path(triangle) == 1

def test_two_rows():
    triangle = [
        [1],
        [1, 2]]
    assert max_path(triangle) == 3

def test_middle():
    triangle = [
        [1],
        [2, 1],
        [1, 3, 2],
        [1, 2, 4, 1]]
    assert max_path(triangle) == 10

def test_antagonist():
    triangle = [
        [2],
        [2, 2],
        [0, 2, 2],
        [0, 0, 2, 2],
        [100, 0, 0, 2, 2]]
    assert max_path(triangle) == 104
