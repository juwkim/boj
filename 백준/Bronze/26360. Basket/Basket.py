X = int(input())
if int(input()):
    ans = X + (int(input()) and int(input()))
else:
    ans = 0
    if int(input()):
        ans = sum(int(input()) for _ in range(X))
print(ans)