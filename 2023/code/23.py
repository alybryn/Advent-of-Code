from collections import deque, namedtuple
from copy import deepcopy
import pathlib
from queue import PriorityQueue
import sys

SAMPLE_ANSWER_1 = 94
SAMPLE_ANSWER_2 = 154

NINF = -10**99

class PathSquare(namedtuple('PathSquare',['x','y'])):
    def __repr__(self):
        return f'({self.x},{self.y})'

    def neighbors(self,slope):
        switch = {'.':[(-1,0),(1,0),(0,-1),(0,1)],
                  '^':[(-1,0)],
                  'v':[(1,0)],
                  '>':[(0,1)],
                  '<':[(0,-1)]}
        matrix = switch[slope]
        return [PathSquare(self.x+m[0], self.y+m[1]) for m in matrix]
    
class Path(namedtuple('Path',['start', 'end', 'weight'])):
    # def __eq__(self, other):
    #     return self.start==other.start and self.end==other.end and self.weight == other.weight

    def __repr__(self) -> str:
        return f'({self.start} -> {self.end}: {self.weight} steps)'

def parse(puzzle_input):
    # parse the input
    lines =  puzzle_input.split()
    paths = {}
    start = lines[0]
    end = lines[-1]
    # lines = lines[1:-1]

    for y in range(len(lines[0])):
        if start[y] == '.':
            start_path = PathSquare(0,y)
            paths['start'] = start_path
            paths[start_path] = '.'
        if end[y] == '.':
             end_path = PathSquare(len(lines)-1,y)
             paths['end'] = end_path
             paths[end_path] = '.'
        for x in range(1,len(lines)-1):
            if lines[x][y] == '#':
                continue
            paths[PathSquare(x,y)] = lines[x][y]
    
    return paths

def exits(paths, center):
    ret = []
    checks = [(-1,0,'^'),(1,0,'v'),(0,-1,'<'),(0,1,'>')]
    for c in checks:
        new = PathSquare(center.x+c[0],center.y+c[1])
        if paths.get(new,'#') == c[2]:
            ret.append(new)
    return ret

# start should be '.'
def garden_path(paths,start,u):
    frontier = deque()
    frontier.append(start)
    reached = set()
    reached.add(start)
    while frontier:
        current = frontier.popleft()
        for next in current.neighbors(paths[current]):
            if next in paths:
                if next not in reached:
                    if paths[next] != '.':
                        if len(reached) != 1:
                            return Path(u,next.neighbors(paths[next])[0],len(reached)+1)
                            return Path(start, next, len(reached)+1)
                    if paths[next] == '.':
                        frontier.append(next)
                        reached.add(next)
    return Path(u,paths['end'],len(reached)-1)

def weigh(pathsquares):
    start = garden_path(pathsquares,pathsquares['start'],pathsquares['start'])
    frontier = deque()
    frontier.append(start)
    graph = {}
    graph['start'] = start
    while frontier:
        current = frontier.popleft()
        # print(f'current: {current}')
        for next in exits(pathsquares,current.end):
            next_node = garden_path(pathsquares, next,current.end)
            next_node = Path(next_node.start,next_node.end,next_node.weight+1)
            # print(next_node)
            frontier.append(next_node)
            goes_to = graph.get(current,set())
            goes_to.add(next_node)
            graph.update({current:goes_to})
            # dict_print(graph)

    return graph

def in_degree(k, graph):
    i = 0
    for v in graph.values():
        if k in v:
            i += 1
    return i

def topological_sort(graph):
    graph = deepcopy(graph)
    del graph['start']
    # print(graph)
    S = []
    incounter = {}
    # for all u in G.vertices():
    for k in graph.keys():
        #Let incounter(u) be the in-degree of u
        incounter[k] = in_degree(k,graph)
        # if incounter(u) == 0:
        if incounter[k] == 0:
            # S.push(u)
            S.append(k)
    ret = []
    while S:
        u = S.pop()
        # let u be vertex number i in topological ordering
        ret.append(u)

        # for all outgoing edge(u,w) of u:
        for w in graph[u]:
            # incounter(w) -= 1
            incounter[w] = incounter.get(w,0) - 1
            # if incounter(w) == 0:
            if incounter[w] == 0:
                # S.push(w)
                S.append(w)
    # ret.extend(graph[ret[-1]])
    return ret

def critical_path(topo,graph,s):
    # dist[] = {NINF,NINF,....}
    dist = {}#[-10**9 for i in range(len(topo))]
    # -10**9
    # dist[s] = 0
    dist[s] = s.weight
    # for vertex u in topo order:
    for u in topo:
        # for adjacent vertex v of u
        for v in graph[u]:
            #if dist[v] < dist[u] + weight(u,v):
            if dist.get(v,NINF) < dist[u] + v.weight:
                # dist[v] = dist[u] + weight(u,v)
                dist[v] = dist[u] + v.weight
    print(dist)
    return dist

def extract(dist):
    return max(dist.values())

def dict_print(dictionary):
    for k in dictionary.keys():
        print(f'{k}:{dictionary[k]}')

def part1(parsed):
    weighted_graph = weigh(parsed)
    dict_print(weighted_graph)
    topo = topological_sort(weighted_graph)
    critical_paths = critical_path(topo,weighted_graph,weighted_graph['start'])
    print(critical_paths)
    weighed_end = extract(critical_paths)
    return weighed_end

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
