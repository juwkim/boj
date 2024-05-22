import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

for tc in range(1, 1 + int(input())):
    N, D = g()
    ans = D
    for X in [*g()][::-1]: ans -= ans % X
    print(f"Case #{tc}: {ans}")