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

            for cmd in '+-*/':
                match cmd:
                    case '+': c = a + b
                    case '*': c = a * b
                    case '-':
                        c = a - b
                        if c <= 0: continue
                    case '/':
                        c, r = divmod(a, b)
                        if r: continue
                q = tuple(sorted(p + [c]))
                if q not in check:
                    check.add(q)
                    res.append((a, cmd, b, c))
                    if solve(q): return True
                    res.pop()
    return False

if solve(X):
    print(len(res))
    for a, cmd, b, c in res:
        print(f"{a} {cmd} {b} = {c}")
else:
    print(-1)