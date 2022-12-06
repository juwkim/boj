D, R, T = [int(input()) for _ in range(3)]

rita, theo = (D + 6) * (D - 1) // 2, 0

num = 3
while rita + theo != R + T:
    rita += num + D
    theo += num
    num += 1
print(R - rita)