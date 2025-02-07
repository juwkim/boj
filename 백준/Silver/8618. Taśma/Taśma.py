import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    def solve(l):
        i = n - 1
        while i and l[i] == l[0]:
            i -= 1
        return i
    ans = max(solve(a), solve(a[::-1]))
    if ans == 0:
        ans = "BRAK"
    print(ans)