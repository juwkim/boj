import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    if b >= n or a > b:
        print("IMPOSSIBLE")
    else:
        for i in range(2, a + 1):
            print(1, i)
        print(b - a + 1, *range(a + 1, b + 2))
        for _ in range(n - a):
            print(0)