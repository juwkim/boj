g = lambda: [*map(int, input().split())]

W, H = g()
p, q = g()
t = int(input())

a = (p + t) % (2 * W)
b = (q + t) % (2 * H)
if a > W:
    a = 2 * W - a
if b > H:
    b = 2 * H - b
print(a, b)