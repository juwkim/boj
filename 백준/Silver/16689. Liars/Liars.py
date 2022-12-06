g = lambda: [*map(int, input().split())]

N = int(input())
buf = [g() for _ in range(N)]

ans = -1
for i in range(N, -1, -1):
    if sum(a <= i <= b for a, b in buf) == i:
        ans = i
        break
print(ans)