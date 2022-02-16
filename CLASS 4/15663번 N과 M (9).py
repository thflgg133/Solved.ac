import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
N_list = list(map(int, sys.stdin.readline().split()))

permu = sorted(set(list(permutations(N_list, M))))

for i in permu:
    print(*i)