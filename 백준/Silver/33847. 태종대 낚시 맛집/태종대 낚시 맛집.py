import sys
input = sys.stdin.readline

n, c = int(input()), int(input())
fish = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: -x[1])
ans = 0
for t in range(10001):
    profit, left = -c * t, t
    for x, _, w in fish:
        if x <= left:
            left -= x
            profit += w
    ans = max(ans, profit)
print(ans)