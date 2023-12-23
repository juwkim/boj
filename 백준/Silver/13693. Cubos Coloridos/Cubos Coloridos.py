import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

def rotate(p, q):
    for i in range(4):
        if all(p[j] == q[(i + j) % 4] for j in range(4)):
            return True
    return False

def is_same(a, b):
    aa = a[1:5]
    if (a[0], a[5]) == (b[0], b[5]):
        if rotate(aa, b[1:5]):
            return True
    if (a[0], a[5]) == (b[5], b[0]):
        if rotate(aa, b[4:0:-1]):
            return True
    if (a[0], a[5]) == (b[1], b[3]):
        if rotate(aa, [b[2], b[0], b[4], b[5]]):
            return True
    if (a[0], a[5]) == (b[3], b[1]):
        if rotate(aa, [b[5], b[4], b[0], b[2]]):
            return True
    if (a[0], a[5]) == (b[2], b[4]):
        if rotate(aa, [b[0], b[1], b[5], b[3]]):
            return True
    if (a[0], a[5]) == (b[4], b[2]):
        if rotate(aa, [b[3], b[5], b[1], b[0]]):
            return True
    return False

while N:= int(input()):
    cubes = []
    for _ in range(N):
        cubes.append(g() + g() + g())
    check = bytearray(N)
    for i in range(N - 1):
        if check[i]:
            continue
        for j in range(i + 1, N):
            if check[j]:
                continue
            if is_same(cubes[i], cubes[j]):
                check[j] = True
    ans = N - sum(check)
    print(ans)