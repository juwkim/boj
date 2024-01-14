import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
p = g()
problems = [[] for _ in range(5)]
for _ in range(N):
    k, t = g()
    problems[k - 1].append(t)
ans = 0
for i in range(5):
    problems[i] = sorted(problems[i])[:p[i]]
    ans += sum(problems[i])
    ans += sum(abs(a - b) for a, b in zip(problems[i], problems[i][1:]))
ans += 60 * (sum(i != 0 for i in p) - 1)
print(ans)