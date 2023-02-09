ans = 1e9
a, b, c = map(int, input().split())
for op1 in ('+', '-', '*', '//'):
    if op1 == '//' and a % b:
        continue
    num = eval(f'{a}{op1}{b}')
    for op2 in ('+', '-', '*', '//'):
        if op2 == '//' and num % c:
            continue
        res = eval(f'{num}{op2}{c}')
        ans = ans if res < 0 else min(ans, res)
print(ans)