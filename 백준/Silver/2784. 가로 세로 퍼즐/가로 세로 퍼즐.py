def solve():
    l = [input() for _ in range(6)]
    for i in range(6):
        for j in range(6):
            if i == j:
                continue
            for k in range(6):
                if k in (i, j):
                    continue
                t = sorted(l[m] for m in range(6) if m not in (i, j, k))
                if t == sorted(l[i][m] + l[j][m] + l[k][m] for m in range(3)):
                    return f"{l[i]}\n{l[j]}\n{l[k]}"
    return 0
print(solve())