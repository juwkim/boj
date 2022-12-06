n = int(input())
a = int(n**.5)
if n == a * a:
    print(a, a)
elif n <= a * (a + 1):
    print(a, a + 1)
else:
    print(a + 1, a + 1)