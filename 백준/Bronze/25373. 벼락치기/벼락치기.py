N = int(input())
if N == 1:
    ans = 1
elif N <= 3:
    ans = 2
elif N <= 6:
    ans = 3
elif N <= 10:
    ans = 4
elif N <= 15:
    ans = 5
elif N <= 21:
    ans = 6
else:
    r, q = divmod(N - 21, 7)
    if q:
        ans = r + 7
    else:
        ans = r + 6
print(ans)