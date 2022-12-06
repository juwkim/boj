g = lambda: [*map(int, input().split())]

V, W, D = g()
cnt, t = 0, W / V

while True:
    D -= 5 * t * t
    if D < 0:
        break
    cnt += 1
    t *= 1.25
print(cnt)