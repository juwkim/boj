g = lambda: map(int, input().split())
xs, ys = g()
xt, yt = g()
xp, yp = g()
ans = []
if xs < xp:
    P = 10001
    ans.append((-P, ys))
    if xt < xp:
        ans.append((-P, yt))
    else:
        ans.append((-P, P))
        ans.append((P, P))
        ans.append((P, yt))
else:
    P = 10001
    ans.append((P, ys))
    if xt > xp:
        ans.append((P, yt))
    else:
        ans.append((P, P))
        ans.append((-P, P))
        ans.append((-P, yt))
print(len(ans))
for x, y in ans:
    print(x, y)