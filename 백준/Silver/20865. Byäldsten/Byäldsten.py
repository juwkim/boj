import sys
input = sys.stdin.readline

n = int(input())
ans, died = [0] * n, 0
for f, d, i in sorted([*map(int, input().split())] + [i] for i in range(n)):
    ans[i] = max(0, d - max(f, died))
    died = max(died, d)
print(*ans)