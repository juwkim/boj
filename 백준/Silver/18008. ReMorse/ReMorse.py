from collections import Counter

cnt = Counter(l:=[c for c in input().lower() if c.isalpha()])
a = 1, 3, 3, 5, 5, 5, 7, 7, 7, 7, 7, 9, 9, 9, 9, 9, 9, 9, 9, 11, 11, 11, 11, 11, 11, 11
ans = 3 * (len(l) - 1) + sum(c * v for c, v in zip(a, sorted(cnt.values(), reverse=True)))
print(ans)