# 0,1
A = 15
# 5,4
B = 22
# 6,3
BP = 22
#4,11
C = 24
# 13,6
CP = 12
# 13,14
D = 18
# 14,13
DP = 10
# 3,12
CD = 30
# 14,5
CDP = 38
# 12,21
E = 10
# 19,14
EP = 10
# 20,19
F = 5

PATHS = [[A,B,C,D,E,F],
         [A,B,CD,E,F],
         [A,B,C,DP,EP,F],
         [A,BP,CP,D,E,F],
         [A,BP,CP,DP,EP,F],
         [A,BP,CDP,EP,F]]

def main():
    print(f'a-b-c-d-e-f{sum([A,B,C,D,E,F])}')
    print(f'a-b-CD-e-f{sum([A,B,CD,E,F])}')
    print(f'a-b-c-D-E-f{sum([A,B,C,DP,EP,F])}')
    print(f'a-B-C-d-e-f{sum([A,BP,CP,D,E,F])}')
    print(f'a-B-C-D-E-f{sum([A,BP,CP,DP,EP,F])}')
    print(f'a-B-CD-E-f{sum([A,BP,CDP,EP,F])}')

if __name__ == "__main__":
    main()