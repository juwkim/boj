def solve(e):
    m = 1e6
    p = 1
    while p**3 <= e:
        p += 1
    p -= 1
    for z in range(p, -1, -1):
        y = int((e - z**3)**.5)
        x = e - y ** 2 - z ** 3
        m = min(m, x + y + z)
    return m

while (e:=int(input())):
    m = solve(e)
    print(m)