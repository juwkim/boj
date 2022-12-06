g = lambda: [*map(int, input().split())]


A, B, C, D = g()
ans = None
X = (C + B - 1) // B
for b in range(X, X+A):
    a, q = divmod(D + b * B, A)
    if q == 0:
        ans = a, b
        break
   
if ans:
    a, b = ans
    msg = f'We need {ans[0]} truck'
    if a != 1: msg += 's'
    msg += f' and {ans[1]} boat'
    if b != 1: msg += 's'
    print(msg, end='.')
else:
    print('No solution.')