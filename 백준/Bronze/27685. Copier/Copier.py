import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    input()
    n = int(input())
    ans, check = [], set()
    for num in g():
        if num not in check:
            check.add(num)
            ans.append(num)
    print(*ans)