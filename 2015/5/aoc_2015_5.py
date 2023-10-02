import pathlib
import sys

SAMPLE_ANSWER_1 = None
SAMPLE_ANSWER_2 = None

def parse(puzzle_input):
    # parse the input
    return [line for line in puzzle_input.split()]

def denegrate(word):
    print(f"{word} is naughty")
    return

def praise(word):
    print(f"{word} is nice")
    return

def is_nice_1(word):
    # does not contain 'ab' 'cd' 'pq' or 'xy'
    if 'ab' in word:
        #denegrate(word)
        return False
    if 'cd' in word:
        #denegrate(word)
        return False
    if 'pq' in word:
        #denegrate(word)
        return False
    if 'xy' in word:
        #denegrate(word)
        return False
    # at least 3 vowels
    vowels = [1 for c in word if c in ['a', 'e', 'i', 'o', 'u']]
    if sum(vowels) < 3:
        #denegrate(word)
        return False
    # at least one letter twice in a row
    previous = word[0]
    for char in word[1:]:
        if previous == char:
            #praise(word)
            return True
        previous = char
    return False
    
def part1(parsed):
    nice_words = 0
    for line in parsed:
        if is_nice_1(line):
            nice_words += 1
    return nice_words

def is_nice_2(word):
    if len(word) < 4:
        return False
    condition1 = False
    condition2 = False
    #contains a pair of any 2 letters that appear at least twice without overlapping
    letter1 = word[0]
    letter2 = word[1]
    # TODO: ANOTHER FOR LOOP, JEEVES!
    for i in range(2, len(word)):
        if word[i] == letter1 and word[i+1] == letter2:
            condition1 = True
            break
    #contains at least 1 letter which repeats with exactly 1 letter between them
    return condition1 and condition2

def part2(parsed):
    nice_words = 0
    for line in parsed:
        if is_nice_2(line):
            nice_words += 1

    return nice_words

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