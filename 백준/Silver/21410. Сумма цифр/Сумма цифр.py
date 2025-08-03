def digit_sum(x):
    return sum(map(int, str(x)))

A = int(s:=input())
best_sum = digit_sum(A)
best_B, best_C = 0, A
n = len(s)
for i in range(n):
    if s[i] == '0':
        continue
    B_digits = list(s)
    B_digits[i] = str(int(s[i]) - 1)
    for j in range(i + 1, n):
        B_digits[j] = '9'
    B_str = ''.join(B_digits).lstrip('0')
    B_val = int(B_str) if B_str else 0

    C_val = A - B_val
    cur_sum = digit_sum(B_val) + digit_sum(C_val)
    if cur_sum > best_sum:
        best_sum = cur_sum
        best_B, best_C = B_val, C_val
print(best_sum)
print(best_B, best_C)