s = input()
p, q, r = s.index('@'), s.index('#'), s.index('!')
if p < q < r or p > q > r:
    print(abs(p - r) - 1)
else:
    print(-1)