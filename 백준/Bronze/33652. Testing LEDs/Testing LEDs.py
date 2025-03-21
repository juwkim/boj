import sys
input = sys.stdin.readline

ans = float('inf')
for _ in range(int(input())):
    M, O = map(int, input().split())
    if O == 0 and M < ans:
        ans = M
if ans == float('inf'):
    ans = -1
print(ans)