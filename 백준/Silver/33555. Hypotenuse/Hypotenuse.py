from collections import Counter

a, b, c = input().split()
if a == '?':
    num = int(c) ** 2 - int(b) ** 2
elif b == '?':
    num = int(c) ** 2 - int(a) ** 2
else:
    num = int(a) ** 2 + int(b) ** 2

cnt = Counter()
for i in range(2, int(num ** 0.5) + 1):
    while num % i == 0:
        cnt[i] += 1
        num //= i
if num > 1:
    cnt[num] += 1
s, t = 1, 1
for k, v in cnt.items():
    q, r = divmod(v, 2)
    for _ in range(q):
        s *= k
    if r:
        t *= k
if t == 1:
    print(s)
elif s == 1:
    print("\\sqrt{%d}" % t)
else:
    print("%d \\cdot \\sqrt{%d}" % (s, t))