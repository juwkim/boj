f = {k: v for k, v in zip(map(str, range(10)), input().split())}
rf = {v: k for k, v in f.items()}
fA, fB = input().split()
AB = str(int("".join(rf[c] for c in fA)) + int("".join(rf[c] for c in fB)))
fAB = [f[c] for c in AB]
print(*fAB, sep='')