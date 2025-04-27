import sys
import math
input = sys.stdin.readline

def is_prime(n):    
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def solve(s: str):
    i = s.find('.')
    if i == -1:
        return int(s), 1
    return int(s.replace('.', '')), 10 ** (len(s) - i - 1)

for _ in range(int(input())):
    (na, da), (nb, db) = map(solve, input().split())
    s, t = na * db, nb * da
    g = math.gcd(s, t)
    p, q = s // g, t // g
    if p == q:
        print(2, 2)
    elif is_prime(p) and is_prime(q):
        print(p, q)
    else:
        print("impossible")