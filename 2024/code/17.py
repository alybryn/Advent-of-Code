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

DIAGNOSTIC = False

def parse(puzzle_input):
    # parse the input
    registers,instructions = puzzle_input.split('\n\nProgram: ')
    a,b,c = map(int,re.findall(r'\d+',registers))
    instructions = [int(i) for i in instructions.split(',')]
    return Computer(a,b,c,instructions)

class Computer:
    def __init__(self, a, b, c, instructions):
        self._register_a = a
        self._register_b = b
        self._register_c = c
        self._instructions = instructions
        self._ptr = 0
    
    def run(self):
        ret = []
        while self._ptr < len(self. _instructions):
            remember = self._ptr
            optional = self._operate(self._instructions[self._ptr],self._instructions[self._ptr+1])
            if self._ptr == remember:
                self._ptr += 2
            if optional != None:
                ret.append(optional)
        print(','.join(map(str,ret)))

    def diagostic(self, register, assertion):
        match register:
            case 'a':
                assert self._register_a == assertion
            case 'b':
                assert self._register_b == assertion
            case 'c':
                assert self._register_c == assertion

    def _operate(self, opcode, operand):
        return self._interpret_instruction(opcode)(operand)

    def _interpret_instruction(self, opcode):
        match opcode:
            case 0: return self._adv
            case 1: return self._bxl
            case 2: return self._bst
            case 3: return self._jnz
            case 4: return self._bxc
            case 5: return self._out
            case 6: return self._bdv
            case 7: return self._cdv
            case _: print(f'unknown opcode: {opcode}')

    def _interpret_combo(self, operand):
        match operand:
            case 0: return 0
            case 1: return 1
            case 2: return 2
            case 3: return 3
            case 4: return self._register_a
            case 5: return self._register_b
            case 6: return self._register_c
            case _: print(f'unknown combo operand: {operand}')

    # The adv instruction (opcode 0) performs division. The numerator is the value in the A register. The denominator is found by raising 2 to the power of the instruction's combo operand. (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) The result of the division operation is truncated to an integer and then written to the A register.
    def _adv(self, combo):
        # call dv
        # put return in register a
        self._register_a = self._dv(combo)

    # The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand, then stores the result in register B.
    def _bxl(self, literal):
        self._register_b = self._register_b ^ literal

    # The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to the B register.
    def _bst(self, combo):
        self._register_b = self._interpret_combo(combo)%8

    # The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero, it jumps by setting the instruction pointer to the value of its literal operand; if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
    def _jnz(self, literal):
        if self._register_a != 0:
            self._ptr = literal

    # The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B. (For legacy reasons, this instruction reads an operand but ignores it.)
    def _bxc(self,_):
        self._register_b = self._register_b ^ self._register_c

    # The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. (If a program outputs multiple values, they are separated by commas.)
    def _out(self, combo):
        return self._interpret_combo(combo)%8

    # The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register. (The numerator is still read from the A register.)
    def _bdv(self, combo):
        self._register_b = self._dv(combo)

    # the cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register. (The numerator is still read from the A register.)
    def _cdv(self, combo):
        self._register_c = self._dv(combo)

    # do all the division operations in one place
    def _dv(self, combo):
        return self._register_a // pow(2,self._interpret_combo(combo))

    def __repr__(self):
        ret = '---------------\n'
        ret += f'Register A: {self._register_a}\n'
        ret += f'Register B: {self._register_b}\n'
        ret += f'Register C: {self._register_c}\n\n'
        ret += ','.join(map(str,self._instructions))
        ret += '\n---------------'
        return ret

def run_diagnostic():
    if DIAGNOSTIC:
        diagnostic1()
        diagnostic2()
        diagnostic3()
        diagnostic4()
        diagnostic5()

def diagnostic1():
        # If register C contains 9, the program 2,6 would set register B to 1.
        comp = Computer(a=0,b=0,c=9,instructions=[2,6])
        comp.run()
        comp.diagostic('b',1)
        
def diagnostic2():
        # If register A contains 10, the program 5,0,5,1,5,4 would output 0,1,2.
        comp = Computer(a=10,b=0,c=0,instructions=[5,0,5,1,5,4])
        print('Expected output is\n0,1,2')
        comp.run()

def diagnostic3():
        # If register A contains 2024, the program 0,1,5,4,3,0 would output 4,2,5,6,7,7,7,7,3,1,0 and leave 0 in register A.
        comp = Computer(a=2024,b=0,c=0,instructions=[0,1,5,4,3,0])
        print('Expected output is\n4,2,5,6,7,7,7,7,3,1,0')
        comp.run()
        comp.diagostic('a',0)

def diagnostic4():
        # If register B contains 29, the program 1,7 would set register B to 26.
        comp = Computer(a=0,b=29,c=0,instructions=[1,7])
        comp.run()
        comp.diagostic('b',26)

def diagnostic5():
        # If register B contains 2024 and register C contains 43690, the program 4,0 would set register B to 44354.
        comp = Computer(a=0,b=2024,c=43690,instructions=[4,0])
        comp.run()
        comp.diagostic('b',44354)

def part1(parsed):
    print(parsed)
    run_diagnostic()
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