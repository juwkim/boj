import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    input()
    n = int(input())
    s = input()
    p = input()
    cnt = n - sum(c in p for c in s)
    ans = pow(2, cnt, 10**9 + 7) + 1
    print(ans)