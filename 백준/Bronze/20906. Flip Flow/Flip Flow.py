t, s, n = map(int, input().split())
flips = [*map(int, input().split())] + [t]
top, bottom = 0, s

for a,b in zip(flips, flips[1:]):
    top, bottom = max(bottom + a - b, 0), min(top + b - a, s)
print(top) 