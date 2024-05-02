input()
N = int(input())
s = [input().split(', ') for _ in range(N)]
t = min(l:=[max(sum(a != b for a, b in zip(x, y)) for y in s) for x in s])
for i in range(N):
    if l[i] == t:
        print(*s[i], sep=', ')