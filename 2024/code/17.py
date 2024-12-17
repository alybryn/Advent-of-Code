DAY = 17

START = f'/workspaces/Advent of Code/2024'
SAMPLE_PATH = f'{START}/sample/{DAY}.txt'
DATA_PATH = f'{START}/data/{DAY}.txt'

ONLY_ARGS = []
ONLY_SAMPLE = [SAMPLE_PATH]
ONLY_DATA = [DATA_PATH]
ALL = [SAMPLE_PATH, DATA_PATH]

RUN = ONLY_SAMPLE

# --------------------------------

import pathlib
import re
import sys

SAMPLE_ANSWER_1 = 4,6,3,5,6,3,5,2,1,0
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    registers,instructions = puzzle_input.split('\n\nProgram: ')
    a,b,c = re.findall(r'\d+',registers)
    instructions = [int(i) for i in instructions.split(',')]
    opcodes = [code for i,code in enumerate(instructions) if i%2==0]
    operands = [op for i, op in enumerate(instructions) if i%2==1]
    print(opcodes,operands)
    return Computer(a,b,c,instructions)

class Computer:
    def __init__(self, a, b, c, instructions):
        self._register_a = a
        self._register_b = b
        self._register_c = c
        self._instructions = instructions
        self._ptr = 0
    
    def run(self):
        while ptr < len(self. _instructions):
            op = self.interpret_instruction(self._instructions[ptr])
            op(self._instructions[ptr+1])
            ptr += 2

    def interpret_instruction(self, opcode):
        match opcode:
            case 0: return self.adv
            case 1: return self.bxl
            case 3: return self.jnz
            case 4: return self.bxc
            case 5: return self.out
            case 6: return self.bdv
            case 7: return self.cdv
            case _: print(f'unknown opcode: {opcode}')

    def interpret_combo(self, operand):
        match operand:
            case 0: return 0
            case 1: return 1
            case 2: return 2
            case 3: return 3
            case 4: return self._register_a
            case 5: return self._register_b
            case 6: return self._register_c
            case _: print(f'unknown combo operand: {operand}')

    # A division by 2^operand
    # combo operand, truncate
    # -> A
    def adv(self, combo):
        pass

    # The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand, then stores the result in register B.
    def bxl(self, lit):
        pass

    # The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to the B register.
    def bst(self, combo):
        pass

    # The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero, it jumps by setting the instruction pointer to the value of its literal operand; if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
    def jnz(self, lit):
        pass

    # The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B. (For legacy reasons, this instruction reads an operand but ignores it.)
    def bxc(self,_):
        pass

    # The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. (If a program outputs multiple values, they are separated by commas.)
    def out(self, combo):
        pass

    # The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register. (The numerator is still read from the A register.)
    def bdv(self, combo):
        pass

    # the cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register. (The numerator is still read from the A register.)"""
    def cdv(self, combo):
        pass

    def __repr__(self):
        ret = f'Register A: {self._register_a}\n'
        ret += f'Register B: {self._register_b}\n'
        ret += f'Register C: {self._register_c}\n\n'
        ret += ','.join(self._instructions)
        return ret

def part1(parsed):
    print(parsed)
    output = parsed.run()
    return output

def part2(parsed):
    return 0

def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

def run(path):
    print(f'{path}')
    puzzle_input = pathlib.Path(path).read_text().strip()

    solutions = solve(puzzle_input)
    print('\n'.join(str(solution) for solution in solutions))

if __name__ == "__main__":
    for path in RUN:
        run(path)
    for path in sys.argv[1:]:
        run(path)