a, b = 1, 0
for _ in range(int(input())):
    a, b = (a + b) % 15746, a
print(a)