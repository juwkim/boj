N, d, ap1, ap2 = map(int, input().split())
d1, d2, same, intersect = 0, 0, 1, 0
v1, v2 = bytearray(N), bytearray(N)
v1[0], v2[0] = 1, 1
p1, p2 = 0, 0
for _ in range(N - 1):
    move1 = ap1 + 1
    while v1[(p1 + move1) % N]:
        move1 += 1
    d1 += move1
    intersect += any(p2 == (p1 + i) % N for i in range(1, move1))
    p1 = (p1 + move1) % N
    v1[p1] = 1
    if p1 == p2:
        same += 1
    
    move2 = ap2 + 1
    while v2[(p2 - move2) % N]:
        move2 += 1
    d2 += move2
    intersect += any(p1 == (p2 - i) % N for i in range(1, move2))
    p2 = (p2 - move2) % N
    v2[p2] = 1
    if p1 == p2:
        same += 1
print(d1 * d, d2 * d, same, intersect)