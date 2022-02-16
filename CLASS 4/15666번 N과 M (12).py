import sys
from itertools import combinations_with_replacement

N, M = map(int, sys.stdin.readline().split())
N_list = list(map(int, sys.stdin.readline().split()))
N_list.sort()

combi_w_list = sorted(set(list(combinations_with_replacement(N_list, M))))

for i in combi_w_list:
    print(*i)