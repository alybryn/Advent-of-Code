import pathlib
import sys

SAMPLE_ANSWER_1 = 6
SAMPLE_ANSWER_2 = 6

def parse(puzzle_input):
    # parse the input
    left_right, nodes = puzzle_input.split('\n\n')
    left_right = list(left_right)
    nodes = [[''.join([l[0], l[1], l[2]]), ''.join([l[7], l[8], l[9]]), ''.join([l[12], l[13], l[14]])] for l in nodes.split('\n')]
    graph = Graph(left_right, nodes)
    return graph

def lcm(numbers):
    factorizations = []
    for number in numbers:
        factorizations.append(factorize(number))
    ret = {}
    for factorization in factorizations:
        for k in factorization.keys():
            ret.update({k: max(factorization.get(k), ret.get(k, 0))})
    return ret

def factorize(number):
    factors = []
    # print(f'the number is {number} which is prime? {is_prime(number)}\nFirst factor is {first_factor(number)}')
    while not is_prime(number):
        # print(number)
        factor = first_factor(number)
        factors.append(factor)
        number = number // factor
        
    factors.append(number)

    ret = {}
    for factor in set(factors):
        ret.update({factor: factors.count(factor)})

    return ret

def is_prime(number):
    return first_factor(number) == 1

def first_factor(number):
    # print(number)
    for i in range(number//2):
        if number%(i+1) == 0 and i+1 != 1:
            return i + 1
    return 1

# def factor(n):
#     ret = []
#     for i in range(n//2):
#         if n%(i+1) == 0:
#             ret.append(i+1)
#     return ret

class Node():
    # strings, not objects
    def __init__(self, params) -> None:
        self._name = params[0]
        self._left = params[1]
        self._right = params[2]

    def __str__(self) -> str:
        return f'{self._name} = ({self._left}, {self._right})'
    
    def get(self, left_or_right):
        if left_or_right == 'L':
            return self._left
        elif left_or_right == 'R':
            return self._right
        else:
            print(f"Unaccessable code accessed. Node.get({left_or_right})")
    
    @property
    def name(self):
        return self._name

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

    # start: str, end: list(str)
    def traverse(self, start, end):
        dir_pointer = 0
        count = 0
        node = self._nodes.get(start)
        while node.name not in end:
            node = self.get_next_for(node, dir_pointer)

            dir_pointer += 1
            if dir_pointer == len(self._lr):
                dir_pointer = 0
            
            count += 1
        return count
    
    # dep
    # def traverse_twice(self, start, end):
    #     dir_pointer = 0
    #     count = 0
    #     once = False
    #     node = self._nodes.get(start)
    #     while node.name not in end or not once:
    #         if node.name in end:
    #             once = True
    #         node = self.get_next_for(node, dir_pointer)

    #         dir_pointer += 1
    #         if dir_pointer == len(self._lr):
    #             dir_pointer = 0
            
    #         count += 1
    #     return count
        
    def ghost_traversal(self, start, end):
        start_names = []
        end_names = []
        for k in self._nodes.keys():
            if k.endswith(start):
                start_names.append(k)
            elif k.endswith(end):
                end_names.append(k)
        
        counts = []
        for name in start_names:
            # counts.append(self.traverse_twice(name, end_names) == self.traverse(name, end_names) * 2)
            counts.append(self.traverse(name, end_names))
        
        return lcm(counts)
    
    # def single_ghost_traversal(self, node):
    #     dir_pointer = 0
    #     count = 0
    #     while not node.name.endswith('Z'):
    #         node = self.get_next_for(node, dir_pointer)

    #         dir_pointer += 1
    #         if dir_pointer == len(self._lr):
    #             dir_pointer = 0
            
    #         count += 1
    #     return count

    def get_next_for(self, node, dir_pointer):
        return self._nodes.get(node.get(self._lr[dir_pointer]))

    def __str__(self) -> str:
        ret = f"{''.join(self._lr)}"
        for k in self._nodes.keys():
            ret += '\n'
            ret += self._nodes.get(k).__str__()
        return ret

def part1(parsed):
    return 11 #parsed.traverse('AAA', ['ZZZ'])

def part2(parsed):
    print(factorize(6))
    print(factorize(12))
    print(factorize(24))
    print(factorize(23))
    print(lcm([6, 12,24, 15]))
    return parsed.ghost_traversal('A', 'Z')

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