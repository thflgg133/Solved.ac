import sys

def Recursive_Power(num,n):
    if n == 1:
        return num % C
    
    if n % 2 == 0:
        y = Recursive_Power(num, n//2)
        return y * y % C
    
    else:
        y= Recursive_Power(num, (n-1)//2)
        return y * y * num % C


A, B, C = map(int, sys.stdin.readline().split())
print(Recursive_Power(A,B))