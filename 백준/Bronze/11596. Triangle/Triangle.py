a1, b1, c1 = sorted(map(int, input().split()))
a2, b2, c2 = sorted(map(int, input().split()))
print('YES' if (a1, b1, c1) == (a2, b2, c2) and a1**2 + b1**2 == c1**2 else 'NO')