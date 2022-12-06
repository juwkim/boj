count = 0
for i, s in enumerate(''.join([input() for _ in range(4)])):
    if s != '.':
        r1, q1 = divmod(i, 4)
        r2, q2 = divmod(ord(s) - 65, 4)
        count += abs(r1 - r2) + abs(q1 - q2)
print(count)