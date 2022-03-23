import sys
from collections import deque
from math import sqrt

def isPrime(N):
    visited = [True for _ in range(N+1)]

    for i in range(2, int(sqrt(N))+1):
        if visited[i] == True:
            
            for j in range(i+i, N, i):
                visited[j] = False

    return [i for i in range(2, N) if visited[i] == True]
    

def two_pointer():
    result = 0
    tmp = deque([prime_list[0]]) # 초깃값
    
    if N < 5:
        if N == 2 or N == 3:
            return 1
        
        else:
            return 0
    
    else:
        if N in prime_list:
            result += 1
    
        start, end = 0, 1
    
        while True:
            if sum(tmp) == N:
                result += 1
    
            if sum(tmp) < N:
                tmp.append(prime_list[end])
                end += 1
                
            if sum(tmp) > N:
                tmp.popleft()
                start += 1


N = int(sys.stdin.readline())
prime_list = print(isPrime(N))