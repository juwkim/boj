g = lambda: [*map(int, input().split())]

input()
h, a = g(), g()
tw, cw = sum(a), 0
for height, weight in sorted(zip(h, a)):
    cw += weight
    if cw * 2 >= tw:
        break
print(height, sum(abs(hi - height) * ai for hi, ai in zip(h, a)))