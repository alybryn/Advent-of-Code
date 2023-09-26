import pathlib
#import pytest
import aoc_template as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

def example1():
    puzzle_input = (PUZZLE_DIR / "sample.txt").read_text().strip()
    return aoc.parse(puzzle_input)