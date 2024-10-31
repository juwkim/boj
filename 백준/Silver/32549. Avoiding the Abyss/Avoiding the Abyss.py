xs, ys = map(int, input().split())
xt, yt = map(int, input().split())
xp, yp = map(int, input().split())
ans = []
if xs < xp:
    ans.append((-10001, ys))
    if xt < xp:
        ans.append((-10001, yt))
    else:
        ans.append((-10001, 10001))
        ans.append((10001, 10001))
        ans.append((10001, yt))
else:
    ans.append((10001, ys))
    if xt > xp:
        ans.append((10001, yt))
    else:
        ans.append((10001, -10001))
        ans.append((-10001, -10001))
        ans.append((-10001, yt))
print(len(ans))
for x, y in ans:
    print(x, y)