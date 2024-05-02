import sys
g = lambda: map(int, sys.stdin.readline().split())

x1, x2 = g()
N1, *T1 = g()
N2, *T2 = g()
l, r, t = 0, 0, 1
ans = "safe and sound"
while l < N1 or r < N2:
    x1 += l&1
    x2 += r&1
    if l < N1 and T1[l] == t: l += 1
    if r < N2 and T2[r] == t: r += 1
    if abs(x1 - x2) < 5:
        ans = f"bumper tap at time {t}"
        break
    t += 1
if ans == "safe and sound":
    if l&1 and r&1:
        pass
    elif x1 < x2 and l&1:
        t += x2 - x1 - 5
        ans = f"bumper tap at time {t}"
    elif x2 < x1 and r&1:
        t += x1 - x2 - 5
        ans = f"bumper tap at time {t}"
print(ans)