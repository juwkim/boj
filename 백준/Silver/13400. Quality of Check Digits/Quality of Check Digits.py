from itertools import product

arr = [[*map(int, input().split())] for _ in range(10)]
ans = 0
for a, b, c, d in product(range(10), repeat=4):
    e = 0
    for p in (a, b, c, d):
        e = arr[e][p]
    def solve():
        l = a, b, c, d, e
        for i in range(4):
            if l[i] == l[i + 1]:
                continue
            p = [a, b, c, d, e]
            p[i], p[i + 1] = p[i + 1], p[i]
            x = 0
            for q in p:
                x = arr[x][q]
            if x == 0:
                return True
        for i in range(10):
            for j in range(5):
                p = [a, b, c, d, e]
                if p[j] == i:
                    continue
                p[j] = i
                x = 0
                for q in p:
                    x = arr[x][q]
                if x == 0:
                    return True
        return False
    ans += solve()
print(ans)