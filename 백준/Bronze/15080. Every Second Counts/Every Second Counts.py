h0, m0, s0 = map(int, input().split(':'))
h1, m1, s1 = map(int, input().split(':'))
time = (h1 - h0) * 3600 + (m1 - m0) * 60  + s1 - s0
print(time % 86400)