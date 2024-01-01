import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
if N == 0:
    print("NO")
    exit()
cur = 1
while True:
    if cur * 3 <= N:
        cur *= 3
    else:
        break
while cur:
    if N >= cur:
        N -= cur
    cur //= 3
if N == 0:
    ans = "YES"
else:
    ans = "NO"
print(ans)