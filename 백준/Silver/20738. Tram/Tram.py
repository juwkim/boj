import sys
input = sys.stdin.readline

N = int(input())
ans = 0
for _ in range(N):
    x, y = map(int, input().split())
    ans += y - x
print(ans / N)