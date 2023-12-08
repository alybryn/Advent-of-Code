import pathlib
import sys

SAMPLE_ANSWER_1 = 6
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    left_right, nodes = puzzle_input.split('\n\n')
    left_right = list(left_right)
    nodes = [[''.join([l[0], l[1], l[2]]), ''.join([l[7], l[8], l[9]]), ''.join([l[12], l[13], l[14]])] for l in nodes.split('\n')]
    graph = Graph(left_right, nodes)
    return graph


class Node():
    # strings, not objects
    def __init__(self, params) -> None:
        self._name = params[0]
        self._left = params[1]
        self._right = params[2]

    def __str__(self) -> str:
        return f'{self._name} = ({self._left}, {self._right})'
    
    @property
    def left(self):
        return self._left
    
    @property
    def right(self):
        return self._right

class Graph():
    def __init__(self, left_and_right, nodes_input) -> None:
        self._lr = left_and_right
        self._nodes = {}
        for node in nodes_input:
            self._nodes.update({node[0]: Node(node)})

    # def make_nodes(self, nodes_input):
    #     for node in nodes_input:
    #         self._nodes.update({node[0]: Node(node)})
    #     self._is_noded = True

    # def link_nodes(self):
    #     self._is_linked = True

    def __str__(self) -> str:
        ret = f"{''.join(self._lr)}"
        for k in self._nodes.keys():
            ret += '\n'
            ret += self._nodes.get(k).__str__()
        return ret

def part1(parsed):
    return parsed

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