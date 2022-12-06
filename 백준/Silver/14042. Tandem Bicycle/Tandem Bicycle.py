g = lambda: [*map(int, input().split())]

t = int(input())
N = int(input())
Dmojistan = sorted(g())
Pegland = g()
if t == 1:
    Pegland.sort()
else:
    Pegland.sort(reverse=True)
ans = sum(max(a, b) for a, b in zip(Dmojistan, Pegland))
print(ans)