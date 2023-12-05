import pathlib
import re
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    lines = puzzle_input.split('\n\n')
    # seeds = [int(l) for l in lines[0].split(' ')[1:]]
    # # seed -> fertilizer
    # fertilizer_ints = [[int(i) for i in l.split(' ')] for l in lines[1].split('\n')[1:]]
    # fertilizer = [AlmanacMap(i[0], i[1], i[2]) for i in [f for f in fertilizer_ints]]
    # # fertilizer -> water
    # lines[2]
    # # water -> light
    # lines[3]
    # # light -> temperature
    # lines[4]
    # # temperature -> humidity
    # lines[5]
    # # humidity -> location
    # lines[6]
    seeds = []
    maps = []
    for line in lines:
        if re.match(r'^seeds:', line):
            seeds = [int(l) for l in line.split(' ')[1:]]
        else:
            ints = [[int(i) for i in l.split(' ')] for l in line.split('\n')[1:]]
            maps.append([AlmanacMap(i[0], i[1], i[2]) for i in [f for f in ints]])

    return seeds, maps

class AlmanacMap():
    def __init__(self, destination_range_start, source_range_start, range_length) -> None:
        self._drs = destination_range_start
        self._srs = source_range_start
        self._sr_end = source_range_start + range_length - 1
        self._rl = range_length
    
    def map(self, input):
        if input in range(self._srs, self._sr_end):
            diff = input - self._srs
            return self._drs + diff

    def __repr__(self) -> str:
        return f'AlmanacMap: {self._drs}, {self._srs}, {self._rl}, (optionally) {self._sr_end}'

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
    print(parsed)
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