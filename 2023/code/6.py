import pathlib
import re
import sys

SAMPLE_ANSWER_1 = 288
SAMPLE_ANSWER_2 = 71503

def parse(puzzle_input):
    # parse the input
    return [line for line in puzzle_input.split('\n')]

def better_times(boat_race):
    ret = 0
    race = boat_race[0]
    record = boat_race[1]
    for hold in range(race):
        speed = hold
        travel_time = race - hold
        if record < speed * travel_time:
            ret += 1
    return ret

def part1(parsed):
    ret = 1
    races = [int(r) for r in re.findall(r'\d+', parsed[0])]
    record = [int(r) for r in re.findall(r'\d+', parsed[1])]
    for boat_race in zip(races, record):
        ret = ret * better_times(boat_race)
    return ret

def part2(parsed):
    time = [r for r in re.findall(r'\d+', parsed[0])]
    record = [r for r in re.findall(r'\d+', parsed[1])]
    print([int(''.join(time)), int(''.join(record))])
    return better_times((int(''.join(time)), int(''.join(record))))

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