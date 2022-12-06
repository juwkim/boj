root5 = 5**.5
a, b = (1 + root5) / 2, (1 - root5) / 2
n = int(input()) + 2
print(2 * round((a**n - b**n) / root5))