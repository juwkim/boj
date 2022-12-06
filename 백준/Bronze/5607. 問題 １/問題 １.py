A, B = 0, 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        A += a + b
    elif a < b:
        B += a + b
    else:
        A += a
        B += b
print(A, B) 