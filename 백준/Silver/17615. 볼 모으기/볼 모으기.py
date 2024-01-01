import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
S = input()

def solve(c, l):
    i = 0
    while i < len(l) and l[i] == c:
        i += 1
    if i == len(l):
        return 0
    ans = 0
    while i < len(l):
        if l[i] == c:
            ans += 1
        i += 1
    return ans

ans = min(solve("R", S), solve("R", S[::-1]), solve("B", S), solve("B", S[::-1]))
print(ans)