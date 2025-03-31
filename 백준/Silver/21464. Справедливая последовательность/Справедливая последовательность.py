n = len(s := input())
even, odd = s[::2].count('1'), s[1::2].count('1')
curr_even, curr_odd = 0, 0
ans = 0
for i in range(n):
    if s[i] == '1':
        if i & 1:
            a = curr_odd + even - curr_even
            b = curr_even + odd - curr_odd - 1
        else:
            a = curr_odd + even - curr_even - 1
            b = curr_even + odd - curr_odd
    else:
        a = curr_odd + even - curr_even
        b = curr_even + odd - curr_odd
    if a == b:
        ans = i + 1
        break

    if i & 1:
        curr_odd += s[i] == '1'
    else:
        curr_even += s[i] == '1'
print(ans)