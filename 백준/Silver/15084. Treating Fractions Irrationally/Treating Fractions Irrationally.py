import decimal
decimal.getcontext().prec = 500
n, d = map(int, input().split())
num = str(decimal.Decimal(n) / d) + '0' * 500
idx = 2
ans = None
while idx < 400:
    if num[idx] == '0':
        ans = num[:idx]
        break
    if num[idx] == '9':
        if idx == 2:
            ans = 1
        else:
            ans = num[:idx-1] + str(int(num[idx-1]) + 1)
        break
    idx += 1
if ans:
    if ans == '0.':
        print(0)
    else:
        print(ans)
else:
    print('throw out')