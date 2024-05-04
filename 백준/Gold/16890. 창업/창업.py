a, b = input(), input()
q, r = divmod(N:=len(a), 2)
l = sorted(a, reverse=True)[-(q + r):], sorted(b)[-q:]
ans1 = []
turn = 0
while turn < N:
    if all(l) and l[0][-1] >= l[1][-1]:
        break
    ans1.append(l[turn&1].pop())
    turn += 1
l[0].reverse()
l[1].reverse()
ans2 = []
while turn < N:
    ans2.append(l[turn&1].pop())
    turn += 1
print(*ans1, *reversed(ans2), sep='')