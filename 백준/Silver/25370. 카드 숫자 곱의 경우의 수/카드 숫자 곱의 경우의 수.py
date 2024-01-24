import sys
input = lambda: sys.stdin.readline().rstrip()

ans = set()
N = int(input())
def solve(num, cnt):
    if cnt == N:
        ans.add(num)
        return
    for i in range(1, 10):
        solve(num * i, cnt + 1)
solve(1, 0)
print(len(ans))