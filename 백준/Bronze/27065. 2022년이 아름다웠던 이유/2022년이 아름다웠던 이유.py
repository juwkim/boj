input = __import__('sys').stdin.readline
from math import isqrt

def get_divisor(n):
    divisor = []
    for i in range(1, isqrt(n) + 1):
        q, r = divmod(n, i)
        if r:
            continue
        divisor.append(q)
        if i != q:
            divisor.append(i)
    return divisor
            

for _ in range(int(input())):
    n = int(input())
    divisor = get_divisor(n)
    divisor.remove(n)
    if sum(divisor) > n and all(sum(get_divisor(num)) <= 2 * num for num in divisor):
        ans = 'Good Bye'
    else:
        ans = 'BOJ 2022'
    print(ans)