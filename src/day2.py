"""Day 2: Dive!"""

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Callable

INPUT_PATH = 'input/day2.txt'


class InstructionType(Enum):
    """Enum defining possible types of submarine instructions."""

    FORWARD = auto()
    DOWN = auto()
    UP = auto()


@dataclass
class Instruction:
    """An individual instruction."""

    instruction_type: InstructionType
    value: int


@dataclass
class Submarine:
    """Represents a submarine with a depth and horizontal position."""

    position: int = 0
    depth: int = 0

    instruction_map: dict[InstructionType, Callable[[int], None]] = field(init=False)

    def __post_init__(self):
        self.instruction_map = {
            InstructionType.FORWARD: self.move_forward,
            InstructionType.DOWN: self.move_down,
            InstructionType.UP: self.move_up,
        }

    def process_instruction(self, instruction: Instruction) -> None:
        """Process a single instruction."""
        self.instruction_map[instruction.instruction_type](instruction.value)

    def move_forward(self, value: int):
        """Move submarine forward."""
        self.position += value

    def move_down(self, value: int):
        """Move submarine down."""
        self.depth += value

    def move_up(self, value: int):
        """Move submarine up. Assuming we can't have negative depth."""
        self.depth -= value
        self.depth = max(0, self.depth)

    def calculate_norm(self) -> int:
        """Calculate the product of the horizontal position and depth."""
        return self.position * self.depth


class AimSubmarine(Submarine):
    """
    Represents a submarine with an aiming mechanic that determines depth rather
    than being able to move up and down at will.
    """

    aim: int = 0

    def move_forward(self, value: int):
        """
        Move submarine forward in the aimed direction. Assume we can't have
        negative depth.
        """
        self.position += value
        self.depth += self.aim * value
        self.depth = max(0, self.depth)

    def move_down(self, value: int):
        """Point submarine down."""
        self.aim += value

    def move_up(self, value: int):
        """Point submarine up."""
        self.aim -= value


def parse_input(input_string: str) -> list[Instruction]:
    """
    Parse input to list of instruction objects. Assume input is a list of
    instructions separated by newlines. Each instruction is in the form:
    INSTRUCTION VALUE
    """
    input_string = input_string.strip()
    lines = input_string.splitlines()
    pairs = [line.split() for line in lines]
    instructions = [
        Instruction(InstructionType[instruction_string.upper()], int(value_string))
        for instruction_string, value_string in pairs
    ]
    return instructions


def calculate_submarine_norm(
    submarine: Submarine, instructions: list[Instruction]
) -> int:
    """
    Calculate the product of the submarine's horizontal position and depth after
    following a set of instructions.
    """
    for instruction in instructions:
        submarine.process_instruction(instruction)
    return submarine.calculate_norm()


def solve_part1() -> int:
    """Solve the puzzle for part 1 with the official input."""
    with open(INPUT_PATH, encoding='utf-8') as f:
        input_text = f.read()
    input_instructions = parse_input(input_text)
    submarine = Submarine()
    return calculate_submarine_norm(submarine, input_instructions)


def solve_part2() -> int:
    """Solve the puzzle for part 2 with the official input."""
    with open(INPUT_PATH, encoding='utf-8') as f:
        input_text = f.read()
    input_instructions = parse_input(input_text)
    submarine = AimSubmarine()
    return calculate_submarine_norm(submarine, input_instructions)


def test_example_part1():
    """Test case provided in prompt for part 1."""
    sample_input = """
        forward 5
        down 5
        forward 8
        up 3
        down 8
        forward 2
    """
    expected_output = 150

    input_instructions = parse_input(sample_input)
    submarine = Submarine()
    assert calculate_submarine_norm(submarine, input_instructions) == expected_output


def test_example_part2():
    """Test case provided in prompt for part 2."""
    sample_input = """
        forward 5
        down 5
        forward 8
        up 3
        down 8
        forward 2
    """
    expected_output = 900

    input_instructions = parse_input(sample_input)
    submarine = AimSubmarine()
    assert calculate_submarine_norm(submarine, input_instructions) == expected_output


if __name__ == '__main__':
    test_example_part1()

    part1_solution = solve_part1()
    print(part1_solution)

    test_example_part2()

    part2_solution = solve_part2()
    print(part2_solution)
