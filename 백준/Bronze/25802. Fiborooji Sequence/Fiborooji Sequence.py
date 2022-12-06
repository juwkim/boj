g = lambda: [*map(int, input().split())]

a, b = g()
s, t = a, b
cnt = 2
while True:
    cnt += 1
    s, t = t, (s + t) % 10
    if (s, t) == (a, b):
        break
print(cnt)