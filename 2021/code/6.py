import pathlib
import sys

SAMPLE_ANSWER_1 = 5934
SAMPLE_ANSWER_2 = 26984457539


def parse(puzzle_input):
    # parse the input
    return [int(line) for line in puzzle_input.split(",")]


class School:
    def __init__(self, lanternfish) -> None:
        # 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0
        self._lanternfish = {}
        counts = {}
        for i in range(9):
            self._lanternfish.update({i:sum([1 for l in lanternfish if l = i])})
    
    def time_passes(self):
        temp = self._lanternfish.get(0)
        for i in range(6):
            if i == 6:
                self._lanternfish.update({i: self._lanternfish.get(i + 1) + temp})
            elif i == 8:
                self._lanternfish.update({i: temp})
            else:
                self._lanternfish.update({i: self._lanternfish.get(i + 1)})

# def time_passes(initial):
#     ret = []
#     app = []
#     for lanternfish in initial:
#         if lanternfish == 0:
#             ret.append(6)
#             app.append(8)
#         else:
#             ret.append(lanternfish - 1)
#     return ret + app


def time_passes_loop(time, lanternfish):
    my_fish = School(lanternfish)
    for i in range(time):
        my_fish.time_passes()
    return len(lanternfish)


def part1(lanternfish):
    return time_passes_loop(80, lanternfish)


def part2(lanternfish):
    return time_passes_loop(256, lanternfish)


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
