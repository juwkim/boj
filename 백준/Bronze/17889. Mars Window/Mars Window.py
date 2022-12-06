y = int(input())
r1, q1 = divmod(12 * (y - 2018) - 3, 26)
r2, q2 = divmod(12 * (y - 2018) + 8, 26)
if r1 < r2 or q1 == 0:
    print('yes')
else:
    print('no')