from itertools import permutations, product

a1, b1, a2, b2, a3, b3 = map(int, open(0))
ans = 1e9
for (s1, t1), (s2, t2), (s3, t3) in product(((a1, b1), (b1, a1)), ((a2, b2), (b2, a2)), ((a3, b3), (b3, a3))):
    ans = min(ans, (s1 + s2 + s3) * max(t1, t2, t3))

for (p1, q1), (p2, q2), (p3, q3) in permutations(((a1, b1), (a2, b2), (a3, b3))):
    for (s1, t1), (s2, t2), (s3, t3) in product(((p1, q1), (q1, p1)), ((p2, q2), (q2, p2)), ((p3, q3), (q3, p3))):
        ans = min(ans, (max(s1, s2) + s3) * max(t1 + t2, t3))
print(ans)