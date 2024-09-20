import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

mod = 1000000009
mem = {i: 0 for i in range(-6, 0)}
mem[0] = 1

def f(num):
    if num not in mem:
        mem[num] = (f(num - 2) + 2 * f(num - 3) + 3 * f(num - 4) + 2 * f(num - 5) + f(num - 6)) % mod
    return mem[num]

for _ in range(int(input())):
    n = int(input())
    print((f(n - 1) + f(n - 2) + f(n - 3)) % mod, f(n))