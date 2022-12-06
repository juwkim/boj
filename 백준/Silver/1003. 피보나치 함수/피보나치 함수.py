import math

def fibo(n):
    a = (1 + math.sqrt(5)) / 2
    b = (1 - math.sqrt(5)) / 2
    return int((pow(a, n) - pow(b, n)) / math.sqrt(5))

T = int(input())

for _ in range(T):
    N = int(input())
    
    if N == 0:
        print(1, 0)
    else:
        print(fibo(N-1), fibo(N))