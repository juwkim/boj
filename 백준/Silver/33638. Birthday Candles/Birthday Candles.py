import sys
g = lambda: map(int, sys.stdin.readline().split())

N, H, C = g()
ans = 0
for l in map(sorted, zip(*[sorted(g()) for _ in range(N)])):
    for num in l:
        if num > C:
            break
        ans += 1
        C -= num
    else:
        continue
    break
print(ans)