def operation(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return abs(a) // abs(b) * (-1)**(a < 0 or b < 0)

K1, O1, K2, O2, K3 = input().split()
K1, K2, K3 = map(int, [K1, K2, K3])
ans1 = operation(operation(K1, K2, O1), K3, O2)
ans2 = operation(K1, operation(K2, K3, O2), O1)
print(min(ans1, ans2), max(ans1, ans2), sep='\n')