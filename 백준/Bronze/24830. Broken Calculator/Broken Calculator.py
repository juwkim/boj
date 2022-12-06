pre = 1
for _ in range(int(input())):
    a, op, b = input().split()
    a, b = map(int, [a, b])
    if op == '+':
        res = a + b - pre
    elif op == '-':
        res = (a - b) * pre
    elif op == '*':
        res = (a * b) ** 2
    else:
        res = a // 2 + a % 2
    pre = res
    print(res)