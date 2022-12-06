n = int(input()) % (15*10**5)
a, b = 0, 1
for i in range(n):
    a, b = b, (a + b) % 10**6
print(a)