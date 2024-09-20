import sys
input = lambda: sys.stdin.readline().rstrip()

R, C = map(int, input().split())
a = [input() for _ in range(R)]
def solve(ans):
    for l in a:
        for word in l.split('#'):
            if len(word) > 1:
                ans = min(ans, word)
    return ans
ans = solve('z' * 20)
a = [*map("".join, zip(*a))]
ans = solve(ans)
print(ans)