import sys
input = lambda: sys.stdin.readline().rstrip()

N, S = input().split()
ans = 0
for _ in range(int(N)):
    name, cnt = input().split()
    if S in name.split('_'):
        ans += int(cnt)
print(ans)