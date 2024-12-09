from collections import namedtuple
import pathlib
import sys

SAMPLE_ANSWER_1 = 1928
SAMPLE_ANSWER_2 = None

DiskRecord = namedtuple('DiskRecord',['name','size'])

def parse(puzzle_input):
    # parse the input
    file_system_str = []

    for i in range(0, len(puzzle_input)//2):
        file_name = i
        free = int(puzzle_input[i*2+1])
        file = int(puzzle_input[i*2])
        for b in range(0, file):
            file_system_str.append(file_name)
        for b in range(0, free):
            file_system_str.append(None)
    file = int(puzzle_input[-1])
    for b in range(0,file):
        file_system_str.append(len(puzzle_input)//2)
        
    file_system_disk = []

    for i in range(0, len(puzzle_input)//2):
        file_name = i
        file_size = int(puzzle_input[i*2])
        free_size = int(puzzle_input[i*2+1])
        file_system_disk.append(DiskRecord(file_name,file_size))
        file_system_disk.append(DiskRecord(None,file_size))
    file_size = int(puzzle_input[-1])
    file_system_disk.append(DiskRecord(len(puzzle_input)//2,file_size))
    return file_system_str,file_system_disk

def frag(file_system):
    while None in file_system:
        temp = file_system.pop()
        if temp == None:
            continue
        # get index of earliest None
        i = file_system.index(None)
        # remove that None
        # insert temp
        file_system[i] = temp

def checksum(file_system):
    ret = 0
    for i in range(0, len(file_system)):
        ret += i * file_system[i]
    return ret

def defrag(file_system):
    print('defrag')
    # largest filename to smallest file name
    last_file = file_system[-1].name
    # cycle file names from last to first
    for file_name in range(last_file,-1,-1):
        print([(idx,(dr.name,dr.size)) for idx,dr in enumerate(file_system)])
        print(f'file: {file_name}')
        # get matching DiskRecord
        idx, file_size = find_file_index(file_system, file_name)
        free_spans = find_free_space(file_system)
        # idx at span[0]
        # size at span[1]
        for span in free_spans:
            if span[1] >= file_size:
                print(f'putting {file_name}({file_size}) in {span[1]} sized space at {span[0]}')
                # put the file, remove original free space
                file_system[span[0]] = DiskRecord(file_name,file_size)
                # put any remaining free space
                if span[1] > file_size:
                    file_system.insert(span[0]+1, DiskRecord(None, span[1]-file_size))
                # remove the file
                file_system[idx] = DiskRecord(None,file_size)
                break

def find_file_index(file_system, file_name):
    return [(idx,dr.size) for idx, dr in enumerate(file_system) if dr.name == file_name][0]
    i = 0
    while i < len(file_system):
        if file_system[i] == file_name:
            j = i
            while file_name[i] == file_name:
                i += 1
            # inclusive, exclusive range
            return (j, i)

def find_free_space(file_system):
    return [(idx,dr.size) for idx, dr in enumerate(file_system) if dr.name == None]
    ret = []
    # loop on DRs
    for i in range(0,len(file_system)):
        # if DR.name == None
        if file_system[i].name == None:
            # record the index
            ret.append((i))
    return ret

def part1(parsed):
    parsed, _ = parsed
    # print(parsed)
    frag(parsed)
    return checksum(parsed)

def part2(parsed):
    _, parsed = parsed
    defrag(parsed)

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