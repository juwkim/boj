X = int(input())
ans = 1

while(True):
    if X <= 0:
        break
    X -= ans
    ans += 1

X += ans - 1
if ans % 2:
    print("%d/%d" % (X, ans - X))
else:
    print("%d/%d" % (ans - X, X))