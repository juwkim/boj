from math import pi
def g(): return [*map(int, input().split())]

t = int(input()) / (2 * pi)
ans = 0
nums = sorted(g()[::-1] for _ in range(int(input())))
for s, d in nums:
    if t > s * d:
        ans += d
        t -= s * d
    else:
        ans += t // s
        break
print(int(ans))