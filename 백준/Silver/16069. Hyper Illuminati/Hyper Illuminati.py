def solve():
    m = int(input())
    for p in range(2, 61):
        s, total = 0, 0
        while total < m:
            s += 1
            total += s ** p
        if total == m:
            print(p + 1, s)
            return
    print("impossible")
solve()