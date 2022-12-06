N = int(input())
ans = 0
flag = 0
for A, B in zip(input(), input()):
    if flag:
        flag ^= A == B
    elif A != B:
        flag = 1
        ans += flag
ans += flag
print(ans)