n, a, b = map(int, input().split())
if 2 * a <= n:
    if 2 * b <= n:
        move = "U" * (n - 1) + "L" * (n - 1) + "D" * (a - 1) + "R" * (b - 1)
    else:
        move = "U" * (n - 1) + "R" * (n - 1) + "D" * (a - 1) + "L" * (n - b)
elif 2 * b <= n:
    move = "L" * (n - 1) + "D" * (n - 1) + "U" * (n - a) + "R" * (b - 1)
else:
    move = "D" * (n - 1) + "R" * (n - 1) + "U" * (n - a) + "L" * (n - b)
print(move)