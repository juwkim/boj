g = lambda: [*map(int, input().split())]

a, b, c = g(), g(), g()
ans = 'WINNER WINNER CHICKEN DINNER!'
if a[0] == b[0] == c[0]:
    ans = 'WHERE IS MY CHICKEN?'
elif (b[0] - a[0]) * (c[1] - a[1]) == (c[0] - a[0]) * (b[1] - a[1]):
    ans = 'WHERE IS MY CHICKEN?'
print(ans)