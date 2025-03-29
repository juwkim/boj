a, b, c = map(int, input().split())
print(a + (a - a // c) * b)