import pathlib
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    return [line for line in puzzle_input.split()]


class AlmanacMap():
    def __init__(self) -> None:
        pass

class Almanac():
    def __init__(self, seeds, maps) -> None:
        self._seeds = seeds
        self._seed_to_fertilizer = maps[0]
        self._fertilizer_to_water = maps[1]
        self._water_to_light = maps[2]
        self._light_to_temperature = maps[3]
        self._temperature_to_humidity = maps[4]
        self._humidity_to_location = maps[5]

def something(source, maps):
    for map in maps:
        if source in range(map[1], map[1] + map[2]):
            return 3

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