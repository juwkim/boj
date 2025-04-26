m = int(input())
x, l_sum = m + 1, m
n, r_sum = m + 2, m + 2
while l_sum != r_sum:
    if l_sum < r_sum:
        l_sum += x
        x += 1
        r_sum -= x
    else:
        n += 1
        r_sum += n
print(m, x, n)