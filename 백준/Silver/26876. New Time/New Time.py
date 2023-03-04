h1, m1 = map(int, input().split(':'))
h2, m2 = map(int, input().split(':'))

if m2 >= m1:
    ans = m2 - m1
else:
    ans = 60 + m2 - m1
    h1 += 1

ans += (h2 - h1) % 24
print(ans)