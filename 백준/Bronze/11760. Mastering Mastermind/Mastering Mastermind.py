from collections import Counter as c
_, maker, breaker = input().split()
r = sum(x == y for x, y in zip(maker, breaker))
s = sum((c(maker)&c(breaker)).values())
print(r, s - r)