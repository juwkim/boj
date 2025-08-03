def digit_sum(x):
    return sum(map(int, str(x)))

A = int(s:=input())
n = len(s)
ans = digit_sum(A), A, 0
for i in range(n):
    if s[i] == '0':
        continue
    B_digits = list(s)
    B_digits[i] = str(int(s[i]) - 1)
    for j in range(i + 1, n):
        B_digits[j] = '9'
    B_val = int(''.join(B_digits))
    C_val = A - B_val
    ans = max(ans, (digit_sum(B_val) + digit_sum(C_val), B_val, C_val))
print(ans[0])
print(*ans[1:])