a, b, c = 0, 0, 1
for _ in range(int(input())):
    a, b, c = b, c, (a + c) % 1_000_000_009
print(c)