import pathlib
import sys

SAMPLE_ANSWER_1 = 198
SAMPLE_ANSWER_2 = 230

def parse(puzzle_input):
    # parse the input
    return Diagnostic([line for line in puzzle_input.split()])

class Diagnostic():
    def __init__(self, output: [str]):
        #self._output = output
        self._count = len(output)
        self._width = len(output[0])
        self._ones_count = [0] * self._width
        # zeros_count[i] is self._count - self._ones_count[i]
        for l in output:
            for i in range(0, self._width):
                if l[i] == '1':
                    self._ones_count[i] += 1
        
    @property
    def gammaRate(self):
        s = ''
        for i in range(0, self._width):
            # if 1s > 0s
            if self._ones_count[i] > self._count - self._ones_count[i]:
                s += '1'
            else:
                s += '0' 
        return int(s, 2)
    
    @property
    def epsilonRate(self):
        s = ''
        for i in range(0, self._width):
            # if 1s < 0s
            if self._ones_count[i] < self._count - self._ones_count[i]:
                s += '1'
            else:
                s += '0' 
        return int(s, 2)

    @property
    def powerRate(self):
        return self.gammaRate * self.epsilonRate

    @property
    def o2Rate(self):
        return 0
        remainingCodes = self._output
        index = 0
        while len(remainingCodes) > 1:
            zeros = []
            ones = []
            for l in remainingCodes:
                if list(l)[index] == "1":
                    ones.append(1)


def part1(d):
    return d.powerRate 

def part2(d):
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