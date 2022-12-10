def to_min(st):
    h, m = map(int, st.split(':'))
    time = h * 60 + m
    return time

N = int(input())
a, b = input().split()
if '+' in b:
    time = to_min(a) - 60 * float(b[b.index('+') + 1:])
else:
    time = to_min(a) + 60 * float(b[b.index('-') + 1:])
for _ in range(N):
    s = input()
    if '+' in s:
        off = 60 * float(s[s.index('+') + 1:])
    else:
        off = - 60 * float(s[s.index('-') + 1:])
    print("%02d:%02d" % divmod((time + off) % 1440, 60))