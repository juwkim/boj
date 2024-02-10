a, b = map(int, input().split())
two, num = 0, 2
while b // num != (a - 1) // num:
    two += 1
    num <<= 1
five, num = 0, 5
while b // num != (a - 1) // num:
    five += 1
    num *= 5
print(min(two, five))