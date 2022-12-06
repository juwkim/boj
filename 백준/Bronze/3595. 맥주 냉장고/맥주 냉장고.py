n = int(input())
min_area = 99999999
for i in range(1, 1 + round(n**(1/3))):
    if n / i == n // i:
        a = n // i
        for j in range(1, 1 + round(a**.5)):
            if a / j == a // j:
                b = a // j
                area = 2*(i*j + i*b + j*b)
                if area < min_area:
                    min_area = area
                    x, y, z = i, j, b
print(x, y, z)