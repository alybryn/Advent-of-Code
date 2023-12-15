import pathlib
import sys

SAMPLE_ANSWER_1 = 1320
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    return [chunk for chunk in puzzle_input.split(',')]

def hash(chunk):
    ret = 0
    for c in chunk:
        ret += ord(c)
        ret = ret * 17
        ret = ret%256
    return ret

class Boxes():
    def __init__(self) -> None:
        self._boxes = {}

    def process(self, instruction):
        label, *lens = instruction.split(',')
        box = hash(label)
        if '-' in instruction:
            # remove lens with label from box h
            self.remove(box, label)
        else: # '=' in chunk
            self.place(box, label, lens[0])
    
    # remove the lens with the given label if it is present
    # any other lenses should be moved forward
    def remove(self, box, label):
        unshelved = self._boxes.get(box, [])
        if label in unshelved:
            i = list

    def place(self, box, label, lens):
        unshelved = self._boxes.get(box, [])
        if label

    def focusing_power(self):
        ret = 0
        for k in self._boxes.keys():
            for l in self._boxes.get(k):
                pass

    def __str__(self) -> str:
        p = ''
        for k in self._boxes.keys():
            p += f'Box {k}: '
            for l in self._boxes.get(k):
                p += str(l)
        return p

def part1(parsed):
    ret = 0
    for chunk in parsed:
        ret += hash(chunk)
    return ret

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