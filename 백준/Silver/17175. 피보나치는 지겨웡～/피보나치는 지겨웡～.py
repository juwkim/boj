a, b = -1, 1
for i in range(int(input())):
    a, b = b, (a + b + 1) % 1_000_000_007
print(b)