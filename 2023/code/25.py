import pathlib
import sys

SAMPLE_ANSWER_1 = 54
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
class Graph():
    def __init__(self) -> None:
        self._edges = {}
    
    def add_edge(self, a, b):
        a_set = self._edges.get(a,set())
        a_set.add(b)
        b_set = self._edges.get(b,set())
        b_set.add(a)
        self._edges.update({a:a_set})
        self._edges.update({b:b_set})

    def output(self, selections):
        printed = set()
        for k in self._edges:
            if k not in selections:
                continue
            for v in self._edges[k]:
                if v in printed:
                    continue
                print(f'{k} -> {v}')
            printed.add(k)

    def find_seed(self):
        for k in self._edges.keys():
            print(f'k:{k}')
            if len(self._edges[k]) >=3:
                consideration = self._edges[k]
                for a in consideration:
                    print(f'\ta:{a}')
                    for b in consideration:
                        if b == a:
                            continue
                        print(f'\t\tb:{b}')
                        if b in self._edges[a]:
                            for c in consideration:
                                if c == a or c == b:
                                    continue
                                print(f'\t\t\tc:{c}')
                                if c in self._edges[a] and c in self._edges[b]:
                                    return (k,a,b,c)

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