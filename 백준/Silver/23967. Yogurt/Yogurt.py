import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for tc in range(1, 1 + int(input())):
    n, k = g()
    ans = 0
    for num in sorted(g()):
        day = ans // k
        if day < num:
            ans += 1
    print(f"Case #{tc}: {ans}")