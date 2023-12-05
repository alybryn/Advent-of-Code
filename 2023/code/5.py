import pathlib
import re
import sys

SAMPLE_ANSWER_1 = 35
SAMPLE_ANSWER_2 = 46

def parse(puzzle_input):
    # parse the input
    lines = puzzle_input.split('\n\n')
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
        # range does this for me
        # self._sr_end = source_range_start + range_length - 1
        self._rl = range_length
    
    def map(self, input):
        if input in range(self._srs, self._srs + self._rl):
            # print(f'\t{input} is in {self._srs} - {self._srs + self._rl - 1}')
            diff = input - self._srs
            return self._drs + diff
        # print(f'\t{input} not in {self._srs} - {self._srs + self._rl - 1}')

    def __repr__(self) -> str:
        return f'AlmanacMap: {self._drs}, {self._srs}, {self._rl}, {self._srs + self._rl - 1}'

def map_a_seed(input, mapses):
    num = input
    for maps in mapses:
        # print(num)
        becomes = None
        for map in maps:
            # print(f'\t{map}')
            becomes = map.map(num)
            if becomes:
                break
        if becomes:
            num = becomes
    # print(f'Mapped seed {input} to loc {num}')
    return num

def part1(parsed):
    seeds = parsed[0]
    mapses = parsed[1]
    ret = []
    for seed in seeds:
        ret.append(map_a_seed(seed, mapses))
    return min(ret)

def part2(parsed):
    # reimagine seeds as ranges
    seeds = parsed[0]
    seeds_to_map = []
    i = 0
    while i < len(seeds):
        print(i)
        for seed in range(seeds[i], seeds[i] + seeds[i+1]):
            seeds_to_map.append(seed)
            print(f'adding seed {seed}')
        i += 2
    mapses = parsed[1]
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