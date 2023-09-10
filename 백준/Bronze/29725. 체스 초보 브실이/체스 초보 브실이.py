score = {a: b for a, b in zip(".KPNBRQ", (0, 0, 1, 3, 3, 5, 9))}
score.update(zip(".kpnbrq", (0, 0, -1, -3, -3, -5, -9)))

ans = 0
for _ in range(8):
    for c in input():
        ans += score[c]
print(ans)