N, P = map(int, input().split())
lo, hi = P, P
for _ in range(N):
    op1, num1, op2, num2 = input().split()
    if op1 == 'x': op1 = '*'
    if op2 == 'x': op2 = '*'
    l = eval(f"{lo}{op1}{num1}"), eval(f"{lo}{op2}{num2}"), eval(f"{hi}{op1}{num1}"), eval(f"{hi}{op2}{num2}")
    lo, hi = min(l), max(l)
print(hi)