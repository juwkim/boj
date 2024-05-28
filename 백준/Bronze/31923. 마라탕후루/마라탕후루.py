g = lambda: map(int, input().split())
N, P, Q = g()
ans = "YES"
l = []
for a, b in zip(g(), g()):
    if a == b:
        l.append(0)
    elif (P - Q) * (a - b) >= 0:
        ans = "NO"
        break
    else:
        q, r = divmod(abs(a - b), abs(Q - P))
        if r or q > 10000:
            ans = "NO"
            break
        l.append(q)
print(ans)
if ans == "YES":
    print(*l)