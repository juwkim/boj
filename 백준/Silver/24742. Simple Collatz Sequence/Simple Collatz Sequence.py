a, b = 0, 1
for _ in range(int(input())):
    a, b = b, (a + b) % 1000007
print(a)