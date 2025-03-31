T = int(input())
X = [*map(int, input().split())]
res = []
check = set()
def solve(l):
    if T in l: return True
    for i in range(len(l)):
        a = l[i]
        for j in range(len(l)):
            if i == j: continue
            b = l[j]
            p = [l[k] for k in range(len(l)) if k not in (i, j)]

            q = tuple(sorted(p + [a + b]))
            if q not in check:
                check.add(q)
                res.append((a, '+', b, a + b))
                if solve(q): return True
                res.pop()
            
            if a > b:
                q = tuple(sorted(p + [a - b]))
                if q not in check:
                    check.add(q)
                    res.append((a, '-', b, a - b))
                    if solve(q): return True
                    res.pop()
            
            q = tuple(sorted(p + [a * b]))
            if q not in check:
                check.add(q)
                res.append((a, '*', b, a * b))
                if solve(q): return True
                res.pop()
            
            if a % b == 0:
                q = tuple(sorted(p + [a // b]))
                if q not in check:
                    check.add(q)
                    res.append((a, '/', b, a // b))
                    if solve(q): return True
                    res.pop()
    return False

if solve(X):
    print(len(res))
    for a, cmd, b, c in res:
        print(f"{a} {cmd} {b} = {c}")
else:
    print(-1)