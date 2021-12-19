"""Day 3: Binary Diagnostic"""

from __future__ import annotations
from dataclasses import dataclass

INPUT_PATH = 'input/day3.txt'


@dataclass
class BitString:
    """A string of bits with functions to manipulate them."""

    bits: list[int]

    def __int__(self):
        return int(''.join([str(bit) for bit in self.bits]), 2)

    def __len__(self):
        return len(self.bits)

    def __repr__(self):
        return ''.join([str(bit) for bit in self.bits])

    def get_bit(self, position: int) -> int:
        """
        Get an individual bit at the given position, where the most-significant
        bit is position 0.
        """
        assert position < len(self.bits)
        return self.bits[position]

    def flip(self) -> BitString:
        """Flips all bits and return a new BitString."""
        flipped_bits = ['1' if bit == 0 else '0' for bit in self.bits]
        return BitString.from_str(''.join(flipped_bits))

    @staticmethod
    def from_int(value: int, length: int) -> BitString:
        """Create a BitString from an int."""
        as_string = BitString.int_repr(value, length)
        return BitString.from_str(as_string)

    @staticmethod
    def from_str(s: str) -> BitString:
        """Create a BitString from a string."""
        return BitString([int(c) for c in list(s)])

    @staticmethod
    def int_repr(value: int, length: int) -> str:
        """
        Convert an integer to a bit string, as a Python string (not the class
        representation).
        """
        return f'{value:0>{length}b}'


@dataclass
class DiagnosticReport:
    """Represents a diagnostic report of binary records."""

    records: list[BitString]

    @property
    def bit_length(self) -> int:
        """Get the length of the report's bit strings."""
        return len(self.records[0])

    @property
    def gamma_rate(self) -> int:
        """The most common bit at each position of all the individual records."""
        most_common_bits = []
        for i in range(self.bit_length):
            ones = sum(record.get_bit(i) for record in self.records)
            most_common_bits.append('1' if ones > len(self.records) // 2 else '0')
        bitstring = ''.join(most_common_bits)
        return int(BitString.from_str(bitstring))

    @property
    def epsilon_rate(self) -> int:
        """
        The least common bit at each position of all the individual records, or
        alternatively, the ones' complement of the gamma rate.
        """
        gamma_bitstring = BitString.from_int(self.gamma_rate, self.bit_length)
        return int(gamma_bitstring.flip())

    @property
    def power_consumption(self) -> int:
        """Product of gamma rate and epsilon rate."""
        return self.gamma_rate * self.epsilon_rate


def parse_input(input_string: str) -> list[BitString]:
    """
    Parse input strings into list of BitString objects. Assuming inputs are
    records separated by newlines, where each record is a string of bits (0/1)
    and all are the same length.
    """
    input_string = input_string.strip()
    return [BitString.from_str(line.strip()) for line in input_string.splitlines()]


def solve_part1() -> int:
    """Solve the puzzle for part 1 with the official input."""
    with open(INPUT_PATH, encoding='utf-8') as f:
        input_text = f.read()
    records = parse_input(input_text)
    report = DiagnosticReport(records)
    return report.power_consumption


def solve_part2() -> int:
    """Solve the puzzle for part 2 with the official input."""
    with open(INPUT_PATH, encoding='utf-8') as f:
        input_text = f.read()
    records = parse_input(input_text)
    report = DiagnosticReport(records)
    raise NotImplementedError


def test_example_part1():
    """Test case provided in prompt for part 1."""
    sample_input = """
        00100
        11110
        10110
        10111
        10101
        01111
        00111
        11100
        10000
        11001
        00010
        01010
    """
    expected_output = 198

    records = parse_input(sample_input)
    report = DiagnosticReport(records)
    assert report.power_consumption == expected_output


def test_example_part2():
    """Test case provided in prompt for part 2."""
    sample_input = """
        00100
        11110
        10110
        10111
        10101
        01111
        00111
        11100
        10000
        11001
        00010
        01010
    """
    expected_output = 230

    records = parse_input(sample_input)
    report = DiagnosticReport(records)
    raise NotImplementedError


def test_bitstring_repr():
    """Test BitString __repr__ method."""
    assert str(BitString.from_str('10101')) == '10101'
    assert str(BitString.from_str('01010')) == '01010'
    assert str(BitString.from_str('11000')) == '11000'
    assert str(BitString.from_str('00011')) == '00011'
    assert str(BitString.from_str('101')) == '101'
    assert str(BitString.from_str('010')) == '010'


def test_bitstring_get_bit():
    """Test BitString get_bit method."""
    s = '1010'
    bitstring = BitString.from_str(s)
    assert bitstring.get_bit(0) == 1
    assert bitstring.get_bit(1) == 0
    assert bitstring.get_bit(2) == 1
    assert bitstring.get_bit(3) == 0


def test_bitstring_flip():
    """Test BitString flip method."""
    assert str(BitString.from_str('10101').flip()) == '01010'
    assert str(BitString.from_str('01010').flip()) == '10101'
    assert str(BitString.from_str('11000').flip()) == '00111'
    assert str(BitString.from_str('00011').flip()) == '11100'
    assert str(BitString.from_str('101').flip()) == '010'
    assert str(BitString.from_str('010').flip()) == '101'


if __name__ == '__main__':
    test_bitstring_repr()
    test_bitstring_get_bit()
    test_bitstring_flip()

    test_example_part1()

    part1_solution = solve_part1()
    print(part1_solution)
    assert part1_solution == 852500  # Verified correct

    # test_example_part2()

    # part2_solution = solve_part2()
    # print(part2_solution)
