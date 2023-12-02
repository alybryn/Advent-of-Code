from enum import Enum
import pathlib
import re
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input

    # return a dict in form: 
    # {<game #> : [{Color.RED: #, Color.BLUE: #, Color.GREEN: #}
    for line in puzzle_input.split():
        pattern = r''
# (?::|; )(((\d blue|\d green|\d red),? )+)
# ^Game (\d+): ((\d+ (red|blue|green),? )+)
# ^Game (\d+)
# (?::|;)(?<blah>( \d+ red,?| \d+ blue,?| \d+ green,?){1,3})(?=;?)


class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'


def part1(parsed):
    return 0

def part2(parsed):
    return 0

def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}")
        puzzle_input = pathlib.Path(path).read_text().strip()

        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))