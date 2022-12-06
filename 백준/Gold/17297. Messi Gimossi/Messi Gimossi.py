from bisect import bisect_left
res = [5, 13]
while res[-1] < 2**31:
    res.append(res[-1] + res[-2] + 1)
M = int(input())
idx = bisect_left(res, M)
flag = False
while idx > 1:
    if M == res[idx-1] + 1:
        flag = True
        break
    elif M > res[idx-1] + 1:
        M -= res[idx-1] + 1
        idx -= 2
    else:
        idx -= 1
if flag or M == 6:
    print('Messi Messi Gimossi')
else:
    print('Messi Gimossi'[M - 1])