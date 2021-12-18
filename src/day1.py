"""Day 1: Sonar Sweep"""

INPUT_PATH = 'input/day1.txt'


def parse_input(input_string: str) -> list[int]:
    """
    Parse string input to numbers. Assume input provided as string of integers
    separated by newlines.
    """
    return [int(value) for value in input_string.splitlines()]


def count_increases(input_list: list[int]) -> int:
    """
    Count the number of times a depth increases from one item to the next.

    Parameters
    ----------
    input : list[int]
        Successive depth measurements.

    Returns
    -------
    int
        Number of times depth increases from one item to the next.
    """
    pairs = zip(input_list, input_list[1:])
    return sum(pair[1] > pair[0] for pair in pairs)


def count_rolling_increases(input_list: list[int]) -> int:
    """
    Count the number of times a rolling sum of three-measurement windows
    increases from one window to the next.

    Parameters
    ----------
    input : list[int]
        Successive depth measurements.

    Returns
    -------
    int
        Number of times sum of window depths increases from one window to the
        next.
    """
    windows = zip(input_list, input_list[1:], input_list[2:])
    window_sums = [sum(window) for window in windows]
    return count_increases(window_sums)


def solve_part1() -> int:
    """Solve the puzzle with the official input."""
    with open(INPUT_PATH, encoding='utf-8') as f:
        input_text = f.read()
    input_list = parse_input(input_text)
    return count_increases(input_list)


def solve_part2() -> int:
    """Solve the puzzle for part 2 with the official input."""
    with open(INPUT_PATH, encoding='utf-8') as f:
        input_text = f.read()
    input_list = parse_input(input_text)
    return count_rolling_increases(input_list)


def test_example_part1():
    """Test case provided in prompt."""
    sample_input = '\n'.join(
        ['199', '200', '208', '210', '200', '207', '240', '269', '260', '263']
    )
    expected_output = 7

    input_list = parse_input(sample_input)
    assert count_increases(input_list) == expected_output


def test_example_part2():
    """Test case provided in prompt for part 2."""
    sample_input = '\n'.join(
        ['199', '200', '208', '210', '200', '207', '240', '269', '260', '263']
    )
    expected_output = 5

    input_list = parse_input(sample_input)
    assert count_rolling_increases(input_list) == expected_output


def test_all_decreasing():
    """Test when depth value is always decreasing."""
    sample_input = '\n'.join(
        ['200', '190', '180', '170', '165', '150', '149', '120', '100', '0']
    )
    expected_output = 0

    input_list = parse_input(sample_input)
    assert count_increases(input_list) == expected_output


def test_same():
    """Test when depth stays constant."""
    sample_input = '\n'.join(['200', '200', '200'])
    expected_output = 0

    input_list = parse_input(sample_input)
    assert count_increases(input_list) == expected_output


if __name__ == '__main__':
    test_example_part1()
    test_all_decreasing()
    test_same()

    test_example_part2()

    part1_solution = solve_part1()
    print(part1_solution)

    part2_solution = solve_part2()
    print(part2_solution)
