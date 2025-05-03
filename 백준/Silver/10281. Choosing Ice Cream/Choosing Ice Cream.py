import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

def solve_case(n, k):
    if k == 1:
        return 1 if n == 1 else "unbounded"
    if n == 1:
        return 0
    
    max_iter = 1000
    prod = 1
    for i in range(1, max_iter + 1):
        prod = (prod * k) % n
        if prod == 0:
            return i
    return "unbounded"

T = int(input())
for _ in range(T):
    n, k = g()
    print(solve_case(n, k))
