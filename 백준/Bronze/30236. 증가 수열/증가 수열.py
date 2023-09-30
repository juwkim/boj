import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    n = int(input())
    ans = 0
    for num in g():
        ans += 1
        if num == ans:
            ans += 1
    print(ans)