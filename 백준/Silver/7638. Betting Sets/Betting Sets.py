import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

while (l:=g())[0]:
    n, m = l
    ans = 0
    for s in zip(*map(sorted, zip(*[map(float, input().split()) for _ in range(n)]))):
        cur = 1
        for p in s:
            cur *= p
        ans += cur
    print(f"{ans:.4f}")