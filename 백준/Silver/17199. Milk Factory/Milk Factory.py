import sys
input = sys.stdin.readline

N = int(input())
cnt = [0 for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    cnt[a - 1] += 1
print(cnt.index(0) + 1 if cnt.count(0) == 1 else -1)