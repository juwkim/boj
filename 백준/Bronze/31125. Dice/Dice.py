import sys
input = sys.stdin.readline

for _ in range(int(input())):
    S, n, f, m = map(int, input().split())
    if n <= S - m <= n * f:
        print("YES")
    else:
        print("NO")