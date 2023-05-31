s = input()
idx = 1
while s[idx] in '0123456789':
    idx += 1

a = int(s[:idx], 8)
b = int(s[idx + 1: ], 8)
op = s[idx]
if op == '/' and b == 0:
    print('invalid')
else:
    if op == '/':
        op = '//'
    n = eval(f'{a}{op}{b}')
    ans = ''
    sign = ''
    if n < 0:
        n = -n
        sign = '-'
    
    while True:
        n, q = divmod(n, 8)
        ans = str(q) + ans
        if n == 0:
            break
    
    print(sign + str(ans))