import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    
    if S == E:
        print(1)
        continue
        
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
    print(dp) 