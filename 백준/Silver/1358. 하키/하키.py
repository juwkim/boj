from math import dist
g = lambda: [*map(int, input().split())]

W, H, X, Y, P = g()
R = H >> 1    
one = (X, Y + R)
two = (X+W, Y + R)

cnt = 0
for _ in range(P):
    pos = g()
    if X <= pos[0] <= X + W and Y <= pos[1] <= Y + H:
        cnt += 1
    elif dist(pos, one) <= R:
        cnt += 1
    elif dist(pos, two) <= R:
        cnt += 1
print(cnt)