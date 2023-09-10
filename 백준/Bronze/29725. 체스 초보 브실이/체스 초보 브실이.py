s = {a: b for a, b in zip(".KPNBRQkpnbrq", (0, 0, 1, 3, 3, 5, 9, 0, -1, -3, -3, -5, -9))}
print(sum(sum(s[c] for c in input()) for _ in range(8)))